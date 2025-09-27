#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import subprocess

## Links Activator #####################################################################################################

def activate_links_filter(html_template, dirpath):
	dir = dirpath.rstrip('/')
	lines = html_template.split('\n')
	relative_path = '/' + os.path.relpath(dir, root_dir()).replace('\\', '/')

	result_lines = []
	for line in lines:
		if '%ACTIVATION%' in line:
			start = line.find('href="') + len('href="')
			end = line.find('"', start)
			href = line[start:end].rstrip('/')
			# Ensure href_path starts with "/" char.
			if not href.startswith('/'):
				href = '/' + href
			activation = 'active' if relative_path == href or relative_path.startswith(href + '/') else 'inactive'
			# Home page workaround.
			if relative_path == '/.' and href == '/':
				activation = 'active'
			line = line.replace('%ACTIVATION%', activation)
		result_lines.append(line)
	return '\n'.join(result_lines)

## File Walker #########################################################################################################

def root_dir():
	return os.path.dirname(os.path.abspath(__file__))

def on_dir(dirname, filename):
	return os.path.join(dirname, filename)

def on_root(filename):
	return on_dir(root_dir(), filename)

def del_file(filename):
	if os.path.isfile(filename):
		try:
			os.remove(filename)
		except Exception as exception:
			print(f'Error: Cannot delete "{filename}" file!\n{exception}', file=sys.stderr)

def read_html(filename):
	try:
		with open(filename, 'r', encoding='utf-8') as file:
			content = file.read()
		return content
	except Exception as exception:
		print(f'Error: Cannot read "{filename}" file!\n{exception}', file=sys.stderr)
		return None

def save_html(filename, content):
	try:
		with open(filename, 'w', encoding='utf-8') as file:
			file.write(content)
	except Exception as exception:
		print(f'Error: Cannot write "{filename}" file!\n{exception}', file=sys.stderr)

def walk_all_files(dirname, html_template, markdown_generator):
	# Count all files first.
	count_all = 0
	for dirpath, dirnames, filenames in os.walk(dirname):
		if any(file in filenames for file in ['tabs.html', 'tabs-inner.html', 'content.md']):
			count_all += 1

	print(f'Found {count_all} files in "{dirname}".')
	print()

	# Generate index.html files.
	count_page = 0
	for dirpath, dirnames, filenames in os.walk(dirname):
		if any(file in filenames for file in ['tabs.html', 'tabs-inner.html', 'content.md']):
			html = html_template

			if 'tabs.html' in filenames:
				html = html.replace('<!-- %TABS% -->', read_html(on_dir(dirpath, 'tabs.html')))

			if 'tabs-inner.html' in filenames:
				html = html.replace('<!-- %TABS-INNER% -->', read_html(on_dir(dirpath, 'tabs-inner.html')))

			if 'content.md' in filenames:
				execute_markdown_generator(
					markdown_generator,
					on_dir(dirpath, 'content.md'),
					on_dir(dirpath, 'markdown.html')
				)

				html = html.replace('<!-- %MARKDOWN% -->', read_html(on_dir(dirpath, 'markdown.html')))

				# Delete generated file after use.
				del_file(on_dir(dirpath, 'markdown.html'))

			# Delete previous rendered "index.html" if any.
			del_file(on_dir(dirpath, 'index.html'))

			html = activate_links_filter(html, dirpath)
			save_html(on_dir(dirpath, 'index.html'), html)
			count_page += 1
			print(f'Compiled [{count_page:04}/{count_all:04}]: {on_dir(dirpath, "index.html")}')

## Markdown ############################################################################################################

def try_to_find_markdown_generator():
	# Try to find markdown generator in PATH environment variable first.
	system_markdown_generator = shutil.which('pandoc')
	found_in_path = bool(system_markdown_generator)

	# Try to find markdown generator in the project root directory second.
	local_markdown_generator = on_root('pandoc.exe' if os.name == 'nt' else 'pandoc')
	found_in_root = (os.path.isfile(local_markdown_generator) and os.access(local_markdown_generator, os.X_OK))

	# Use local markdown generator instead of system one if present.
	if found_in_root:
		return local_markdown_generator
	if found_in_path:
		return system_markdown_generator
	print('Error: Markdown generator executable not found in the "PATH" or root project directory.', file=sys.stderr)
	return None

def execute_markdown_generator(markdown_generator, file_in, file_out):
	pandoc_lua_filter = on_root('pandoc-filters.lua')
	command_with_args = [markdown_generator]
	command_with_args.extend([
		file_in,
		'-f', 'gfm+gfm_auto_identifiers+hard_line_breaks',
		'-t', 'html',
		'--lua-filter', pandoc_lua_filter,
		'-o', file_out
	])
	try:
		result = subprocess.run(command_with_args, check=True)
		return result.returncode
	except subprocess.CalledProcessError as error:
		print(f'Error: Markdown generator execution failed:\n{error}', file=sys.stderr)
		return error.returncode

## Entry Point #########################################################################################################

def main():
	print('Static Site Generator (SSG) v0.9 by EXL, 2025')
	print()

	if len(sys.argv) > 2:
		print('Usage:', file=sys.stderr)
		print('\t./build.py', file=sys.stderr)
		print('\t./build.py path/to/directory', file=sys.stderr)
		return 1

	markdown_generator = try_to_find_markdown_generator()
	html_template = read_html(on_root('index_template.html'))
	if markdown_generator and html_template:
		walk_all_files(sys.argv[1] if (len(sys.argv) == 2) else root_dir(), html_template, markdown_generator)
		return 0

	return 1

if __name__ == '__main__':
	sys.exit(main())

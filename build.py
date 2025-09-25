#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

from shutil import which

## Links Activator #####################################################################################################

def activate_links(template, dirpath):
	lines = template.split('\n')
	result_lines = []
	base_dir = os.path.dirname(os.path.abspath(__file__))
	dir_path = dirpath.rstrip('/')
	relative_path = '/' + os.path.relpath(dir_path, base_dir).replace('\\', '/')

	for line in lines:
		if '%ACTIVATION%' in line:
			start = line.find('href="') + len('href="')
			end = line.find('"', start)
			href = line[start:end].rstrip('/')
			# Ensure href_path starts with /
			if not href.startswith('/'):
				href = '/' + href
			activation = 'active' if relative_path == href or relative_path.startswith(href + '/') else 'inactive'
			if relative_path == '/.' and href == '/':
				activation = 'active'
			line = line.replace('%ACTIVATION%', activation)
		result_lines.append(line)
	return '\n'.join(result_lines)

## File Walker #########################################################################################################

def walk_files(template, markdown):
	for dirpath, dirnames, filenames in os.walk(os.path.dirname(os.path.abspath(__file__))):
		html_to_write = template
		found = False
		if 'tabs.html' in filenames:
			tabs = read_text_file(dirpath, 'tabs.html')
			html_to_write = html_to_write.replace('<!-- %TABS% --->', tabs)
			found = True
		if 'content.md' in filenames:
			full_path = os.path.join(dirpath, 'content.md')
			markdown_html = os.path.join(dirpath, 'markdown.html')
			execute_md_gen(markdown, full_path, markdown_html)
			html = read_text_file(dirpath, 'markdown.html')
			html_to_write = html_to_write.replace('<!-- %MARKDOWN% --->', html)
			# Delete generated file after use.
			try:
				os.remove(markdown_html)
			except Exception as e:
				print(f'Error deleting {markdown_html}: {e}')
			found = True
		if found:
			print(f'Regenerated: {os.path.join(dirpath, "index.html")}')
			html_to_write = activate_links(html_to_write, dirpath)
			save_html_page(html_to_write, dirpath, 'index.html')

def read_text_file(directory, filename):
	try:
		path = os.path.join(directory, filename) if directory else filename
		with open(path, 'r', encoding='utf-8') as f:
			content = f.read()
		return content
	except FileNotFoundError:
		print(f'File not found: {path}')
		return None
	except Exception as e:
		print(f'Error reading {path}: {e}')
		return None

def save_html_page(content, directory, filename):
	try:
		path = os.path.join(directory, filename) if directory else filename
		with open(path, 'w', encoding='utf-8') as file:
			file.write(content)
	except Exception as e:
		print(f'Error writing {path}: {e}')

## Markdown ############################################################################################################

def find_md_gen():
	# Try to find markdown generator in PATH environment variable.
	md_path = which('pandoc')
	if md_path:
		return md_path

	script_dir = os.path.dirname(os.path.abspath(__file__))
	local_md = os.path.join(script_dir, 'pandoc.exe' if os.name == 'nt' else 'pandoc')
	if os.path.isfile(local_md) and os.access(local_md, os.X_OK):
		return local_md

	print('Markdown generator executable not found in PATH or script directory.', file=sys.stderr)

	return None

def execute_md_gen(md, file_in, file_out):
	lua_filter = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pd-anchor-links.lua')
	cmd = [md]
	cmd.extend([
		file_in,
		'-f', 'gfm+gfm_auto_identifiers+hard_line_breaks',
		'-t', 'html',
		'--lua-filter', lua_filter,
		'-o', file_out
	])
	try:
		result = subprocess.run(cmd, check=True)
		return result.returncode
	except subprocess.CalledProcessError as e:
		print(f'Markdown generator execution failed: {e}', file=sys.stderr)
		return e.returncode

## Entry Point #########################################################################################################

def main():
	print('Simple Static Site Generator v0.9')
	print('EXL, 2025')
	print()
	markdown = find_md_gen()
	template = read_text_file(os.path.dirname(os.path.abspath(__file__)), 'index_.html')
	if markdown and template:
		walk_files(template, markdown)

if __name__ == '__main__':
	main()

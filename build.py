#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

from shutil import which

## File Walker #########################################################################################################

def walk_files(template, pandoc):
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
			execute_pandoc(
				pandoc,
				[full_path, '-f', 'gfm', '-t', 'html', '-o', markdown_html]
			)
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

## Pandoc ##############################################################################################################

def find_pandoc():
	# Try to find pandoc in PATH environment variable.
	pandoc_path = which('pandoc')
	if pandoc_path:
		return pandoc_path

	script_dir = os.path.dirname(os.path.abspath(__file__))
	local_pandoc = os.path.join(script_dir, 'pandoc.exe' if os.name == 'nt' else 'pandoc')
	if os.path.isfile(local_pandoc) and os.access(local_pandoc, os.X_OK):
		return local_pandoc

	print('Pandoc executable not found in PATH or script directory.', file=sys.stderr)

	return None

def execute_pandoc(pandoc, args=None):
	cmd = [pandoc]
	if args:
		cmd.extend(args)

	try:
		result = subprocess.run(cmd, check=True)
		return result.returncode
	except subprocess.CalledProcessError as e:
		print(f'Pandoc execution failed: {e}', file=sys.stderr)
		return e.returncode

## Entry Point #########################################################################################################

def main():
	print('Simple Static Site Generator, 2025, EXL')
	print()
	pandoc = find_pandoc()
	template = read_text_file(os.path.dirname(os.path.abspath(__file__)), 'index_.html')
	if pandoc and template:
		walk_files(template, pandoc)

if __name__ == '__main__':
	main()

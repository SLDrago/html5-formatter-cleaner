import re
from bs4 import BeautifulSoup, Comment
import argparse
import cssbeautifier
import jsbeautifier

class HTMLFormatException(Exception):
    pass

class HTMLFormatter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.soup = None
        self.void_elements = {
            'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 
            'link', 'meta', 'param', 'source', 'track', 'wbr'
        }
        self.inline_elements = {
            'a', 'abbr', 'acronym', 'b', 'bdo', 'big', 'br', 'button', 'cite', 'code',
            'dfn', 'em', 'i', 'img', 'input', 'kbd', 'label', 'map', 'object', 'output',
            'q', 'samp', 'script', 'select', 'small', 'span', 'strong', 'sub', 'sup',
            'textarea', 'time', 'tt', 'var'
        }

    def read_file(self):
        with open(self.input_file, 'r', encoding='utf-8') as file:
            return file.read()

    def write_file(self, content):
        with open(self.output_file, 'w', encoding='utf-8') as file:
            file.write(content)

    def parse_html(self, content):
        self.soup = BeautifulSoup(content, 'html.parser')

    def format_html(self):
        self.remove_comments()
        self.remove_empty_tags()
        self.ensure_proper_nesting(self.soup)
        self.handle_void_elements()
        self.format_internal_css()
        self.format_internal_js()
        self.handle_whitespace()

    def remove_comments(self):
        for comment in self.soup.find_all(text=lambda text: isinstance(text, Comment)):
            comment.extract()

    def remove_empty_tags(self):
        for tag in self.soup.find_all():
            if tag.name not in self.void_elements and not tag.contents and not tag.string:
                tag.extract()

    def ensure_proper_nesting(self, element):
        for child in element.children:
            if child.name:
                if child.name in ['p', 'div'] and child.find_all(['p', 'div']):
                    self.unwrap_invalid_children(child)
                self.ensure_proper_nesting(child)

    def unwrap_invalid_children(self, tag):
        invalid_children = tag.find_all(['p', 'div'])
        for invalid_child in invalid_children:
            invalid_child.unwrap()

    def handle_void_elements(self):
        for tag in self.soup.find_all():
            if tag.name in self.void_elements and tag.is_empty_element:
                tag.attrs['self-closed'] = True  # Handle as self-closed if empty

    def format_internal_css(self):
        for style in self.soup.find_all('style'):
            if style.string:
                style.string = cssbeautifier.beautify(style.string)

    def format_internal_js(self):
        for script in self.soup.find_all('script'):
            if script.string:
                script.string = jsbeautifier.beautify(script.string)

    def handle_whitespace(self):
        for tag in self.soup.find_all():
            if tag.name not in self.inline_elements:
                if tag.string:
                    tag.string = tag.string.strip()
            else:
                if tag.string:
                    tag.string = ' '.join(tag.string.split())

    def run(self):
        try:
            content = self.read_file()
            self.parse_html(content)
            self.format_html()
            formatted_html = self.soup.prettify(formatter='html5')
            self.write_file(formatted_html)
            print(f"HTML formatted successfully. Output written to {self.output_file}")
        except Exception as e:
            raise HTMLFormatException(f"Error formatting HTML: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Format and clean HTML files")
    parser.add_argument("input_file", help="Path to the input HTML file")
    parser.add_argument("output_file", help="Path to the output HTML file")
    args = parser.parse_args()

    formatter = HTMLFormatter(args.input_file, args.output_file)
    formatter.run()

if __name__ == "__main__":
    main()

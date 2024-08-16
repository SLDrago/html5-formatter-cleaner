# HTML5 Formatter and Cleaner

This Python script provides a comprehensive solution for formatting and cleaning HTML5 files. It handles all HTML5 tags, formats internal CSS and JavaScript, manages whitespace, and ensures proper nesting of elements.

## Features

- Formats and cleans HTML5 documents
- Handles all HTML5 tags, including void and inline elements
- Formats internal CSS using cssbeautifier
- Formats internal JavaScript using jsbeautifier
- Removes comments and empty tags
- Ensures proper nesting of elements
- Intelligently manages whitespace
- Preserves structure while improving readability

## Requirements

- Python 3.6+
- BeautifulSoup4
- cssbeautifier
- jsbeautifier

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/html5-formatter-cleaner.git
   cd html5-formatter-cleaner
   ```

2. Install the required packages:
   ```
   pip install beautifulsoup4 cssbeautifier jsbeautifier
   ```

## Usage

Run the script from the command line, providing input and output file paths:

```
python html_formatter.py input.html output.html
```

Replace `input.html` with the path to your HTML file that needs formatting, and `output.html` with the desired path for the formatted result.

## How It Works

1. The script reads the input HTML file.
2. It uses BeautifulSoup to parse the HTML structure.
3. Comments are removed, and empty tags are cleaned up.
4. The script ensures proper nesting of elements, preventing invalid structures.
5. Internal CSS and JavaScript are formatted using their respective beautifiers.
6. Whitespace is managed based on whether elements are inline or block-level.
7. The formatted HTML is written to the output file.

## Customization

You can customize the behavior of the formatter by modifying the `HTMLFormatter` class. For example, you can adjust the sets of `void_elements` and `inline_elements` if you need to handle additional tags differently.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- BeautifulSoup4 for HTML parsing
- cssbeautifier for CSS formatting
- jsbeautifier for JavaScript formatting

## Contact

If you have any questions or feedback, please open an issue in this repository.

---

Happy HTML formatting!

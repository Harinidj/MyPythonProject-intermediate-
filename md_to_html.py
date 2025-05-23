import markdown
import sys
import os

def convert_markdown_to_html(input_path: str, output_path: str) -> None:
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' does not exist.")
        return

    with open(input_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    if not markdown_text.strip():
        print("Error: The markdown file is empty.")
        return

    html_output = markdown.markdown(markdown_text)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_output)

    print(f"Success! HTML saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python markdown_converter.py <input_markdown_file> <output_html_file>")
        sys.exit(1)

    convert_markdown_to_html(sys.argv[1], sys.argv[2])

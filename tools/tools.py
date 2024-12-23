def write_markdown_file(content, filename):
    """Writes the given content as a markdown file to the local directory.

    Args:
        content: The string content to write to the file.
        filename: The filename to save the file as.
    """
    import os

    # Check if the file exists
    filepath = f"{filename}.md"
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write(content)
            print(f"File '{filepath}' created successfully.")
    else:
        print(f"File '{filepath}' already exists.")

def test_write_markdown_file():
    """Test the write_markdown_file function."""
    import os

    # Test content and filename
    test_content = "# Test Markdown File\nThis is a test content for the markdown file."
    test_filename = "test_markdown"

    # Ensure the file does not exist before the test
    filepath = f"{test_filename}.md"
    if os.path.exists(filepath):
        os.remove(filepath)

    # Test file creation
    write_markdown_file(test_content, test_filename)
    assert os.path.exists(filepath), "File was not created."

    # Test file existence handling
    write_markdown_file(test_content, test_filename)

    # Clean up test file
    if os.path.exists(filepath):
        os.remove(filepath)

    print("All tests passed.")

# Run the test
#test_write_markdown_file()
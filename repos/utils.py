import difflib

def compare_files(file1_content, file2_content):
    differ = difflib.Differ()
    diff = differ.compare(file1_content.splitlines(), file2_content.splitlines())
    return '\n'.join(diff)

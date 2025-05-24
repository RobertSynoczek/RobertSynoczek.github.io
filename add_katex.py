import argparse

katex_snippet = '''<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.css" integrity="sha384-5TcZemv2l/9On385z///+d7MSYlvIEw9FuZTIdZ14vJLqWphw7e7ZPuOiCHJcFCP" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.js" integrity="sha384-cMkvdD8LoxVzGF/RPUKAcvmm49FQ0oxwDF3BGKtDXcEc+T1b2N+teh/OJfpU0jr6" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/contrib/auto-render.min.js" integrity="sha384-hCXGrW6PitJEwbkoStFjeJxv+fSOOQKOPbJxSfM6G5sWZjAyWhXiTIIAmQqnlLlh" crossorigin="anonymous"
    onload="renderMathInElement(document.body);"></script>
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Insert KaTeX snippet into an HTML file.")
    parser.add_argument("-f","--filename", help="Path to the HTML file to modify")

    args = parser.parse_args()
    filename = args.filename

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    if '</body>' not in content:
        raise ValueError("The </body> tag was not found in the file.")

    updated_content = content.replace('</body>', katex_snippet + '\n</body>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"KaTeX snippet inserted into {filename}")

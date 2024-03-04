import re
import sys

def replacetitle(match):
    counter = len(match.group(1))
    replace = f'<h{counter}>{match.group(2)}</h{counter}>'
    return replace

def replacelist(match):
    items = f'<ol>{match.group(1)}\n</ol>'
    return items


def parser2(file: str):

    file = re.sub(r'\`(.*?)\`',r'<code>\1</code>', file)

    file = re.sub(r'^\d\.(.*)(\n|\Z)',r'<li>\1</li>', file, flags=re.MULTILINE) 

    file = re.sub(r'<li>(.*)</li>',r'<ol><li>\1</li>\n</ol>\n', file)

    file = re.sub(r'<li>(.*?)</li>',r'\n<li>\1</li>', file)

    file = re.sub(r'^(#+)\s+(.*)$', replacetitle, file, flags=re.MULTILINE)
    
    # Bold
    file = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', file)
    
    # Itálico
    file = re.sub(r'\*(.*?)\*', r'<i>\1</i>', file)

    # Lista numerada

    # Imagem
    file = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', file)

    # Link
    file = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', file)

    return file
    

def main(md_file):
    with open(md_file, 'r') as f:
        with open('convertedfile.html', 'w') as arq:
            file = f.read()
            arq.write(parser2(file))

if __name__ == "__main__":
    main(sys.argv[1])
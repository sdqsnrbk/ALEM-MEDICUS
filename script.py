import lorem

def generate_lorem_paragraphs(n=3):
    paragraphs = [lorem.paragraph() for _ in range(n)]
    return '\n\n'.join(paragraphs)

if __name__ == "__main__":
    print(generate_lorem_paragraphs(5))

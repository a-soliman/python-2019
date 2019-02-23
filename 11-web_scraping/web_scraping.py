from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
    <head></head>
    <body>
        <h1>This is a title</h1>
        <p class="subtitle">this is a subtitle</p>
        <ul>
            <li>JaveScript</li>
            <li>Python</li>
            <li>Go Lang</li>
        </ul>
    </body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, "html.parser")


def get_list_items():
    list_items = [item.string for item in simple_soup.find_all("li")]
    print(list_items)


get_list_items()

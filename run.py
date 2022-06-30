from gc import get_debug
from project import create_app, parser

app = create_app()

if __name__ == "__main__":
    app.run(debug=parser.get_debug_mode())
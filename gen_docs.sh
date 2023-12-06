pip install pydoc
pip install dotenv-cli

# Create documentation
dotenv -e api/.env pdoc -o docs api

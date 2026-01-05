# phython_rag-bot
it is a bot which analyse data stored in databse and answer queries

py -m venv venv  // to create python environment
.\venv\Scripts\Activate.ps1 // activate environment
pip install langchain langchain-community langchain-chroma langchain-ollama langchain-text-splitters chromadb pypdf 

python populate_database.py --reset
python query_data.py


ensure this should run on terminal
$env:OLLAMA_HOST="http://127.0.0.1:11434"

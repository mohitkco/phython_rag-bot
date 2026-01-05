# phython_rag-bot
it is a bot which analyse data stored in databse and answer queries

when you open folder for the first time try to open via terminal using code . 


py -m venv venv  // to create python environment
.\venv\Scripts\Activate.ps1 // activate environment
pip install langchain langchain-community langchain-chroma langchain-ollama langchain-text-splitters chromadb pypdf 

python populate_database.py --reset
python query_data.py


you also need to download a ai bot and processor is following
download from https://ollama.com/ and install it
then run these two in terminal
ollama pull mistral
ollama pull nomic-embed-text

ensure this should run on terminal
$env:OLLAMA_HOST="http://127.0.0.1:11434"

# Llama 3.2:3B Hospital Medical Customer Service

A chatbot as a customer service in a hospital, while a customer service in a hospital usually doesn't answer a medical question, now with this chatbot, it can. 

## Getting Started

Simply clone this repo by doing.
`git clone https://github.com/DickyAdi/llama_medical_cs.git`

### build with

- Python 3.11.7
- Langchain
- Langgraph
- FastAPI
- Ollama

### Installing

This project is developed in a cloud vm as it requires an LLM backend which dependent on a GPU. Therefore, to fire up this project migh be different in each device you have. However, here i give you how do i set up this project with some of my script.

1. make sure you already in the root of the project and then run this code below in the terminal. (open the script to see what does it do)
    ```
    ./database_setup.sh
    ```
2. after a while, it will asks for a database password 2 times, write `root` unless you have your own password.
3. after the process finish, it will run ollama backend in the terminal.
4. open new terminal and run
    ```
    ./model_pull.sh
    ```
    this will run llama3.2:3B prompt template modification. ([why?](#prompt-template-modification))
5. in the same terminal, run
    ```
    cd medical_cs
    fastapi dev main.py
    ```
    this will fire up the fastapi
6. project is on! you can go hit the API using curl or open it on a browser

## Authors

  - **Billie Thompson** - *Provided README Template* -
    [PurpleBooth](https://github.com/PurpleBooth)
  - **Dicky Adi** - *Developing the project* -
    [K y c d i A](https://github.com/DickyAdi)
  - **Meta AI** - *Provided Llama 3.2:3B* -
    [Meta-llama](https://github.com/meta-llama)


## License

This project is licensed under the [MIT License](LICENSE) alongside [llama license](LLAMA_LICENSE)


## Prompt template modification
While developing the project, the LLM's tool calling is not really that good. After some research in the internet, i found [this](https://github.com/ollama/ollama/issues/6127#issuecomment-2264291170)

## Things To-Do in the future

 - ~~Initiate github repo~~
 - Refactor and make the code look cleaner and easier to work with.
 - Proper code comment documentation
 - Docker it!
 
If you have something in mind with this list, feel free to open up an [issue](https://github.com/DickyAdi/llama_medical_cs/issues)
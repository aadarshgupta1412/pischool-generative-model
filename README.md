# Pi School Challenge: Business application discovery of LLMs

## Overview

This project aims to explore the opportunities for leveraging the state-of-the-art Language Models (LLMs) in various industries. Specifically, the project focuses on the application of LLMs in chatbots and the importance of prompt engineering in enhancing the quality of the chatbot's response.

**Problem:** No automated and well-defined way to evaluate the effectiveness of chatbots

### Goals

1. Create a workshop on Prompt Engineering techniques
2. Develop a Chatbot Benchmarking tool leveraging LLMs while also the framework to interact with the deployed chatbots
3. Study and devise metrics to evaluate the effectiveness of chatbots

### Setup Instructions

1. Clone the repository

   ```sh
   git clone https://github.com/PiSchool/pischool-generative-models.git
   ```

2. Install the dependencies

   ```sh
   pip install -r requirements.txt
   pip install -e .
   ```

3. Run the project

   ```sh
   streamlit run scripts/runner.py
   ```

## Directory structure

Update appropriately before handing over this repository. You may want to add other directories/files or remove those you don't need.

```
|── chatbot_eval
|    |── LLM           <- Contains the LLM Client for Converstaion/Evaluation
|    |── chatbots      <- Contain the Chatbot Interaction Logic
|    |── utils         <- Contains the browser driver utils
│
├── scripts            <- Contains the runner script for the application
│
├── notebooks          <- Contains the Jupter Notebook for the application. However, to access the updated code please refer to this scripts.
│
├── requirements.txt   <- Required packages (dependencies)
│
│
├── setup.py           <- makes project pip installable (pip install -e .) so
│                         that `your_package_name` can be imported

```

## How to install

This project requires ChromeDriver to run. Please ensure to have a Chrome browser installed in your system.

After cloning the repo, enter the project folder and create a virtual env.

```
python3 -m venv env
```

Initialise the virtual env

```
. env/bin/activate
```

Now, install the dependencies using the following command:

```
pip3 install -r requirements.txt
```

We have the dependencies installed and are ready to run the project. But before that, we add the `OPENAI_KEY` and `DEBUG` env variables in the `.env` file

```
# .env
OPENAI_KEY=<YOUR_OPENAI_KEY>
DEBUG=<DEBUG_MODE>
```

## How to run

```
streamlit run ./scripts/runner.py -- --conversation_length=[conv_length]
```

Here, argument `conversation_length` refers to the maximum number of interactions GPT can have with the chatbot before deciding the verdict.



## The team

This challenge, sponsored by Pi School, was carried out by Aadarsh Gupta, Neeraj Rajpurohit and Shubhanshu Saxena as part of the 12th edition of Pi School's School of AI program.
| Aadarsh Gupta | Neeraj Rajpurohit | Shubhanshu Saxena |
| ------------- | ------------- | ------------- |
| ![Aadarsh Gupta](https://avatars.githubusercontent.com/u/62350692?v=4) | ![Neeraj Rajpurohit](https://avatars.githubusercontent.com/u/31539812?v=4) | ![Shubhanshu Saxena](https://avatars.githubusercontent.com/u/54344426?v=4)
| Bio for the Aadarsh Gupta | Bio for the Neeraj Rajpurohit | Bio for the Shubhanshu Saxena |
| <img src="https://camo.githubusercontent.com/b079fe922f00c4b86f1b724fbc2e8141c468794ce8adbc9b7456e5e1ad09c622/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f6769746875622e737667" width="20"> [aadarshgupta1412](https://github.com/aadarshgupta1412/)<br/> <img src="https://camo.githubusercontent.com/c8a9c5b414cd812ad6a97a46c29af67239ddaeae08c41724ff7d945fb4c047e5/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f6c696e6b6564696e2e737667" width="20"> [aadarshgupta1412](https://www.linkedin.com/in/aadarshgupta1412/)<br/> <img src="https://camo.githubusercontent.com/35b0b8bfbd8840f35607fb56ad0a139047fd5d6e09ceb060c5c6f0a5abd1044c/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f747769747465722e737667" width="20"> [@imaadarshgupta](https://twitter.com/imaadarshgupta/) | <img src="https://camo.githubusercontent.com/b079fe922f00c4b86f1b724fbc2e8141c468794ce8adbc9b7456e5e1ad09c622/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f6769746875622e737667" width="20"> [neeraj3029](https://github.com/neeraj3029)<br/> <img src="https://camo.githubusercontent.com/c8a9c5b414cd812ad6a97a46c29af67239ddaeae08c41724ff7d945fb4c047e5/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f6c696e6b6564696e2e737667" width="20"> [Neeraj Rajpurohit](https://www.linkedin.com/in/nrajpurohit/)<br/> <img src="https://camo.githubusercontent.com/35b0b8bfbd8840f35607fb56ad0a139047fd5d6e09ceb060c5c6f0a5abd1044c/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f747769747465722e737667" width="20"> [@neerajr_](https://twitter.com/neerajr_) | <img src="https://camo.githubusercontent.com/b079fe922f00c4b86f1b724fbc2e8141c468794ce8adbc9b7456e5e1ad09c622/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f6769746875622e737667" width="20"> [shubhanshu02](https://github.com/shubhanshu02)<br/> <img src="https://camo.githubusercontent.com/c8a9c5b414cd812ad6a97a46c29af67239ddaeae08c41724ff7d945fb4c047e5/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f6c696e6b6564696e2e737667" width="20"> [Shubhanshu Saxwna](https://www.linkedin.com/in/shubhanshu-saxena/)<br/> <img src="https://camo.githubusercontent.com/35b0b8bfbd8840f35607fb56ad0a139047fd5d6e09ceb060c5c6f0a5abd1044c/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f747769747465722e737667" width="20"> [](https://twitter.com/your_twitter_handle) |

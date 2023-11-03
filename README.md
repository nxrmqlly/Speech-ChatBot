# Speech-ChatBot

Speech-ChatBot is a simple chatbot that utilizes the brainshop.ai API to provide natural language conversation capabilities. This README will guide you through the process of setting up and using the Speech-ChatBot with the brainshop.ai API.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Running the ChatBot](#running-the-chatbot)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you can use the Speech-ChatBot, you need to have the following prerequisites:

1. Python 3.x (<=3.12.0 for compatibility issues) installed on your system.
2. An API key from brainshop.ai. You can sign up for an API key at [https://brainshop.ai](https://brainshop.ai).

### Installation

1. Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/nxrmqlly/speech-chatbot.git
   ```

2. Change to the project directory:

   ```bash
   cd speech-chatbot
   ```

3. Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Configuration

**1.** Before you can use the Speech-ChatBot, you need to configure it with your brainshop.ai API key and Brain ID. Create (in `./`) and open the `secret.env` file in a text editor and replace `YOUR_API_KEY_HERE` and `YOUR_BRAIN_ID_HERE` with your actual API key and Brain ID:

```bash
# secret.env

# Replace "YOUR_API_KEY_HERE" with your brainshop.ai API key
BS_KEY="YOUR_API_KEY_HERE"
# Replace "YOUR_BRAIN_ID_HERE" with your brainshop.ai Brain ID
BS_ID="YOUR_BRAIN_ID_HERE"

```
**2.** Train your Brain at https://brainshop.ai including attributes and other models.


### Running the ChatBot

To start the Speech-ChatBot, simply run the following command:

```bash
python . # Or python __main__.py
```

The chatbot will start and display a prompt for you to speak through your microphone. It will send your messages to the brainshop.ai API and display the chatbot's responses.

Feel free to have a natural conversation with the chatbot. You can use it for various purposes, including answering questions, providing information, or just engaging in casual conversation.

## Contributing

If you'd like to contribute to the development of the Speech-ChatBot, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Push your branch to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the Apache-2.0 license - see the [LICENSE](LICENSE) file for details.
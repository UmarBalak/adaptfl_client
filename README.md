# AdaptFL Client

The AdaptFL Client is a Python-based application designed to handle client-side operations for a federated learning system. It includes functionalities for client registration, data preprocessing, model training, and communication with a central server via WebSockets.

## Table of Contents

- [AdaptFL Client](#adaptfl-client)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [Client Registration](#client-registration)
  - [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/UmarBalak/adaptfl_client.git
    cd adaptfl_client
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the root directory of the project and add environment variables.
2. Ensure that the `client_credentials.json` file is present in the root directory after running the client registration script.

## Usage

### Client Registration

To register the client and obtain client details, run:
```sh
python client_registration.py
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
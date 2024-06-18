# Contributing to Quartz Crystal Microbalance Data Analysis Software

Thank you for your interest in contributing to our project! Your contributions help improve the software and provide value to the QCM-D community. Below are the guidelines to help you get started.

## Code of Conduct

Please note that this project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How to Report Bugs

If you find a bug, please open an issue on GitHub and include as much detail as possible. Provide a clear and descriptive title, and include steps to reproduce the issue, the expected result, and the actual result.

## How to Request Features

To request a new feature, open an issue on GitHub and describe the feature you would like to see, including its benefits and use cases. Provide as much detail as possible to help us understand your request.

## How to Submit Changes

1. Fork the repository.
2. Create a new branch for your changes (`git checkout -b feature-branch`).
3. Make your changes.
4. Ensure your code follows the project's coding style and conventions.
5. Write tests for your changes and ensure all tests pass.
6. Commit your changes (`git commit -m 'Add new feature'`).
7. Push to your branch (`git push origin feature-branch`).
8. Open a pull request on GitHub.

## Development Setup

To set up the development environment, follow these steps:

1. Clone the repository (`git clone https://github.com/your-username/project-name.git`).
2. Install dependencies using a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate   # On mac/linux, use `source venv/bin/activate`
   pip install -r requirements.txt

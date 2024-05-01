# Quizlet Scraper API

A Flask web application that scrapes data from Quizlet when provided with a URL.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Flask web application serves as an API for scraping data from Quizlet. It provides a simple endpoint `/apii` where you can pass a Quizlet URL, and it returns the scraped content.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/quizlet-scraper-api.git
    cd quizlet-scraper-api
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

## Usage

Once the application is running, you can access it at `http://localhost:5000/`.

## API Endpoints

- `/apii?url=(pdf_url)`: GET request to this endpoint with a Quizlet URL as a parameter to retrieve scraped content.

## Dependencies

- Flask: Web framework for building the API.
- Requests: HTTP library for making requests to Quizlet.
- BeautifulSoup: Library for parsing HTML.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

[MIT License](LICENSE)

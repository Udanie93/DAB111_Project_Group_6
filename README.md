# Heart Disease Prediction

This project is a Python application designed to collect data legally sourced from Data World (https://data.world/) and store it in a SQLite database. It utilizes the pandas library for data manipulation and SQLite for efficient storage. Additionally, the project leverages Flask, a lightweight web framework for Python, to present the collected data through a website.


## Key Features:

- **Data Collection:** Collects data legally from Data World (https://data.world/), ensuring compliance with data usage policies.
- **Data Storage:** Stores the collected data in a SQLite database for efficient management and retrieval.
- **Web Presentation:** Utilizes Flask to serve the stored data through a website, providing an intuitive interface for users to access and interact with the data.


## Project Structure:

- **`/data_collection/`**: Contains scripts for collecting data from Data World (https://data.world/).
- **`/database/`**: Holds the SQLite database file where collected data is stored.
- **`/web_app/`**: Contains the Flask web application for serving the data.
- **`app.py`**: Python script for starting the data collection and web server processes.
- **`requirements.txt`**: Lists the dependencies required for running the project.
- **`README.md`**: This file provides an overview of the project and usage instructions.


## Credits:

- **Data World:** For providing legal access to the data used in this project.
- **Flask:** For the lightweight web framework used to serve the data.

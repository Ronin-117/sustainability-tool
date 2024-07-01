# Sustainable Project Management Tool

## Overview

This web application uses IBM Watsonx API to analyze project ideas and materials, providing insights into their sustainability. Users can input project ideas and materials, and the application will classify their environmental impact and suggest more sustainable alternatives if necessary.

## Features

- **Project Idea Evaluation:** Analyze project ideas and classify them based on their environmental impact.
- **Material Choosing:** Evaluate the sustainability of materials, objects, or processes, and suggest better alternatives.
- **Project Summary:** View a summary of the project ideas and materials analyzed.

## Setup

### Prerequisites

- Python 3.x
- Flask
- IBM Watsonx API credentials

### Installation

1. Clone the repository:

   bash
   git clone https://github.com/yourusername/sustainable-project-management-tool.git
   cd sustainable-project-management-tool
   

2. Install the required Python packages:

   bash
   pip install -r requirements.txt
   

3. Create a `.env` file in the project directory and add your IBM Watsonx API credentials:

   plaintext
   API_URL=https://us-south.ml.cloud.ibm.com
   API_KEY=your_ibm_watsonx_api_key
   PROJECT_ID=b357c08e-c45b-4721-8e03-ffb9c3fa4924
   

4. Run the Flask application:

   bash
   python app.py
   

## Usage

1. Navigate to `http://127.0.0.1:5000/` in your web browser.
2. Use the **Project Idea Evaluation** and **Material Choosing** features to analyze the sustainability of your project ideas and materials.
3. View the **Project Summary** to see a summary of the analyzed ideas and materials.

## Project Structure

- `app.py`: Main Flask application file.
- `templates/`: Directory containing HTML templates.
  - `home.html`: Home page template.
  - `project_mang.html`: Project management page template.
  - `project_idea.html`: Project idea evaluation page template.
  - `mat_cho.html`: Material choosing page template.
  - `credits.html`: Credits page template.
  - `project_summ.html`: Project summary page template.
- `static/`: Directory for static files (CSS, JS, images).
- `requirements.txt`: List of Python packages required for the project.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

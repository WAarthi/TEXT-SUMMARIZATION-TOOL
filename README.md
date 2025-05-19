# TEXT-SUMMARIZATION-TOOL


This project implements a simple text summarization tool using the Natural Language Toolkit (NLTK) library in Python. It takes a text as input and generates a concise summary by identifying the most important sentences.

## Overview

The script `text_summarizer.py` (or whatever you name the file containing the code you provided) uses basic NLP techniques such as tokenization, stop word removal, and word frequency analysis to score sentences and extract the top N sentences as the summary.

## Setup

1.  **Prerequisites:**
    * Python 3.6 or higher
    * pip

2.  **Installation:**
    Clone this repository (if you have one) or simply create a Python file (e.g., `text_summarizer.py`) and paste the provided code into it.

3.  **Install Dependencies:**
    You need to install the NLTK library and download the necessary data (`punkt` for sentence tokenization and `stopwords`). Open your terminal or command prompt and run:

    ```bash
    pip install nltk
    python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
    ```

## How to Use

1.  Save the Python code as `text_summarizer.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script:

    ```bash
    python text_summarizer.py
    ```

    The script includes example usage within the `if __name__ == "__main__":` block, demonstrating how to summarize predefined articles.

5.  You can also use the `summarize_text` function in your own Python scripts by importing it:

    ```python
    from text_summarizer import summarize_text

    my_text = "Your long text here..."
    summary = summarize_text(my_text, num_sentences=2)
    print(summary)
    ```

## Code Description

* `text_summarizer.py`: Contains the Python script with the `summarize_text` function.
    * `summarize_text(text, num_sentences=3)`: This function takes the input text and the desired number of summary sentences as arguments and returns the summary. It performs the following steps:
        * Tokenizes the text into sentences.
        * Tokenizes words and removes stop words.
        * Calculates word frequencies.
        * Scores sentences based on the frequency of their words.
        * Selects the top N sentences to form the summary.

## Example Output

When you run `python text_summarizer.py`, you should see output similar to this:

```
Original Article:

    Artificial intelligence (AI) is a wide-ranging branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence. AI is an interdisciplinary science with multiple approaches, and advancements in machine learning and deep learning are creating a paradigm shift in virtually every sector of the tech industry.

    AI can be applied across many different fields, including healthcare, finance, education, and transportation. In healthcare, AI can assist with diagnosis and drug discovery. In finance, AI algorithms are used for fraud detection and algorithmic trading. Educational applications of AI include personalized learning platforms. Self-driving cars are a prominent example of AI in transportation.

    The development of AI raises several ethical considerations. Concerns about job displacement due to automation and the potential for bias in AI algorithms are actively being discussed. Ensuring fairness and transparency in AI systems is a crucial area of research and development.

    Despite these challenges, the potential benefits of AI are immense. From solving complex problems to improving efficiency and creating new opportunities, AI continues to be a rapidly evolving and transformative technology.

--- Summary ---

artificial intelligence ai is a wide-ranging branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence. ai can be applied across many different fields, including healthcare, finance, education, and transportation.

--- Another Example ---

Original Article:

    The Amazon rainforest, also known in English as Amazonia, is a moist broadleaf tropical rainforest in the Amazon biome that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometers (2,700,000 sq mi), of which 5,500,000 square kilometers (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil and Peru, followed by Colombia, Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana.

    The Amazon represents over half of the planet's remaining rainforests, and comprises the largest and most species-rich tract of tropical rainforest in the world.

--- Summary ---

the amazon rainforest also known in english as amazonia is a moist broadleaf tropical rainforest in the amazon biome that covers most of the amazon basin of south america.
```

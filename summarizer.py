import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def summarize_text(text, num_sentences=3):
    """
    Summarizes a given text using NLP techniques.

    Args:
        text (str): The input text to summarize.
        num_sentences (int, optional): The desired number of sentences in the summary. Defaults to 3.

    Returns:
        str: A concise summary of the input text.
    """
    try:
        # Tokenize the text into sentences
        sentences = sent_tokenize(text)
        if not sentences:
            return "Input text is empty."

        # Tokenize the words and remove stop words
        stop_words = set(stopwords.words('english'))
        word_frequencies = {}
        for sentence in sentences:
            words = word_tokenize(sentence.lower())
            for word in words:
                if word.isalnum() and word not in stop_words:
                    if word not in word_frequencies:
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1

        if not word_frequencies:
            return "No significant words found after removing stop words."

        # Calculate sentence scores based on word frequencies
        sentence_scores = {}
        for i, sentence in enumerate(sentences):
            for word in word_tokenize(sentence.lower()):
                if word in word_frequencies:
                    if i not in sentence_scores:
                        sentence_scores[i] = word_frequencies[word]
                    else:
                        sentence_scores[i] += word_frequencies[word]

        # Get the top N sentences with the highest scores
        ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
        top_n_sentences_indices = sorted(ranked_sentences[:num_sentences])

        # Create the summary by joining the top sentences in their original order
        summary_sentences = [sentences[i] for i in top_n_sentences_indices]
        summary = " ".join(summary_sentences)
        return summary

    except LookupError as e:
        print(f"Error: {e}. Please make sure you have the necessary NLTK data. "
              "You can download it by running:\n"
              ">>> import nltk\n"
              ">>> nltk.download('punkt')\n"
              ">>> nltk.download('stopwords')")
        return "An error occurred during summarization. Please check the console."

if __name__ == "__main__":
    # Example usage:
    long_article = """
    Artificial intelligence (AI) is a wide-ranging branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence. AI is an interdisciplinary science with multiple approaches, and advancements in machine learning and deep learning are creating a paradigm shift in virtually every sector of the tech industry.

    AI can be applied across many different fields, including healthcare, finance, education, and transportation. In healthcare, AI can assist with diagnosis and drug discovery. In finance, AI algorithms are used for fraud detection and algorithmic trading. Educational applications of AI include personalized learning platforms. Self-driving cars are a prominent example of AI in transportation.

    The development of AI raises several ethical considerations. Concerns about job displacement due to automation and the potential for bias in AI algorithms are actively being discussed. Ensuring fairness and transparency in AI systems is a crucial area of research and development.

    Despite these challenges, the potential benefits of AI are immense. From solving complex problems to improving efficiency and creating new opportunities, AI continues to be a rapidly evolving and transformative technology.
    """

    print("Original Article:\n")
    print(long_article)
    print("\n--- Summary ---\n")
    summary = summarize_text(long_article, num_sentences=2)
    print(summary)

    print("\n--- Another Example ---\n")
    another_article = """
    The Amazon rainforest, also known in English as Amazonia, is a moist broadleaf tropical rainforest in the Amazon biome that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometers (2,700,000 sq mi), of which 5,500,000 square kilometers (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil and Peru, followed by Colombia, Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana.

    The Amazon represents over half of the planet's remaining rainforests, and comprises the largest and most species-rich tract of tropical rainforest in the world.
    """
    print("Original Article:\n")
    print(another_article)
    print("\n--- Summary ---\n")
    another_summary = summarize_text(another_article, num_sentences=1)
    print(another_summary)
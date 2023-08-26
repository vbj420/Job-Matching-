import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords

# Download NLTK data (if not already downloaded)
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')

# Given job description
job_description = """
Requirements:
Bachelor's degree in Computer Science or related field.
Proven experience in software development using Python, JavaScript, and modern web frameworks.
Strong problem-solving skills and the ability to analyze and optimize code for performance.
Familiarity with version control systems, preferably Git.
Excellent communication and teamwork skills.
"""

# Tokenize and tag words
def extract_skills(job_description) :
    tokens = word_tokenize(job_description)
    tagged_tokens = pos_tag(tokens)    
    # Filter out stopwords and extract nouns
    stop_words = set(stopwords.words('english'))
    skills = set()
    for word, tag in tagged_tokens:
        if tag.startswith('NN') and word.lower() not in stop_words:
            skills.add(word.lower())
    return skills


#print("Extracted skills:", skills)

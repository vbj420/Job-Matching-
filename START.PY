from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extracted skills and job description keyword tokens
def match(required,profile) :
# Convert skills and job description tokens to lowercase
    extracted_skills  = required 
    job_description_tokens = profile
    extracted_skills_lower = [skill.lower() for skill in extracted_skills]
    job_description_tokens_lower = [token.lower() for token in job_description_tokens]
    
    # Create a count vectorizer and transform the data
    vectorizer = CountVectorizer().fit_transform(extracted_skills_lower + job_description_tokens_lower)
    vectorized_skills = vectorizer.toarray()
    
    # Calculate cosine similarity between skills and job description tokens
    cosine_similarities = cosine_similarity(vectorized_skills)
    
    # Determine matches based on cosine similarity
    skill_matches = {}
    for i, skill in enumerate(extracted_skills_lower):
        similarity_scores = cosine_similarities[i][len(extracted_skills_lower):]
        matched_indices = [index for index, score in enumerate(similarity_scores) if score > 0]
        matched_tokens = [job_description_tokens_lower[index] for index in matched_indices]
        skill_matches[skill] = matched_tokens
    
    '''
    # Display skill matches
    for skill, matched_tokens in skill_matches.items():
        print(f"Skill: {skill}")
        print(f"Matched Tokens: {matched_tokens}")
        print()
    '''
    total_similarity = sum(cosine_similarities[:len(extracted_skills_lower), len(extracted_skills_lower):])
    average_similarity = total_similarity / len(extracted_skills_lower)
    # Set a threshold for what you consider a "good" match
    threshold = 0.5
    # Print "yes" if the average similarity is above the threshold, else print "no"
    if average_similarity >= threshold:
        return "yes"
    else:
        return "no"
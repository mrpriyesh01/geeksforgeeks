#QUESTION=RANK ASSINGN TO STUDENT BASED ON SCORE VALUE

from operator import itemgetter

def rank_students(student_scores):
    # Step 1: Sort students by score (descending order)
    sorted_by_score = sorted(student_scores.items(), key=itemgetter(1), reverse=True)
    rank = 1  
    result = {}  
    prev_score = None  
    
    for i, (student, score) in enumerate(sorted_by_score):
        if score != prev_score:
            rank = i + 1  
        result[student] = rank  
        prev_score = score
    return result
student_scores = {
    'Raj': 92,
    'Riya': 92,
    'Sahil': 89,
    'Priya': 85,
    'Ankit': 78
}
ranked_students = rank_students(student_scores)
print(ranked_students)


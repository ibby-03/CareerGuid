import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tests.settings')
django.setup()

from core.models import AptitudeQuestion, AptitudeAnswer

def populate_aptitude_questions():
    questions = [
        # Section 1: Technical Skills
        {
<<<<<<< HEAD
            'question_text': 'Which programming languages are you familiar with?',
            'category': 'technical',
            'answers': [
                {'answer_text': 'None', 'score': 0},
                {'answer_text': 'One or two', 'score': 1},
                {'answer_text': 'Three to five', 'score': 3},
                {'answer_text': 'More than five', 'score': 5},
            ]
        },
        {
            'question_text': 'How do you rate your ability to troubleshoot and fix technical issues?',
            'category': 'technical',
            'answers': [
                {'answer_text': 'Poor', 'score': 0},
                {'answer_text': 'Fair', 'score': 1},
                {'answer_text': 'Good', 'score': 3},
                {'answer_text': 'Excellent', 'score': 5},
            ]
        },
        {
            'question_text': 'How comfortable are you with learning new software or tools?',
            'category': 'technical',
            'answers': [
                {'answer_text': 'Not comfortable', 'score': 0},
                {'answer_text': 'Slightly comfortable', 'score': 1},
                {'answer_text': 'Comfortable', 'score': 3},
                {'answer_text': 'Very comfortable', 'score': 5},
            ]
        },
        {
            'question_text': 'Do you have experience in managing databases or cloud services?',
            'category': 'technical',
            'answers': [
                {'answer_text': 'No experience', 'score': 0},
                {'answer_text': 'Some experience', 'score': 1},
                {'answer_text': 'Moderate experience', 'score': 3},
                {'answer_text': 'Extensive experience', 'score': 5},
=======
            'text': 'Which programming languages are you familiar with?',
            'category': 'technical',
            'answers': [
                {'text': 'None', 'score': 0},
                {'text': 'One or two', 'score': 1},
                {'text': 'Three to five', 'score': 3},
                {'text': 'More than five', 'score': 5},
            ]
        },
        {
            'text': 'How do you rate your ability to troubleshoot and fix technical issues?',
            'category': 'technical',
            'answers': [
                {'text': 'Poor', 'score': 0},
                {'text': 'Fair', 'score': 1},
                {'text': 'Good', 'score': 3},
                {'text': 'Excellent', 'score': 5},
            ]
        },
        {
            'text': 'How comfortable are you with learning new software or tools?',
            'category': 'technical',
            'answers': [
                {'text': 'Not comfortable', 'score': 0},
                {'text': 'Slightly comfortable', 'score': 1},
                {'text': 'Comfortable', 'score': 3},
                {'text': 'Very comfortable', 'score': 5},
            ]
        },
        {
            'text': 'Do you have experience in managing databases or cloud services?',
            'category': 'technical',
            'answers': [
                {'text': 'No experience', 'score': 0},
                {'text': 'Some experience', 'score': 1},
                {'text': 'Moderate experience', 'score': 3},
                {'text': 'Extensive experience', 'score': 5},
>>>>>>> 5c5a13cb11c281c8f75415d6aff0591a1535b8dc
            ]
        },
        # Section 2: Creative Skills
        {
<<<<<<< HEAD
            'question_text': 'How often do you engage in creative activities (e.g., drawing, writing, designing)?',
            'category': 'creative',
            'answers': [
                {'answer_text': 'Never', 'score': 0},
                {'answer_text': 'Rarely', 'score': 1},
                {'answer_text': 'Sometimes', 'score': 3},
                {'answer_text': 'Often', 'score': 5},
            ]
        },
        {
            'question_text': 'Do you enjoy brainstorming and generating new ideas?',
            'category': 'creative',
            'answers': [
                {'answer_text': 'Not at all', 'score': 0},
                {'answer_text': 'A little', 'score': 1},
                {'answer_text': 'Somewhat', 'score': 3},
                {'answer_text': 'Very much', 'score': 5},
            ]
        },
        {
            'question_text': 'How do you approach problem-solving in a creative manner?',
            'category': 'creative',
            'answers': [
                {'answer_text': 'I follow standard methods', 'score': 0},
                {'answer_text': 'I sometimes try new approaches', 'score': 1},
                {'answer_text': 'I often come up with creative solutions', 'score': 3},
                {'answer_text': 'I always seek innovative solutions', 'score': 5},
            ]
        },
        {
            'question_text': 'Have you ever worked on a project that required creative thinking?',
            'category': 'creative',
            'answers': [
                {'answer_text': 'No', 'score': 0},
                {'answer_text': 'Once or twice', 'score': 1},
                {'answer_text': 'Several times', 'score': 3},
                {'answer_text': 'Frequently', 'score': 5},
=======
            'text': 'How often do you engage in creative activities (e.g., drawing, writing, designing)?',
            'category': 'creative',
            'answers': [
                {'text': 'Never', 'score': 0},
                {'text': 'Rarely', 'score': 1},
                {'text': 'Sometimes', 'score': 3},
                {'text': 'Often', 'score': 5},
            ]
        },
        {
            'text': 'Do you enjoy brainstorming and generating new ideas?',
            'category': 'creative',
            'answers': [
                {'text': 'Not at all', 'score': 0},
                {'text': 'A little', 'score': 1},
                {'text': 'Somewhat', 'score': 3},
                {'text': 'Very much', 'score': 5},
            ]
        },
        {
            'text': 'How do you approach problem-solving in a creative manner?',
            'category': 'creative',
            'answers': [
                {'text': 'I follow standard methods', 'score': 0},
                {'text': 'I sometimes try new approaches', 'score': 1},
                {'text': 'I often come up with creative solutions', 'score': 3},
                {'text': 'I always seek innovative solutions', 'score': 5},
            ]
        },
        {
            'text': 'Have you ever worked on a project that required creative thinking?',
            'category': 'creative',
            'answers': [
                {'text': 'No', 'score': 0},
                {'text': 'Once or twice', 'score': 1},
                {'text': 'Several times', 'score': 3},
                {'text': 'Frequently', 'score': 5},
>>>>>>> 5c5a13cb11c281c8f75415d6aff0591a1535b8dc
            ]
        },
        # Section 3: Communication Skills
        {
<<<<<<< HEAD
            'question_text': 'How confident are you in public speaking?',
            'category': 'communication',
            'answers': [
                {'answer_text': 'Not confident at all', 'score': 0},
                {'answer_text': 'Slightly confident', 'score': 1},
                {'answer_text': 'Moderately confident', 'score': 3},
                {'answer_text': 'Very confident', 'score': 5},
            ]
        },
        {
            'question_text': 'Do you find it easy to convey your ideas clearly in writing?',
            'category': 'communication',
            'answers': [
                {'answer_text': 'Not at all', 'score': 0},
                {'answer_text': 'Sometimes', 'score': 1},
                {'answer_text': 'Often', 'score': 3},
                {'answer_text': 'Always', 'score': 5},
            ]
        },
        {
            'question_text': 'How do you rate your listening skills?',
            'category': 'communication',
            'answers': [
                {'answer_text': 'Poor', 'score': 0},
                {'answer_text': 'Fair', 'score': 1},
                {'answer_text': 'Good', 'score': 3},
                {'answer_text': 'Excellent', 'score': 5},
            ]
        },
        {
            'question_text': 'Do you feel comfortable communicating with people from diverse backgrounds?',
            'category': 'communication',
            'answers': [
                {'answer_text': 'Not comfortable', 'score': 0},
                {'answer_text': 'Slightly comfortable', 'score': 1},
                {'answer_text': 'Comfortable', 'score': 3},
                {'answer_text': 'Very comfortable', 'score': 5},
=======
            'text': 'How confident are you in public speaking?',
            'category': 'communication',
            'answers': [
                {'text': 'Not confident at all', 'score': 0},
                {'text': 'Slightly confident', 'score': 1},
                {'text': 'Moderately confident', 'score': 3},
                {'text': 'Very confident', 'score': 5},
            ]
        },
        {
            'text': 'Do you find it easy to convey your ideas clearly in writing?',
            'category': 'communication',
            'answers': [
                {'text': 'Not at all', 'score': 0},
                {'text': 'Sometimes', 'score': 1},
                {'text': 'Often', 'score': 3},
                {'text': 'Always', 'score': 5},
            ]
        },
        {
            'text': 'How do you rate your listening skills?',
            'category': 'communication',
            'answers': [
                {'text': 'Poor', 'score': 0},
                {'text': 'Fair', 'score': 1},
                {'text': 'Good', 'score': 3},
                {'text': 'Excellent', 'score': 5},
            ]
        },
        {
            'text': 'Do you feel comfortable communicating with people from diverse backgrounds?',
            'category': 'communication',
            'answers': [
                {'text': 'Not comfortable', 'score': 0},
                {'text': 'Slightly comfortable', 'score': 1},
                {'text': 'Comfortable', 'score': 3},
                {'text': 'Very comfortable', 'score': 5},
>>>>>>> 5c5a13cb11c281c8f75415d6aff0591a1535b8dc
            ]
        },
        # Section 4: Analytical Skills
        {
<<<<<<< HEAD
            'question_text': 'How often do you engage in activities that require analytical thinking (e.g., puzzles, games, problem-solving)?',
            'category': 'analytical',
            'answers': [
                {'answer_text': 'Never', 'score': 0},
                {'answer_text': 'Rarely', 'score': 1},
                {'answer_text': 'Sometimes', 'score': 3},
                {'answer_text': 'Often', 'score': 5},
            ]
        },
        {
            'question_text': 'How do you rate your ability to interpret data and statistics?',
            'category': 'analytical',
            'answers': [
                {'answer_text': 'Poor', 'score': 0},
                {'answer_text': 'Fair', 'score': 1},
                {'answer_text': 'Good', 'score': 3},
                {'answer_text': 'Excellent', 'score': 5},
            ]
        },
        {
            'question_text': 'Do you enjoy breaking down complex problems into smaller, manageable parts?',
            'category': 'analytical',
            'answers': [
                {'answer_text': 'Not at all', 'score': 0},
                {'answer_text': 'A little', 'score': 1},
                {'answer_text': 'Somewhat', 'score': 3},
                {'answer_text': 'Very much', 'score': 5},
            ]
        },
        {
            'question_text': 'Have you ever been involved in a project that required detailed analysis?',
            'category': 'analytical',
            'answers': [
                {'answer_text': 'No', 'score': 0},
                {'answer_text': 'Once or twice', 'score': 1},
                {'answer_text': 'Several times', 'score': 3},
                {'answer_text': 'Frequently', 'score': 5},
=======
            'text': 'How often do you engage in activities that require analytical thinking (e.g., puzzles, games, problem-solving)?',
            'category': 'analytical',
            'answers': [
                {'text': 'Never', 'score': 0},
                {'text': 'Rarely', 'score': 1},
                {'text': 'Sometimes', 'score': 3},
                {'text': 'Often', 'score': 5},
            ]
        },
        {
            'text': 'How do you rate your ability to interpret data and statistics?',
            'category': 'analytical',
            'answers': [
                {'text': 'Poor', 'score': 0},
                {'text': 'Fair', 'score': 1},
                {'text': 'Good', 'score': 3},
                {'text': 'Excellent', 'score': 5},
            ]
        },
        {
            'text': 'Do you enjoy breaking down complex problems into smaller, manageable parts?',
            'category': 'analytical',
            'answers': [
                {'text': 'Not at all', 'score': 0},
                {'text': 'A little', 'score': 1},
                {'text': 'Somewhat', 'score': 3},
                {'text': 'Very much', 'score': 5},
            ]
        },
        {
            'text': 'Have you ever been involved in a project that required detailed analysis?',
            'category': 'analytical',
            'answers': [
                {'text': 'No', 'score': 0},
                {'text': 'Once or twice', 'score': 1},
                {'text': 'Several times', 'score': 3},
                {'text': 'Frequently', 'score': 5},
>>>>>>> 5c5a13cb11c281c8f75415d6aff0591a1535b8dc
            ]
        },
        # Section 5: Social Skills
        {
<<<<<<< HEAD
            'question_text': 'How comfortable are you working in a team?',
            'category': 'social',
            'answers': [
                {'answer_text': 'Not comfortable', 'score': 0},
                {'answer_text': 'Slightly comfortable', 'score': 1},
                {'answer_text': 'Comfortable', 'score': 3},
                {'answer_text': 'Very comfortable', 'score': 5},
            ]
        },
        {
            'question_text': 'Do you find it easy to build relationships with new people?',
            'category': 'social',
            'answers': [
                {'answer_text': 'Not at all', 'score': 0},
                {'answer_text': 'A little', 'score': 1},
                {'answer_text': 'Somewhat', 'score': 3},
                {'answer_text': 'Very much', 'score': 5},
            ]
        },
        {
            'question_text': 'How do you handle conflicts in a group setting?',
            'category': 'social',
            'answers': [
                {'answer_text': 'Poorly', 'score': 0},
                {'answer_text': 'Fairly', 'score': 1},
                {'answer_text': 'Well', 'score': 3},
                {'answer_text': 'Very well', 'score': 5},
            ]
        },
        {
            'question_text': 'Have you ever taken a leadership role in a group project?',
            'category': 'social',
            'answers': [
                {'answer_text': 'No', 'score': 0},
                {'answer_text': 'Once or twice', 'score': 1},
                {'answer_text': 'Several times', 'score': 3},
                {'answer_text': 'Frequently', 'score': 5},
=======
            'text': 'How comfortable are you working in a team?',
            'category': 'social',
            'answers': [
                {'text': 'Not comfortable', 'score': 0},
                {'text': 'Slightly comfortable', 'score': 1},
                {'text': 'Comfortable', 'score': 3},
                {'text': 'Very comfortable', 'score': 5},
            ]
        },
        {
            'text': 'Do you find it easy to build relationships with new people?',
            'category': 'social',
            'answers': [
                {'text': 'Not at all', 'score': 0},
                {'text': 'A little', 'score': 1},
                {'text': 'Somewhat', 'score': 3},
                {'text': 'Very much', 'score': 5},
            ]
        },
        {
            'text': 'How do you handle conflicts in a group setting?',
            'category': 'social',
            'answers': [
                {'text': 'Poorly', 'score': 0},
                {'text': 'Fairly', 'score': 1},
                {'text': 'Well', 'score': 3},
                {'text': 'Very well', 'score': 5},
            ]
        },
        {
            'text': 'Have you ever taken a leadership role in a group project?',
            'category': 'social',
            'answers': [
                {'text': 'No', 'score': 0},
                {'text': 'Once or twice', 'score': 1},
                {'text': 'Several times', 'score': 3},
                {'text': 'Frequently', 'score': 5},
>>>>>>> 5c5a13cb11c281c8f75415d6aff0591a1535b8dc
            ]
        }
    ]

    for question_data in questions:
        question = AptitudeQuestion.objects.create(
<<<<<<< HEAD
            question_text=question_data['question_text'],
=======
            text=question_data['text'],
>>>>>>> 5c5a13cb11c281c8f75415d6aff0591a1535b8dc
            category=question_data['category']
        )
        for answer_data in question_data['answers']:
            AptitudeAnswer.objects.create(
                question=question,
<<<<<<< HEAD
                answer_text=answer_data['answer_text'],
=======
                text=answer_data['text'],
>>>>>>> 5c5a13cb11c281c8f75415d6aff0591a1535b8dc
                score=answer_data['score']
            )

if __name__ == '__main__':
    populate_aptitude_questions()
    print('Aptitude questions populated successfully.')

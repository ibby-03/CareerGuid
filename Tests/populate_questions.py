import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tests.settings')
django.setup()

from core.models import Question

questions = [
    ("I enjoy trying new foods and cuisines.", "O"),
    ("When traveling, I prefer to explore off-the-beaten-path destinations rather than visiting well-known tourist spots.", "O"),
    ("I am a very imaginative person.", "O"),
    ("I enjoy thinking about abstract concepts.", "O"),
    ("I am curious about many different things.", "O"),
    ("I am always on time for appointments.", "C"),
    ("When working on a project, I prefer to set clear deadlines and stick to them.", "C"),
    ("I am a very organized person.", "C"),
    ("I always follow through with my plans.", "C"),
    ("I pay attention to details.", "C"),
    ("I enjoy being the center of attention.", "E"),
    ("At a party, I prefer to meet new people rather than talk to a small group of friends.", "E"),
    ("I am a very energetic person.", "E"),
    ("I feel comfortable leading a group.", "E"),
    ("I am a very talkative person.", "E"),
    ("I am always willing to help others.", "A"),
    ("When someone is upset, I prefer to listen and offer emotional support rather than offering practical advice.", "A"),
    ("I am a very empathetic person.", "A"),
    ("I tend to trust people easily.", "A"),
    ("I am very considerate of other people's feelings.", "A"),
    ("I worry a lot about things.", "N"),
    ("When faced with a stressful situation, I tend to stay calm and collected.", "N"),
    ("I am a very emotionally stable person.", "N"),
    ("I often feel anxious about things.", "N"),
    ("I get upset easily.", "N"),
]

for text, category in questions:
    Question.objects.create(text=text, category=category)
<<<<<<< HEAD

print("Questions populated successfully!")
=======
>>>>>>> 5c5a13cb11c281c8f75415d6aff0591a1535b8dc

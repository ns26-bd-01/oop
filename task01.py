class Score:
    def __init__(self, ball, subject):
        self.ball = ball
        self.subject = subject

    def __str__(self) -> str:
        return f"Score(ball={self.ball}, subject='{self.subject}')"


class Student:
    def __init__(self, name: str):
        self.name = name
        self.scores: list[Score] = []

    def add_score(self, score: Score) -> None:
        self.scores.append(score)

    def get_avg_score(self) -> float:
        total = 0
        for score in self.scores:
            total += score.ball

        avg = round(total / len(self.scores), 2)

        return avg

    def get_max_score(self) -> Score | None:
        max_score = None
        if len(self.scores) > 0:
            max_score = self.scores[0]

        for score in self.scores:
            if score.ball > max_score.ball:
                max_score = score

        return max_score

    def __str__(self) -> str:
        return f"Student(name='{self.name}')"


student01 = Student("Ali")

student01.add_score(Score(75, "English"))
student01.add_score(Score(90, "Programming"))
student01.add_score(Score(80, "Math"))
student01.add_score(Score(70, "Phisics"))

print(student01.get_avg_score())
print(student01.get_max_score())

class Message:
    def __init__(self, text, label):
        self.text = text
        self.label = label  # 'spam' or 'ham'

class SpamClassifier:
    def __init__(self):
        self.spam_words = {}
        self.ham_words = {}
        self.spam_count = 0
        self.ham_count = 0

    def train(self, dataset):
        for msg in dataset:
            words = msg.text.lower().split()
            if msg.label == 'spam':
                self.spam_count += 1
                for w in words:
                    self.spam_words[w] = self.spam_words.get(w, 0) + 1
            else:
                self.ham_count += 1
                for w in words:
                    self.ham_words[w] = self.ham_words.get(w, 0) + 1

    def predict(self, text):
        words = text.lower().split()
        spam_score = sum(self.spam_words.get(w, 0) for w in words)
        ham_score = sum(self.ham_words.get(w, 0) for w in words)
        if spam_score > ham_score:
            return 'spam'
        else:
            return 'ham'


# ---------- MAIN ----------
dataset = [
    Message("Win a free phone now", "spam"),
    Message("Hey are we meeting today?", "ham"),
    Message("Congratulations you won a lottery", "spam"),
    Message("Can we talk tomorrow?", "ham"),
]

model = SpamClassifier()
model.train(dataset)

test_msg = "Hi"
print("Prediction:", model.predict(test_msg))



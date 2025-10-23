const quizData = [
    {
        question: 'What is the correct form of the verb in this sentence: She ___ to the store every Saturday.',
        a: 'go',
        b: 'goes',
        c: 'gone',
        d: 'going',
        correct: 'b',
    },
    {
        question: 'Which of the following is a proper noun?',
        a: 'city',
        b: 'happiness',
        c: 'London',
        d: 'dog',
        correct: 'c',
    },
    {
        question: 'Choose the correct sentence.',
        a: 'He don’t like ice cream.',
        b: 'He doesn’t likes ice cream.',
        c: 'He doesn’t like ice cream.',
        d: 'He not like ice cream.',
        correct: 'c',
    },
    {
        question: 'Which sentence is grammatically correct?',
        a: 'She go to school every day.',
        b: 'She goes to school every day.',
        c: 'She going to school every day.',
        d: 'She gone to school every day.',
        correct: 'b',
    },
];

const quiz = document.getElementById('quiz');
const submitButton = document.getElementById('submit');

function loadQuiz() {
    const currentQuizData = quizData[currentQuiz];
    questionEl.innerText = currentQuizData.question;
    answerEls.forEach((answerEl) => {
        answerEl.checked = false;
    });
    currentQuizData.a;
    answerEls[0].nextElementSibling.innerText = currentQuizData.a;
    answerEls[1].nextElementSibling.innerText = currentQuizData.b;
    answerEls[2].nextElementSibling.innerText = currentQuizData.c;
    answerEls[3].nextElementSibling.innerText = currentQuizData.d;
}

submitButton.addEventListener('click', () => {
    const answer = getSelected();
    if (answer) {
        if (answer === quizData[currentQuiz].correct) {
            score++;
        }
        currentQuiz++;
        if (currentQuiz < quizData.length) {
            loadQuiz();
        } else {
            quiz.innerHTML = `<h2>You scored ${score} out of ${quizData.length}</h2>`;
        }
    }
});
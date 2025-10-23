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
        question: 'Which of the following sentences is grammatically correct?',
        a: 'He don’t like pizza.',
        b: 'He doesn’t likes pizza.',
        c: 'He doesn’t like pizza.',
        d: 'He not like pizza.',
        correct: 'c',
    },
    {
        question: 'Choose the correct word: She is ___ than her brother.',
        a: 'more smart',
        b: 'smarter',
        c: 'most smart',
        d: 'smartest',
        correct: 'b',
    },
    {
        question: 'Identify the error in this sentence: Each of the players have a unique skill.',
        a: 'Each',
        b: 'of',
        c: 'have',
        d: 'unique',
        correct: 'c',
    }
];

let score = 0;

function submitQuiz() {
    const answers = [
        'b',
        'c',
        'b',
        'c'
    ];
    answers.forEach((answer, index) => {
        if (answer === quizData[index].correct) {
            score++;
        }
    });
    alert(`Your score is ${score} out of ${quizData.length}`);
}
const quizData = [
    {
        question: 'What is the correct form of the verb in the sentence: "She ___ to the store every Saturday."',
        a: 'go',
        b: 'goes',
        c: 'gone',
        d: 'going',
        correct: 'b'
    },
    {
        question: 'Which of the following is a correct sentence?',
        a: 'He go to school.',
        b: 'He goes to school.',
        c: 'He gone to school.',
        d: 'He going to school.',
        correct: 'b'
    },
    {
        question: 'Choose the correct past tense form: "They ___ a movie last night."',
        a: 'watch',
        b: 'watched',
        c: 'watches',
        d: 'watching',
        correct: 'b'
    },
    {
        question: 'Identify the error: "She don’t like apples."',
        a: 'She',
        b: 'don’t',
        c: 'like',
        d: 'apples',
        correct: 'b'
    }
];

let score = 0;

function submitQuiz() {
    const answers = [
        document.querySelector('input[name="question1"]:checked').value,
        document.querySelector('input[name="question2"]:checked').value,
        document.querySelector('input[name="question3"]:checked').value,
        document.querySelector('input[name="question4"]:checked').value
    ];

    answers.forEach((answer, index) => {
        if (answer === quizData[index].correct) {
            score++;
        }
    });

    alert(`Your score is ${score} out of ${quizData.length}`);
};
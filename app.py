const quizData = [
    {
        question: 'What is the plural of "child"?',
        a: 'Childs',
        b: 'Children',
        c: 'Childes',
        d: 'Childrens',
        correct: 'b',
    },
    {
        question: 'Which sentence is correct?',
        a: 'He go to school.',
        b: 'He goes to school.',
        c: 'He going to school.',
        d: 'He gone to school.',
        correct: 'b',
    },
    {
        question: 'What is the past tense of "run"?',
        a: 'Runned',
        b: 'Ran',
        c: 'Running',
        d: 'Runed',
        correct: 'b',
    },
    {
        question: 'Which of the following is a correct sentence?',
        a: 'She don’t like apples.',
        b: 'She doesn’t likes apples.',
        c: 'She doesn’t like apples.',
        d: 'She not like apples.',
        correct: 'c',
    }
];

const quiz = document.getElementById('quiz');
const submitButton = document.getElementById('submit');

let score = 0;

function loadQuiz() {
    quizData.forEach((data, index) => {
        const questionElement = document.createElement('div');
        questionElement.innerHTML = `<p>${data.question}</p>`;
        for (let option in data) {
            if (option !== 'question' && option !== 'correct') {
                questionElement.innerHTML += `<label><input type='radio' name='question${index}' value='${option}'> ${data[option]}</label><br>`;
            }
        }
        quiz.appendChild(questionElement);
    });
}

function calculateScore() {
    quizData.forEach((data, index) => {
        const answer = document.querySelector(`input[name='question${index}']:checked`);
        if (answer && answer.value === data.correct) {
            score++;
        }
    });
    alert(`You scored ${score} out of ${quizData.length}`);
}

submitButton.addEventListener('click', calculateScore);

loadQuiz();
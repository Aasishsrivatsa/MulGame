var points
var ip = window.location.origin;

document.addEventListener('DOMContentLoaded', function() {
    var selectedOption = null;
    var correctAnswer = null;


    function fetchQuestion() {
        fetch(ip+'/generate-question')
            .then(response => response.json())
            .then(data => {
                var question = data.question;
                var options = data.options;
                correctAnswer = data.answer;
                points = data.points;

                // Update the question
                document.getElementById('question').textContent = question;
                document.getElementById('points').textContent = 'Points : '+points;

                // Clear the options
                var optionsContainer = document.getElementById('options');
                optionsContainer.innerHTML = '';

                // Generate and append the options
                options.forEach(function(option) {
                    var button = document.createElement('button');
                    button.textContent = option;
                    button.addEventListener('click', function() {
                        if (selectedOption === null) {
                            selectedOption = option;
                            verifyAnswer(); // Verify the answer automatically
                        }
                    });
                    optionsContainer.appendChild(button);
                });
            })
            .catch(error => console.error(error));
    }

    function verifyAnswer() {
        if (selectedOption !== null) {
            // Verify the selected option
            var resultElement = document.getElementById('result');
            if (selectedOption == correctAnswer) {
                resultElement.textContent = 'Correct! +3';
                resultElement.style.color = 'green';
                fetch(ip+'/points-add')
                
            } else {
                resultElement.textContent = 'Incorrect. -1. The correct answer is: ' + correctAnswer;
                resultElement.style.color = 'red';
                fetch(ip+'/points-sub')
            }

            // Disable the buttons after verification
            var answerOptions = document.querySelectorAll('#options button');
            answerOptions.forEach(function(answerOption) {
                answerOption.disabled = true;
            });

            // Refresh the page after 1000ms (1 second)
            setTimeout(function() {
                location.reload();
            }, 1000);
        } else {
            alert('Please select an option first.');
        }
        var pointsElement = document.getElementById('points');
        pointsElement.textContent = 'Points: ' + points;
    }

    // Fetch the first question when the page loads
    fetchQuestion();
});

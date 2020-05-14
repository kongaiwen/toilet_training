
window.addEventListener("load", function(){
	
console.log("window is loaded")

// Main elements from DOM

var traineeAlias = document.getElementById("trainee_alias")
var traineeAge = document.getElementById("trainee_age")
var currentLevel = document.getElementById("current_level")
var currentVoids = document.getElementById("current_voids")
var currentAccidents = document.getElementById("current_accidents")

// Main buttons from DOM
var voidButton = document.getElementById("void")
var accidentButton = document.getElementById("accident")
var toiletTimerButton = document.getElementById("toilet_timer")
var offTimerButton = document.getElementById("off_timer")

// Trainer prompt Div elements
var basicPrompt = document.getElementById("basic_prompt")
var voidPrompt = document.getElementById("void_prompt")
var accidentPrompt = document.getElementById("accident_prompt")

// Trainer prompt childNodes

//  basicPrompt childNodes
var promptLevel = document.getElementById("level")
var promptSitDuration = document.getElementById("sit_duration")
var promptSitFrequency = document.getElementById("sit_frequency")
var levelUpText = document.getElementById("level_up")
var levelDownIntroText = document.getElementById("level_down_intro")
var levelDownText = document.getElementById("level_down")

// Countdown elements


var countdownTimer = document.getElementById("countdown")
var	currentDate = new Date()
var endDate = addMinutes(currentDate, 300);
var interv;



// state variables

var toiletTimerIsOn = false
var offTimerIsOn = false





// Event listeners for buttons
voidButton.addEventListener("click", updateVoids );
accidentButton.addEventListener("click", updateAccidents);
toiletTimerButton.addEventListener("click", manageTimer);




function updateVoids () {
	
	var voidNum = parseInt(currentVoids.innerHTML, 10)
	voidNum += 1 
	currentVoids.innerHTML = voidNum
	currentAccidents.innerHTML = 0
	
	basicPrompt.style.display = "none"
	accidentPrompt.style.display = "none"
	voidPrompt.style.display = "block"
	updateLevel()

}

function updateAccidents () {
	var accNum = parseInt(currentAccidents.innerHTML, 10)
	accNum += 1
	currentAccidents.innerHTML = accNum
	currentVoids.innerHTML = 0
	
	basicPrompt.style.display = "none"
	voidPrompt.style.display = "none"
	accidentPrompt.style.display = "block"
	updateLevel()

}

function updateLevel () {
	if (currentVoids.innerHTML == 3) {
		var level = parseInt(currentLevel.innerHTML, 10) + 1
		currentLevel.innerHTML = level
		currentVoids.innerHTML = 0
		currentAccidents.innerHTML = 0
		accidentPrompt.style.display = "none"
		voidPrompt.style.display = "none"
		levelDownIntroText.style.display = "none"
		levelDownText.style.display = "none"
		basicPrompt.style.display = "block"
		levelUpText.style.display = "block"
		promptLevel.innerHTML = currentLevel.innerHTML


	} else if (currentAccidents.innerHTML == 3 && currentLevel.innerHTML != 1) {
		var level = parseInt(currentLevel.innerHTML, 10) - 1
		currentLevel.innerHTML = level 
		currentVoids.innerHTML = 0
		currentAccidents.innerHTML = 0
		accidentPrompt.style.display = "none"
		voidPrompt.style.display = "none"
		levelUpText.style.display = "none"
		basicPrompt.style.display = "block"
		levelDownIntroText.style.display = "inline"
		levelDownText.style.display = "inline"
		promptLevel.innerHTML = currentLevel.innerHTML
	} else {return}
}



// function togglePrompt(node) {
  
//   if (node.style.display === "none") {
//     node.style.display = "block";
//   } else {
//     node.style.display = "none";
//   }
// };


var timeTable = {
	1 : [10, 5],
	2 : [10, 10],
	3 : [5, 15],
	4 : [5, 25],
	5 : [5, 35],
	6 : [5, 45],
	7 : [5, 60, 30],
	8 : [5, 90, 45],
	9 : [5, 120, 60],
	10 : [5, 150, 75],
	11 : [5, 180, 90],
	12 : [5, 240, 120]
};




function addMinutes(date, minutes) {
    return new Date(date.getTime() + minutes*60000);
}


function setTimer() {
	
	currentDate = new Date()
	var difference = endDate.getTime() - currentDate.getTime();

	if (difference > 0) {
		var parts = {
		  "hours": Math.floor((difference / (1000 * 60 * 60)) % 24),
		  "minutes": Math.floor((difference / 1000 / 60) % 60),
		  "seconds": Math.floor((difference / 1000) % 60),
		} 
	var remaining = `${parts["hours"]} : ${parts["minutes"]} : ${parts["seconds"]}`
	countdownTimer.innerHTML = remaining;
	} else {
		console.log(difference)
		clearInterval(interv)
		endDate = addMinutes(currentDate, 300)
							};

}

function manageTimer() {
	if (toiletTimerIsOn == true){
		toiletTimerIsOn = false
		clearInterval(interv)
		countdownTimer.innerHTML = ''
		toiletTimerButton.innerHTML = "Start Toilet Timer"
	} else {

	var minutes = timeTable[parseInt(currentLevel.innerHTML, 10)][0];
	// var minutes = 5
	currentDate = new Date()
	endDate = addMinutes(currentDate, minutes);
	toiletTimerIsOn = true
	console.log(toiletTimerIsOn)

	setTimer();
	toiletTimerButton.innerHTML = "Stop Toilet Timer"
	interv = setInterval(setTimer, 1000)

}
}

})




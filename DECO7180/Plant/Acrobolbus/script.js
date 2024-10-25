const slider = document.querySelector(".slider");
const handle = document.querySelector(".handle");
/* access the slider */

const minValue = 0;
const maxValue = slider.clientWidth - handle.clientWidth;
/* set the handle area */

let isDragging = false;

handle.addEventListener("mousedown", () => {
  isDragging = true;
  slider.classList.add("dragging");
}); /* when user starts to hold the mouse */

document.addEventListener("mousemove", (e) => {
  if (!isDragging) return;

  let newPosition =
    e.clientX - slider.getBoundingClientRect().left - handle.clientWidth;
  /* let handle position follow the mouse movement */

  if (newPosition < minValue) {
    newPosition = minValue;
  }
  if (newPosition > maxValue) {
    newPosition = maxValue;
  } /* make sure the handle cannot go beyond the slider */

  handle.style.left = newPosition + "px";
  document.querySelector(".slider_dragged").style.width =
    newPosition + 10 + "px";

  const stagePictures = document.querySelectorAll(".stage_picture");
  /* obtain all pictures */
  const stageWidth = 617 / 6;
  /* slider width is 617px, means every stage has 160px in slider */
  const currentStage = Math.floor(newPosition / stageWidth);
  /* determine which stage should be shown */

  stagePictures.forEach((picture) => {
    const index = parseInt(picture.getAttribute("index"));
    /* gain "index" attribute of every picture*/
    if (index === currentStage) {
      picture.style.zIndex = 1;
    } else {
      picture.style.zIndex = 0;
    }

    var infoContent = document.querySelector(".info_content");

    if (currentStage === 0 || currentStage === 1) {
      infoContent.textContent = "Germination";
    } else if (currentStage === 2 || currentStage === 3) {
      infoContent.textContent = "Seedling";
    } else if (currentStage === 4 || currentStage === 5) {
      infoContent.textContent = "Adult Plant";
    }
  });
});

document.addEventListener("mouseup", () => {
  isDragging = false;
  slider.classList.remove("dragging");
}); /* when user releases the mouse */

/* For interaction */

const covers = document.querySelectorAll('.cover');

covers.forEach(cover => {
  cover.addEventListener('click', function () {
    if (cover.classList.contains('clicked')) {
      cover.classList.remove('clicked');
    } else {
      cover.classList.add('clicked');
    }
  });
});


const nativeButton = document.getElementById('nativeButton');
const exoticButton = document.getElementById('exoticButton');

exoticButton.addEventListener('click', function () {
  exoticButton.style.backgroundColor = '#ff5555';

  setTimeout(function () {
    exoticButton.style.backgroundColor = '';
  }, 300);
});

nativeButton.addEventListener('click', function () {
  nativeButton.style.backgroundColor = '#96df6d';
});

// access what to speak and the play button.
var textToSpeak1 = document.querySelector(".plants_name").textContent;
var speakButton1 = document.getElementById("speakButton");

// add event listener to play button.
speakButton1.addEventListener("click", function () {
  // use SpeechSynthesis API to read the text.
  var speech = new SpeechSynthesisUtterance(textToSpeak1);
  speech.lang = "en-US";
  window.speechSynthesis.speak(speech);
});

// drag and drop section
const draggableElements = document.querySelectorAll(".draggable");
let confettiTriggered = false;

// drag and drop interaction
draggableElements.forEach(draggableElement => {
  draggableElement.addEventListener("dragstart", e => {
    e.dataTransfer.setData("text/plain", draggableElement.id);
  });
});

const droppableElements = document.querySelectorAll(".droppable");
let successfulDrops = 0;
let blinkTimeout;

droppableElements.forEach(droppable => {
  // when draggable element is dropped onto the droppable section
  droppable.addEventListener("dragover", e => {
    e.preventDefault();
    droppable.classList.add("droppable-hover");
  });

  // when draggable element is over the droppable sections
  droppable.addEventListener("drop", e => {
    e.preventDefault();
    const droppedElementID = e.dataTransfer.getData("text/plain");
    const droppedElement = document.getElementById(droppedElementID);

    const droppableID = droppable.getAttribute("data-droppable-id");

    // check if draggable element is over the matched droppable section
    if (droppedElement.getAttribute("data-droppable-id") === droppableID) {
      droppable.appendChild(droppedElement);
      droppable.style.border = "none";
      droppable.style.padding = "0";
      droppedElement.style.backgroundColor = "#DCECBB";
      successfulDrops++; //add on successful drop

    } else {
      //change color to indicate the incorrect position
      droppable.style.backgroundColor = "#ff5555";
      droppable.style.transition = "background-color 0.5s ease-out";

      clearTimeout(blinkTimeout);

      blinkTimeout = setTimeout(() => {
        droppable.style.backgroundColor = "";
      }, 500); // remove color
    }

    droppable.classList.remove("droppable-hover");

    //congrat when success
    if (successfulDrops === draggableElements.length) {
      triggerConfetti();
      confettiTriggered = true;
    }
  });

  // when draggable element is remove from the droppable section and not be dropped
  droppable.addEventListener("dragleave", () => {
    droppable.classList.remove("droppable-hover");
  });
});

function triggerConfetti() {
  const confettiContainer = document.getElementById("confetti-container");

  for (let i = 0; i < 200; i++) {
    const confettiPiece = document.createElement("div");
    confettiPiece.className = "confetti";
    confettiPiece.style.backgroundColor = getRandomColor();
    confettiPiece.style.left = `${Math.random() * 100}%`;
    confettiPiece.style.animationDuration = `${Math.random() * 2 + 1}s`;
    confettiPiece.style.animationDelay = `${Math.random() * 2}s`;
    confettiContainer.appendChild(confettiPiece);

    setTimeout(() => {
      confettiContainer.removeChild(confettiPiece);
    }, 4000);

  }
}

function getRandomColor() {
  const colors = ["#F7DDA4", "#DB6D9C", "#E0B4C8", "#D5C3F4", "#6BD3E6", "#C1F185"];
  return colors[Math.floor(Math.random() * colors.length)];
}


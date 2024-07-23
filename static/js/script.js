window.addEventListener("DOMContentLoaded", function (event) {
  let currentPathName = event.target.location.pathname;

  if (currentPathName === "/") {
    document.getElementById("index").classList.add("active");
  } else if (currentPathName === "/delete") {
    document.getElementById("delete").classList.add("active");
  } else {
    document.getElementById("edit").classList.add("active");
  }

  let todoInput = document.querySelector("#item-input");

  todoInput.addEventListener("input", function (e) {
    let userInput = e.target.value;
    let maxCharReached = document.querySelector(".max-char-reached");
    let maximum_characters;

    if (userInput.length > 50) {
      maximum_characters = userInput.substring(0, 51);
      e.target.value = maximum_characters;

      maxCharReached.style.display = "inline-block";
    } else {
      maxCharReached.style.display = "none";
    }
  });

  let items = document.querySelectorAll(".dropdown-item");
  let idInput = document.querySelector(".id-input");
  let dropdownToggle = document.querySelector(".dropdown-toggle");

  items.forEach(function(item) {
    item.addEventListener("click", function(event) {
      idInput.value = event.target.getAttribute("id");
      dropdownToggle.innerHTML = event.target.innerHTML;
    });
  });

  let flashMessageContainer = document.querySelector(".flash-message-container");

  if(flashMessageContainer) {
    this.setTimeout(function() {
      flashMessageContainer.style.display = "none";
    }, 3000);
  }
});
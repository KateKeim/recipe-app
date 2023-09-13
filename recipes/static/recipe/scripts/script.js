// JavaScript code to search recipes on the search box, main template
function search_recipe() {
    let input = document.getElementById('searchbar').value
    input = input.toLowerCase();                                                 //store user search value in 'input' variable as lowercase
    let recipes = document.getElementsByClassName('recipe_searched');          //store list of recipes on database on variable 'recipes'
  
    let recipe_box = document.getElementsByClassName('search_results');
    recipe_box[0].style.display = "block";
  
    for (i = 0; i < recipes.length; i++) {
      if (!recipes[i].innerHTML.toLowerCase().includes(input)) {             //loop through recipes to display recipes matched with user search input
        recipes[i].style.display = "none";
      }
      else {
        recipes[i].style.display = "block";
      }
    }
    if (input == "") {
      recipe_box[0].style.display = "none";
    }
  }

  // Add an event listener for input in the search bar
document.getElementById('searchbar').addEventListener('input', function (e) {
    filterRecipes();
});

// Add an event listener for Enter key press
document.getElementById('searchbar').addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
        e.preventDefault(); // Prevent the form from submitting
        goToSelectedRecipe();
    }
});

  function filterRecipes() {
    let input = document.getElementById('searchbar').value.trim().toLowerCase();
    let recipes = document.getElementsByClassName('recipe_searched');
    let recipe_box = document.querySelector('.search_results');
    let noMatch = true;

    for (let i = 0; i < recipes.length; i++) {
        let recipeName = recipes[i].querySelector('.recipe_name');
        if (!recipeName.innerText.toLowerCase().includes(input)) {
            recipes[i].style.display = "none";
        } else {
            recipes[i].style.display = "block";
            noMatch = false; // Set to false if at least one recipe matches
        }
    }

    if (noMatch || input === "") {
        recipe_box.style.display = "none";
    } else {
        recipe_box.style.display = "block";
    }
}

function goToSelectedRecipe() {
    let input = document.getElementById('searchbar').value.trim().toLowerCase();
    let recipes = document.getElementsByClassName('recipe_searched');

    for (let i = 0; i < recipes.length; i++) {
        let recipeName = recipes[i].querySelector('.recipe_name');
        if (recipeName.innerText.toLowerCase() === input) {
            window.location.href = recipeName.getAttribute('href');
            return;
        }
    }
}
/*
const tabcontents = document.getElementsByClassName('tab-content')

function opentab(arg) {
    for (let tabcontent of tabcontents) {
        tabcontent.classList.remove('active-tab')
    }
    document.getElementById(arg).classList.add('active-tab')

}
*/
// const tabcontents = document.getElementsByClassName('tab-content');
// const tabLinks = document.querySelectorAll('.tab-links'); // Select all tab links

// function opentab(arg) {
//     // Remove the active-tab class from all tab contents
//     for (let tabcontent of tabcontents) {
//         tabcontent.classList.remove('active-tab');
//     }

//     // Add the active-tab class to the clicked tab content
//     document.getElementById(arg).classList.add('active-tab');

//     // Remove the background color from all tab links
//     tabLinks.forEach(link => {
//         link.style.backgroundColor = ''; // Remove background color from all tabs
//         link.style.color = ''; // Reset text color if changed
//     });

//     // Now, find the active tab link and set its background color to red
//     const activeTabLink = document.querySelector(`.tab-links[onclick="opentab('${arg}')"]`);
//     activeTabLink.style.backgroundColor = 'red'; // Set background color to red
//     activeTabLink.style.color = 'white'; // Optional: Change text color to white
// }

// // Initially, set the background color for the 'buff' tab when the page loads
// document.addEventListener('DOMContentLoaded', function () {
//     opentab('buf'); // Activate the Buff tab by default when the page loads
// });




//====== for countrycode =====
const input = document.querySelector("#phone");
const ho = window.intlTelInput(input, {
    initialCountry: "np",
    strictMode: true,
    loadUtils: () => import("https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/25.2.1/build/js/utils.js") // for formatting/placeholders etc
});

document.getElementById('contactForm').addEventListener('submit', function (e) {
    if (ho.isValidNumber()) {
        input.value = ho.getNumber(); //full number
    }
    else {
        e.preventDefault();
    }

})
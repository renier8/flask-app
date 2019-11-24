let day = document.getElementById('day');
let month = document.getElementById('month');
let year = document.getElementById('year');
let footerDivs = document.querySelectorAll('.content-length');
let footerInputs = document.querySelectorAll('.footer-input');
let para = document.querySelectorAll('.footer-para');

let leapYear;

/* Function to update calender so days are same as number of days is month and leapyear gets 29 days in Feb */

function updateCalender() {
    if (year.value%4 === 0) {
        leapYear = 29;
    } else {
        leapYear = 28;
    }
    for (let i = 0; i < day.options.length; i++) {
        let value = day.options[i].value;
        day.options[i].removeAttribute("disabled");
        if (month.value === 'February' && value > leapYear) {
            day.options[i].setAttribute("disabled", "disabled");
        } else if ((month.value === 'April' || month.value === 'June' || month.value === 'September' || month.value === 'November') && value > 30) {
            day.options[i].setAttribute("disabled", "disabled");
        } 
    }
}

if (day) {
    day.addEventListener('click', updateCalender);
}
if (month) {
    month.addEventListener('click', updateCalender);
}
if (year) {
    year.addEventListener('click', updateCalender);
}


/* function that updates the paragraph below input fields to show number of characters left*/
function updatePara() {
    for (let j = 0; j < footerDivs.length; j++) {
        para[j].textContent = footerInputs[j].value.length + '/' + footerInputs[j].maxLength;
    }
}

for (let i = 0; i < footerInputs.length; i++) {
    footerInputs[i].addEventListener('input', updatePara);
    para[i].textContent = footerInputs[i].value.length + '/' + footerInputs[i].maxLength;
  }
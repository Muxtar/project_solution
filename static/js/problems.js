let problemsDiv = document.getElementsByClassName('problems')[0];

let problemsJs = [
    {
        id: 1,
        title: 'En boyuk reqemin sayi',
        result: true,
        difficulty: 'Hard',
        problemNumber: 1
    },
    {
        id: 2,
        title: 'List en kicik reqem',
        result: false,
        difficulty: 'Hard',
        problemNumber: 2
    },
    {
        id: 3,
        title: 'Sagdan birinci reqem',
        result: true,
        difficulty: 'Medium',
        problemNumber: 3
    }
]

for(i in problemsJs){
    if((Number(i)+1)%2 == 0){
        problem = `
            <div class="problem even">
                <div class="problem-name"><a href="problem.html">${problemsJs[i].title}</a></div>
                <div class="solution"><i class="fa fa-question-circle" aria-hidden="true"></i></div>
              
                <div class="difficulty" id="${problemsJs[i].difficulty.toLowerCase()}">${problemsJs[i].difficulty}</div>
                <div>${problemsJs[i].problemNumber}</div>
            </div>`
    }
    else{    
        problem = `
            <div class="problem odd">
                <div class="problem-name"><a href="problem.html">${problemsJs[i].title}</a></div>
                <div class="solution"><i class="fa fa-exclamation-triangle red" aria-hidden="true"></i></div>
                <div class="difficulty" id="${problemsJs[i].difficulty.toLowerCase()}">${problemsJs[i].difficulty}</div>
                <div>${problemsJs[i].problemNumber}</div>
            </div>`
    }
    problemsDiv.insertAdjacentHTML('beforeend', problem);
}
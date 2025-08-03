let CurrentNum = 1
let PerMove = 3

let FirstBtn = document.getElementById('slide1')
let SecondBtn = document.getElementById('slide2')
let ThirdBtn = document.getElementById('slide3')

let Blocks = document.querySelectorAll('.slide')

function HideAllGames() {
    Blocks.forEach(function (element) { 
        element.style.display = 'none'
    })
}

HideAllGames()

function NewSort(NewNum) {
    HideAllGames()

    CurrentNum = NewNum
    
    let SortedBlocks=Array.from(Blocks).slice(CurrentNum*PerMove-PerMove,CurrentNum*PerMove)
    
    SortedBlocks.forEach( function (element) { 
        element.style.display = 'block'
    })
}

NewSort(1)

FirstBtn.addEventListener('change', function () {NewSort(1)})
SecondBtn.addEventListener('change', function () {NewSort(2)})
ThirdBtn.addEventListener('change', function () {NewSort(3)})
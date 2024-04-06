function updateGame (el){
    game_id = el.value
    fetch('/ready/' + game_id, {
        method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'ready': el.checked})
    })
}

function createGame(){
    console.log('Create')
    let played = document.getElementById('played').value
    let release = document.getElementById('release').value

    fetch('/play', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'played': played || 'Пустое', 'release': release || '12.12.24', 'ready': false})
    })

}
// для выставления сегодняшней даты
window.onload = ( () => {
    document.getElementById('release').valueAsDate = new Date()
})
//window.confirm("Now Javascript works");



var modal = document.getElementById('myModal');
// Get the button that opens the modal
var btn = document.getElementById("myBtn3");

var edit_open = document.getElementsByClassName("fa-edit");





// When the user clicks on <span> (x), close the modal
// span.onclick = function () {
//     modal.style.display = "none";
// }

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function displayEditModal() {

    // Get the modal
    var modal = document.getElementById('myModal');
    //display ,modal
    modal.style.display = "block";

}

function hideEditModal() {
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];
    var modal = document.getElementById('myModal');
    // hide modal
    modal.style.display = "none";
}
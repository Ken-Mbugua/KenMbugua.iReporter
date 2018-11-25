//window.confirm("Now Javascript works");

// When the user clicks on <span> (x), close the modal
// span.onclick = function () {
//     modal.style.display = "none";
// }

// When the user clicks anywhere outside of the modal, close it


function resolvedCaseToGreen() {

    $("select.report_case").change(function () {
        var selectedStatus = $(this).children("option:selected").val();

        // resolved cases
        if (selectedStatus = 1) {
            // alert(selectedStatus);
            // $("tr:hover").css({"background-color": "#b9e5b9", "color": "black"});
            // $("tr:hover").css({"background-color": "#fc8f8f", "color": "black", "border-bottom": "1px solid #f4f4f4 "});
            alert(selectedStatus);
            $(this).parents('.options')
                .removeClass('rejectedCase')
                .addClass('resolvedCase');

        }
        // rejected cases
        else if (selectedStatus = 0) {
            alert(selectedStatus);
            $("tr:hover").css({
                "background-color": "red",
                "color": "black"
            });
        } else {
            alert(selectedStatus);
            $("tr:hover").css({
                "background-color": "white",
                "color": "black"
            });
        }
    });

}

function displayEditModal() {

    $('i.fa-edit').click(function(){
        $('#editCaseModal').css("display","block");
    });

}

function displayDeleteMsgModal() {
    $('i.fa-trash').click(function(){
        // alert("Delete MAssage");
        $('#deleteCaseModal').css("display","block");
    });
}

function hideModal() {

    // Get the <span> element that closes the modal
    $('span.close').click(function(){
        $('#editCaseModal').css("display","none");
        $('#deleteCaseModal').css("display","none");
    });

}

function modalCancelBtn() {
    $(".cancel-btn").click(function(){
        $('#editCaseModal').css("display","none");
        $('#deleteCaseModal').css("display","none");
    });
}

function dismisModalOutSideClick(){

    
}

$(document).ready(function (e) {
    
    if ($(e.target).is('#editCaseModal, #deleteCaseModal')) {
        $('#editCaseModal, #deleteCaseModal').fadeOut(500);
    }
    // alert("Javascript is working!!");
    resolvedCaseToGreen();
    displayEditModal();
    displayDeleteMsgModal();
    hideModal();
    modalCancelBtn();
});
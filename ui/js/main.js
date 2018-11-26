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
        if (selectedStatus == 1) {
            $(this).parents('tr')
                .removeClass('draftCase, rejectedCase, underInvCase')
                .addClass('resolvedCase');
        }
        // rejected cases
        else if (selectedStatus == 0) {
            
            $(this).parents('tr')
            .removeClass('resolvedCase, draftCase, underInvCase')
            .addClass('rejectedCase');
        }
         // unresolved cases
        else if (selectedStatus == 2) {
        
            $(this).parents('tr')
            .removeClass('resolvedCase, rejectedCase, underInvCase')
            .addClass('draftCase');
        }

        else if (selectedStatus == 3) {
            
            $(this).parents('tr')
            .removeClass('resolvedCase, rejectedCase, draftCase')
            .addClass('underInvCase');
        }
    });

}

function displayEditModal() {

    $('i.fa-edit').click(function () {
        $('#editCaseModal').css("display", "block");
    });

}

function displayDeleteMsgModal() {
    $('i.fa-trash').click(function () {
        // alert("Delete MAssage");
        $('#deleteCaseModal').css("display", "block");
    });
}

function hideModal() {

    // Get the <span> element that closes the modal
    $('span.close').click(function () {
        $('#editCaseModal').css("display", "none");
        $('#deleteCaseModal').css("display", "none");
    });

}

function modalCancelBtn() {
    $(".cancel-btn").click(function () {
        $('#editCaseModal').css("display", "none");
        $('#deleteCaseModal').css("display", "none");
    });
}

function dismisModalOutSideClick() {

}

$(document).ready(function (event) {

    // if ($(e.target).is('#editCaseModal, #deleteCaseModal')) {
    //     $('#editCaseModal, #deleteCaseModal').fadeOut(500);
    // }

    if (!$(event.target).closest(".modal").length) {
        // $("body").find(".modal").removeClass("visible");
        $('#editCaseModal, #deleteCaseModal').fadeOut(500);
    }

    // alert("Javascript is working!!");
    resolvedCaseToGreen();
    displayEditModal();
    displayDeleteMsgModal();
    hideModal();
    modalCancelBtn();
});
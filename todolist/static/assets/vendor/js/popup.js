
// Get the modal
var modal = document.getElementById("myModal");
// Get the button that opens the modal
var btn = document.getElementById("myBtn");
// Get the  element that closes the modal
var span = document.getElementsByClassName("close")[0];
// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
  modal.style.marginLeft="25%"
  modal.style.marginTop="10%"
 
}
// When the user clicks on  (x), close the modal

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

function hide(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

function openEditModal(taskId, taskTitle, taskDescription, taskStatus) {
  console.log("openEditModal called with", taskId, taskTitle, taskDescription, taskStatus);
  var titleElem = document.getElementById('title');
  var descriptionElem = document.getElementById('description');
  var statusElem = document.getElementById('status');
  var editUrl = document.getElementById('edit-task-url').getAttribute('data-url');

  if (titleElem && descriptionElem && statusElem) {
    titleElem.value = taskTitle;
    descriptionElem.value = taskDescription;
    statusElem.value = taskStatus;
    document.getElementById('taskForm').action = editUrl.replace('0', taskId); // Update form action URL
    var myModal = new bootstrap.Modal(document.getElementById('basicModal'));
    myModal.show();
  } else {
    console.error("One or more elements are not found in the DOM.");
  }
}


  function opentrt() {
    // console.log("openEditModal called with", taskId, taskTitle, taskDescription, taskStatus);
    // // var taskIdElem = document.getElementById('task_id');
    // var titleElem = document.getElementById('title');
    // var descriptionElem = document.getElementById('description');
    // var statusElem = document.getElementById('status');
    
    // if (taskIdElem && titleElem && descriptionElem && statusElem) {
    //     // taskIdElem.value = taskId;
    //     titleElem.value = taskTitle;
    //     descriptionElem.value = taskDescription;
    //     statusElem.value = taskStatus;
    //     document.getElementById('taskForm').action = "{% url 'edit_task' 0 %}".replace('0', taskId); // Update form action URL
        var myModal = new bootstrap.Modal(document.getElementById('basicModal'));
        myModal.show();
    // } else {
    //     console.error("One or more elements are not found in the DOM.");
    // }
}


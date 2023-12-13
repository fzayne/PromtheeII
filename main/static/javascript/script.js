function opencsv() {
  console.log("hello");
  // document.getElementById("upload-photo").onchange = function () {
  document.getElementById("openForm").submit();
  // };
}

function getMatdimension() {
  var n = prompt("enter number of rows");
  var m = prompt("enter number of columns");
  console.log(n, m);
  createMatrix(n, m);
}
function createMatrix(n, m) {
  table = document.getElementById("newMatrix");

  for (let i = 0; i < n; i++) {
    tr = document.createAttribute("tr");
    for (let j = 0; j < m; j++) {
      td = document.createAttribute("td");
      var input = document.createAttribute("input");
      input.type = "text";
      td.appendChild(input);
      tr.appendChild(td);
    }
    table.appendChild(tr);
  }
}
function getMatrix() {
  var matrix = [];

  element = document.getElementsByClassName("inputMat");
  var data = [];
  for (let i = 0; i < element.length; i++) data.push(element[i].value);
  console.log(data);
  for (let i = 0; i < data.length; i += 8) {
    matrix.push(data.slice(i, i + 8));
  }
  console.log(matrix);
  // fetch("/sendMatrix", {
  //   method: "POST",
  //   headers: {
  //     "Content-Type": "application/json",
  //   },
  //   body: JSON.stringify({ matrix: matrix }),
  // })
  //   .then((response) => response.json())
  //   .then((data) => {
  //     console.log("Success:", data);
  //     // Optionally update the UI or perform other actions on success
  //   })
  //   .catch((error) => {
  //     console.error("Error:", error);
  //   });

  $.ajax({
    type: "POST",
    url: "/sendMatrix",
    contentType: "application/json;charset=UTF-8",
    data: JSON.stringify(matrix),
    dataType: "json",
    success: function (response) {
      window.location.href = "http://127.0.0.1:5000/sendMatrix";
      console.log(response);
    },
    error: function (err) {
      console.log(err);
    },
  });
}

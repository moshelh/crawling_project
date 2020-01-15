
//open txt file 
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function(){
    if(xmlhttp.status == 200 && xmlhttp.readyState == 4){
        txt = xmlhttp.responseText;

        var splitted = txt.split(/\n\s*\n/);
        splitted.forEach((capture, i) => {
            item = capture.match(/[^\r\n]+/g);
            addRow('table', item, i);
        });
    }
};
xmlhttp.open("GET","crawling.txt",true);
xmlhttp.send();

function addRow(tableID, item, i) {
    // Get a reference to the table
    let tableRef = document.getElementById(tableID);

    // Insert a row at the end of the table
    let newRow = tableRef.insertRow(-1);

    // Insert a cell in the row at index 0
    let indexCell = newRow.insertCell(0);
    let newText = document.createTextNode(i);
    indexCell.appendChild(newText);

    for (let i = 0; i < item.length; i++) {

        // Image index
        if (i === 3) {
            const imageCell = newRow.insertCell(i + 1);
            const image = new Image();
            image.src = item[i];
            image.classList.add("image");
            imageCell.appendChild(image);
        } else {
            const valueCell = newRow.insertCell(i + 1);
            let newText = document.createTextNode(item[i]);
            valueCell.appendChild(newText);
        }
    }
}

document.addEventListener("DOMContentLoaded", function() {
    let data = [
        {name: "thuyen1", age: 30},
        {name: "thuyen2", age: 23}
    ];

    var tableHtml = '';
    data.forEach(function(item){
        tableHtml += `<tr>
        <td>${item.name}</td>
        <td>${item.age}</td>
        </tr>`;
    });

    document.getElementById("table-container").innerHTML = tableHtml;
});

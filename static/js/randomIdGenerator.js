let uniqueId = localStorage.getItem("uniqueId");

function generateUniqueId () {
    uniqueId = generateRadomId();
    localStorage.setItem("uniqueId", uniqueId);
    document.getElementById("uniqueIdOutput").textContent = uniqueId;

    function generateRadomId () {
        return Math.random().toString(36).substring(2, 8);
    }    
}

window.onload = function () {
    document.getElementById("uniqueIdOutput").textContent = uniqueId;
}

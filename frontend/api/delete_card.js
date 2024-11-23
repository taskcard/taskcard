document.getElementById("delete-card-button").addEventListener("click", function() {
    const cardId = document.getElementById("card-id").value;

    fetch(`http://127.0.0.1:5000/card/delete/${cardId}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("카드가 성공적으로 삭제되었습니다.");
            // 필요시 추가 로직
        } else {
            alert("카드 삭제 중 오류가 발생했습니다: " + data.error);
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("카드 삭제 중 오류가 발생했습니다.");
    });
});
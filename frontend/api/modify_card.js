document.getElementById("modify-card-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const cardId = document.getElementById("card-id").value;
    const title = document.getElementById("card-title").value;
    const content = document.getElementById("card-content").value;
    const category = document.getElementById("card-category").value;

    fetch(`http://127.0.0.1:5000/card/modify/${cardId}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            content: content,
            category: category
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("카드가 성공적으로 수정되었습니다.");
            // 필요시 추가 로직
        } else {
            alert("카드 수정 중 오류가 발생했습니다: " + data.error);
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("카드 수정 중 오류가 발생했습니다.");
    });
});
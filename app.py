// 1. 앱 실행 시 저장된 평가금액 불러오기 (없으면 기본값 사용)
document.addEventListener("DOMContentLoaded", () => {
    const savedAmount = localStorage.getItem("stockEvaluationAmount");
    if (savedAmount !== null) {
        document.getElementById("stockAmountInput").value = savedAmount;
    }
});

// 2. 수치 수정 및 저장 함수
function updateStockAmount() {
    const newAmount = document.getElementById("stockAmountInput").value;
    
    // 로컬 저장소에 저장 (앱을 껐다 켜도 유지됨)
    localStorage.setItem("stockEvaluationAmount", newAmount);
    alert("평가 금액이 저장되었습니다.");
}

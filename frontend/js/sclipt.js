function send_question(){
    console.log("push!");
    const question=document.getElementById("question");
    const answer=document.getElementById("answer");
    answer.value = question.value + "の返信";
}
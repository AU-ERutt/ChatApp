function send_question(){
    console.log("push!");
    const question=document.getElementById("question");
    const answer=document.getElementById("answer");
    answer.value = question.value + "の返信";
}

async function get_hello() {
    console.log("HELLO");
    const url = "http://127.0.0.1:5000/hello";
    fetch(url)
    .then(function(response) {
        return response.json();
    })
    .then(function(response) {  // 引数指定すると↑でreturnしたオブジェクトが入る（thenでチェーンしていける）
        console.log(response);
        console.log(response.data);
        document.getElementById("hello").value = response.data;
        return response.data;  // ここのtextをjsonやblobに変えると取得形式が変わる
      });
  }

async function set_textarea() {
    const txtarea = document.getElementById("hello");
    const result = await get_hello();
    console.log("result: ", result);
    console.log("type result: ", typeof result);
    txtarea.value = result;
}

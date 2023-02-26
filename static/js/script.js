const file_input = document.getElementById("real-file");
const customBtn = document.getElementById("custom-button");
const customTxt = document.getElementById("custom-text");
let flag = false

customBtn.addEventListener("click", function () {
  file_input.click();
});

function reset_file_name(file){
  if (file){
    customTxt.innerHTML = file.name;
    flag = true;
  }
  else{
    customTxt.innerHTML = "No file chosen, yet."
    flag = false;
  }
}

file_input.addEventListener("change", function () {
  let file = file_input.files[0]
  reset_file_name(file)
  let formData = new FormData()
  formData.append('file', file)
  const options = {method: 'POST', body: formData};
  fetch('/reset-session', options);
});


/* The following functions are for transcription and summarization*/

function transcribe(){
  if (flag){
    let transcript = document.getElementById("transcript");
    transcript.innerHTML = "Please Wait this may take some time...";
    fetch('/get-transcription').then(response => response.text()).then(data => transcript.innerHTML = data);
  }
  else
    alert("Please first select an audio file!");
}

function get_short_english_summarization() {
  if (flag){
    let title = document.getElementById("title");
    title.innerHTML = "Please Wait this may take some time...";
    fetch('/get-short-english-summarization').then(response => response.text()).then(data => title.innerHTML = data);
  }
  else
    alert("Please first select an audio file!");
}

function get_short_arabic_summarization() {
  if (flag){
    let title = document.getElementById("title");
    title.innerHTML = "Please Wait this may take some time...";
    fetch('/get-short-arabic-summarization').then(response => response.text()).then(data => title.innerHTML = data);
  }
  else
    alert("Please first select an audio file!");
}

function get_long_english_summarization() {
  if (flag){
    let summarization = document.getElementById("summarization");
    summarization.innerHTML = "Please Wait this may take some time...";
    fetch('/get-long-english-summarization').then(response => response.text()).then(data => summarization.innerHTML = data);
  }
  else
    alert("Please first select an audio file!");
}

function get_long_arabic_summarization() {
  if (flag){
    let summarization = document.getElementById("summarization");
    summarization.innerHTML = "Please Wait this may take some time...";
    fetch('/get-long-arabic-summarization').then(response => response.text()).then(data => summarization.innerHTML = data);
  }
  else
    alert("Please first select an audio file!");
}

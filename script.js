function yourFunction(){
    fetch('https://us-central1-killswitch-301923.cloudfunctions.net/function-1')
  .then((response) => {
    return response.text();
  })
  .then((myJson) => {
    console.log(myJson)
    if(myJson.includes("TRUE")){
     document.elementFromPoint(1041, 1010).click();
     document.elementFromPoint(892, 1010).click();
    }
  });
    setTimeout(yourFunction, 500);
}

yourFunction();

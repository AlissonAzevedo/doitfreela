window.onload = function(){
    document.getElementById('download')
    .addEventListener("click", () =>{
      const requisitos_pdf = this.document.getElementById("requisitos_pdf");
      console.log(requisitos_pdf);
      console.log(window);
      var opt = {
        margin: 1, 
        filename: 'requisitos.pdf',
        image: {type: 'jpg', quality: 0.98},
        html2canvas: {scale: 2},
        jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait'}
      };
      html2pdf().from(requisitos_pdf).set(opt).save();
    })
  }
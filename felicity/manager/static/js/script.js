var id;
const a = document.getElementById("homeLink");

function getToken(name) {
   let cookieValue = null;
   if (document.cookie && document.cookie != '') {
     const cookies = document.cookie.split(';');
     for (let i = 0; i < cookies.length; i++) {
       const cookie = cookies[i].trim();
       // Does this cookie string begin with the name we want?
       if (cookie.substring(0,name.length + 1) === (name + '=')) {
         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
         break;
       }
     }
   }
   return cookieValue;
  }
var csrftoken = getToken('csrftoken')

function create() {

   const invoiceForm = document.getElementById("invoiceForm");
   const formData = new FormData(invoiceForm);
   const data = Object.fromEntries(formData);
   //console.log(data);
   invoiceForm.reset();
   //console.log(data);

   var url = "/createInvoice"
   fetch(url, {
      method:'POST',
      headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken,
      }, 
      body:JSON.stringify({'post_data':data}) //JavaScript object of data to POST
   })
   .then((response) => {
      return response.json(); //converts response to json
   })
   .then((data) => {
         //console.log('data:',data)
         console.log(data.id);
         id = data.id;
      //Perform actions with the response data from the view
   });
   invoiceForm.style.display="none";
   const entryFormDiv = document.getElementById("entryFormDiv");
   entryFormDiv.style.display="block";
}

function addNew() {
   const invoicenum = document.getElementById("invoicenum");
   invoicenum.setAttribute('value', id);
   const entryForm = document.getElementById("entryForm");
   const entryFormData = new FormData(entryForm);
   const entryData = Object.fromEntries(entryFormData)
   entryForm.reset();

   url = "/createInvoice"
   fetch(url, {
      method:'POST',
      headers:{
         'Content-Type':'application/json',
         'X-CSRFToken':csrftoken,
         }, 
         body:JSON.stringify({'post_data':entryData}) //JavaScript object of data to POST
   })
   /*.then((response) => {
      return response.json(); //converts response to json
   })
   .then((data) => {
         //console.log('data:',data)
         console.log(data.id);
         id = data.id;
      //Perform actions with the response data from the view
   }); */
}

function entryDone() {
   addNew();
   const a = document.getElementById("homeLink");
   a.click();
}

function createChallan() {
   const challanForm = document.getElementById("challanForm");
   const challanFormData = new FormData(challanForm);
   const challanData = Object.fromEntries(challanFormData);
   //console.log(data);
   challanForm.reset();
   //console.log(data);

   var url = "/createChallan"
   fetch(url, {
      method:'POST',
      headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken,
      }, 
      body:JSON.stringify({'post_data':challanData}) //JavaScript object of data to POST
   })
   .then((response) => {
      return response.json(); //converts response to json
   })
   .then((data) => {
         //console.log('data:',data)
         console.log(data.id);
         id = data.id;
      //Perform actions with the response data from the view
   });
   challanForm.style.display="none";
   const challanEntryFormDiv = document.getElementById("challanEntryFormDiv");
   challanEntryFormDiv.style.display="block";
}

function addNewChallanEntry() {
   const challanNum = document.getElementById("challanNum");
   challanNum.setAttribute('value', id);
   const challanEntryForm = document.getElementById("challanEntryForm");
   const challanEntryFormData = new FormData(challanEntryForm);
   const challanEntryData = Object.fromEntries(challanEntryFormData)
   challanEntryForm.reset();

   url = "/createChallan"
   fetch(url, {
      method:'POST',
      headers:{
         'Content-Type':'application/json',
         'X-CSRFToken':csrftoken,
         }, 
         body:JSON.stringify({'post_data':challanEntryData}) //JavaScript object of data to POST
   })
}
function challanEntryDone() {
      addNewChallanEntry();
      const a = document.getElementById("homeLink");
      a.click();
}

   /*.then((response) => {
      return response.json(); //converts response to json
   })
   .then((data) => {
         //console.log('data:',data)
         console.log(data.id);
         id = data.id;
      //Perform actions with the response data from the view
   }); */
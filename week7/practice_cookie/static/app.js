document.addEventListener('DOMContentLoaded', function(){
    const form = document.querySelector('form');
    const checkbox = document.getElementById('agree-policy');

    form.addEventListener('submit',async function(event){
        console.log("Submit button clicked");
        if(!checkbox.checked){
            event.preventDefault();
            alert('Please check the checkbox first');
            console.log("Checkbox is not checked! Form submission prevented.");
        }
        // event.preventDefault();
        // await signin();
    });
})

// // 使用表單格式
// async function signin(){
//     const formData = new URLSearchParams();
//     formData.append("username", document.getElementById("username").value);
//     formData.append("password", document.getElementById("password").value);
//     // console.log(formData.toString()); //username=test&password=test
//     try {
//         const response = await fetch("/signin", {
//             method: "POST",
//             headers: { "Content-Type": "application/x-www-form-urlencoded" },
//             body: formData.toString(),
//         });       
//         if (!response.ok) {
//             throw new Error(`HTTP error! Status: ${response.status}`);
//         }
//         const data = await response.json(); //{ "redirect": "/member.html" } or { "redirect": "/error.html" }
//         if (data.redirect) {
//             window.location.href = data.redirect;
//         }
//     } catch (error) {
//         console.error("Error", error);
//     }
// }



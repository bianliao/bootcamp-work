document.addEventListener('DOMContentLoaded', function(){
    const path = window.location.pathname;

    if(path === "/"){
        // signup
        const name = document.getElementById('signup_name');
        const username = document.getElementById('signup_username');
        const password = document.getElementById('signup_password');
        const submit = document.getElementById('signup_submit');
    
        const nameError = document.getElementById('signup_name_error');
        const usernameError = document.getElementById('signup_username_error');
        const passwordError = document.getElementById('signup_password_error');  
        
        const inputRule = /^[A-Za-z0-9]{2,}$/;
        function validateSignupInputs(){
            nameError.textContent= name.value === "" ? "姓名不得空白" 
                : (!inputRule.test(name.value) ? "姓名只能包含英數字，且至少 2 個字元" : "");
            usernameError.textContent= username.value === "" ? "帳號不得空白" 
                : (!inputRule.test(username.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            passwordError.textContent= password.value === "" ? "密碼不得空白" 
                : (!inputRule.test(password.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            submit.disabled = !(nameError.textContent === "" && usernameError.textContent === "" && passwordError.textContent === "");
        }
    
        document.getElementById('signup_form').addEventListener('input', validateSignupInputs);
    
        //signin
        const signinUsername = document.getElementById('signin_username');
        const signinPassword = document.getElementById('signin_password');
        const signinSubmit = document.getElementById('signin_submit');
    
        const signinUsernameError = document.getElementById('signin_username_error');
        const signinPasswordError = document.getElementById('signin_password_error');  
        
        function validateSignupInputs(){
            usernameError.textContent= username.value === "" ? "帳號不得空白" 
                : (!inputRule.test(username.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            passwordError.textContent= password.value === "" ? "密碼不得空白" 
                : (!inputRule.test(password.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            submit.disabled = !(nameError.textContent === "" && usernameError.textContent === "" && passwordError.textContent === "");
        }

        function validateSigninInputs(){
            signinUsernameError.textContent= signinUsername.value === "" ? "帳號不得空白" 
                : (!inputRule.test(signinUsername.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            signinPasswordError.textContent= signinPassword.value === "" ? "密碼不得空白" 
                : (!inputRule.test(signinPassword.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            signinSubmit.disabled = !(signinUsernameError.textContent === "" && signinPasswordError.textContent === "");
        }
    
        document.getElementById('signin_form').addEventListener('input',validateSigninInputs);
    }
    
    if(path==='/member'){
        // createMessage
        const createMessageContent = document.getElementById('create_message_content');
        const createMessageError = document.getElementById('create_message_error');
        const createMessageSubmit = document.getElementById('create_message_submit');
        const inputRule = /^[\p{L}\p{N}]+$/u;
        function createMessage(){
            if (createMessageContent.value === ""){
                createMessageError.textContent="";
                createMessageSubmit.disabled = true;
            }else if(createMessageContent.value.length > 40){
                createMessageError.textContent="請少於 40 個字元";
                createMessageSubmit.disabled = true;
            }else{
                createMessageError.textContent="";
                createMessageSubmit.disabled = false;
            }
        }
        createMessageContent.addEventListener('input',createMessage);

        // deleteMessage
        document.querySelectorAll('.mdi-close').forEach(button => {
            button.addEventListener('click', function(){
                const messageId = this.getAttribute('message-id');
                deleteMessage(messageId);
            });
        })

        async function deleteMessage(messageId) {
            console.log(messageId)
            const isConfirmed = confirm("確定要刪除這則留言嗎？");
            if (!isConfirmed){
                return;
            }
            try{
                const response = await fetch(`/deleteMessage/${messageId}`,{
                    method:'DELETE',
                });
                if (!response.ok) {
                    throw new Error("Could not fetch");
                }
                window.location.reload();
            } catch (error){
                console.error("Error fetching data:", error);
            }
        }

    }
})
async function call() {
    const response = await fetch(
        "/api/user-status"
    );
    
    const responseData = await response.json();
    // const message = responseData.message;
    
    console.log(responseData)
}

call()
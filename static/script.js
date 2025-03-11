window.addEventListener('load', checkStatus);

function checkStatus() {
    if (Cookies.get('clientSignIn')) {
        $('.client-no').hide()
        $('.client-yes').show()
        $('#un').html(Cookies.get('clientSignIn'))
    } else {
        $('.client-no').show()
        $('.client-yes').hide()
    }
}

function signIn() {
    Cookies.set('clientSignIn', $('#sign-in').val(), {path: '/', secure: true, sameSite: 'strict'});
    checkStatus();
}

function signOut() {
    Cookies.remove('clientSignIn', {path: '/', secure: true, sameSite: 'strict'});
    checkStatus();
}
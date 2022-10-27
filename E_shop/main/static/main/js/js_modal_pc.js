
// modal login / register
function modalRegistration(){
    var modalRegistration = document.querySelector('.js-modal-registration')

    var modal = document.querySelector('.modal')

    var modalClose =document.querySelector('.modal-close')

    var modalCloseContainer=document.querySelector('.modal-registration')

    function showModalRegistration(){
        modal.setAttribute('style','display: flex')
    }
    function closeModalRegistration(){
        modal.setAttribute('style','display: none')
    }

    modalRegistration.addEventListener('click',showModalRegistration)

    modalClose.addEventListener('click',closeModalRegistration)
    modal.addEventListener('click',closeModalRegistration)

    modalCloseContainer.addEventListener('click',function(envent){
        event.stopPropagation()
    })
}


function openModal_login(){
    const modalLogin = document.querySelector('.js-modal-login')
    const modal_a = document.querySelector('.modal_a')
    const modalClose =document.querySelector('.modal-close_a')
    const modalCloseContainer=document.querySelector('.modal-login')
    function showModalLogin(){
    modal_a.setAttribute('style','display: flex')
    }
    function closeModalLogin(){
    modal_a.setAttribute('style','display: none')
    }
    modalLogin.addEventListener('click',showModalLogin)
    modalClose.addEventListener('click',closeModalLogin)
    modal_a.addEventListener('click',closeModalLogin)
    modalCloseContainer.addEventListener('click',function(envent){
        event.stopPropagation()
    })
}

modalRegistration()
openModal_login()

var here=document.getElementById("registration_here")

function clicktologin(){
    var modal_a = document.querySelector('.modal_a')
    var modal = document.querySelector('.modal')
    function modal_handle(){
        modal.setAttribute('style','display: none')
        modal_a.setAttribute('style','display: flex')
    }

    here.addEventListener("click",modal_handle)
    
}
clicktologin()


// modal login / register



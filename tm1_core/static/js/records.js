//Capture button
let form = document.getElementById('create-years');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    SendYears(url=form.getAttribute('action'), data=new FormData(form))
    .then(response => {
        if (response.status == 200) {
            Swal.fire({
                icon: 'success',
                title: 'Miembros creados en la dimensión Year_TI',
                showConfirmButton: true,
                timer:3000
              })
            location.reload()
        }else{
            Swal.fire({
                icon: 'warning',
                title: 'Error al procesar la solicitud',
                text: 'Corrobore los datos',
                showConfirmButton: true,
                timer:3000
              })
        }
    })
    .catch(err => {
        Swal.fire({
            icon: 'error',
            title: 'Error al procesar la solicitud',
            text: 'Notifique al administrador o verifique su conexión a la red',
            showConfirmButton: true,
            timer:3000
          })
          console.log(err)
    })
})

async function SendYears(url,data) {
    const response = await fetch(url, {
        method: 'POST',
        body: data});
        return response;
}

//Delete record
document.querySelectorAll('.btn-warning').forEach(element => {
    element.addEventListener('click', (event) =>{
        Swal.fire({
            title: '¿Deseas eliminar el elemento?',
            icon: 'question',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Eliminar',
            cancelButtonText: 'Cancelar'
          }).then((result) => {
            if (result.isConfirmed) {
                let server = event.target.getAttribute('server');
                let year = event.target.innerHTML.trim();
                const crsf = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
                form_delete = new FormData()
                form_delete.append("csrfmiddlewaretoken", crsf);
                //Call
                DeleteYear(url='years/'+server+'/'+year, data=form_delete)
                .then(response => {
                    if (response.status == 200) {
                        Swal.fire({
                            icon: 'success',
                            title: 'Miembro eliminado en la dimensión Year_TI',
                            showConfirmButton: true,
                            timer:3000
                          })
                        location.reload()
                    }else{
                        Swal.fire({
                            icon: 'warning',
                            title: 'Error al procesar la solicitud',
                            text: 'Corrobore los datos',
                            showConfirmButton: true,
                            timer:3000
                          })
                    }
                })
                .catch(err => {
                    Swal.fire({
                        icon: 'error',
                        title: 'Error al procesar la solicitud',
                        text: 'Notifique al administrador o verifique su conexión a la red',
                        showConfirmButton: true,
                        timer:3000
                      })
                      console.log(err)
                })
            }
          })
    })
})

async function DeleteYear(url,data) {
    const response = await fetch(url, {
        method: 'POST',
        body: data});
        return response;
}
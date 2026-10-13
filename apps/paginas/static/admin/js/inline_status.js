document.addEventListener("DOMContentLoaded", function () {

    document.querySelectorAll(".inline-related").forEach(function (inline) {

        let tieneDatos = false;


        // Solo campos visibles
        inline.querySelectorAll(
            "input:not([type='hidden']), textarea, select"
        ).forEach(function (campo) {


            let nombre = campo.name.split("-").pop();


            // Ignorar campos automáticos
            const ignorar = [
                "orden",
                "activo",
                "id",
                "pagina",
                "DELETE"
            ];


            if (ignorar.includes(nombre)) {
                return;
            }



            if (campo.value.trim() !== "") {

                tieneDatos = true;

            }


        });



        if (tieneDatos) {
            inline.classList.add("inline-completo");
        }


    });


});
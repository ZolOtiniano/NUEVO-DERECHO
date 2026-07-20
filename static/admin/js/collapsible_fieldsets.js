document.addEventListener("DOMContentLoaded", function () {

    document.querySelectorAll(".module h2").forEach(function (header) {

        let fieldset = header.closest(".module");

        header.style.cursor = "pointer";


        // Crear icono cerrado inicialmente
        let icon = document.createElement("span");
        icon.innerHTML = "▶ ";
        icon.classList.add("collapse-icon");

        header.prepend(icon);


        // Ocultar contenido al iniciar
        fieldset.classList.add("collapsed");

        fieldset.querySelectorAll(
            ".form-row, .inline-group"
        ).forEach(function (element) {

            element.style.display = "none";

        });


        // Evento abrir/cerrar
        header.addEventListener("click", function () {

            let collapsed = fieldset.classList.toggle("collapsed");


            fieldset.querySelectorAll(
                ".form-row, .inline-group"
            ).forEach(function (element) {

                element.style.display = collapsed
                    ? "none"
                    : "";

            });


            icon.innerHTML = collapsed
                ? "▶ "
                : "▼ ";

        });

    });

});
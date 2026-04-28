function updateFormIndices() {
    const container = document.getElementById("ingredients-container");
    const forms = container.querySelectorAll(".ingredient-form");
    const totalForms = document.getElementById("id_ingredients-TOTAL_FORMS");
    if (totalForms) {
        totalForms.value = forms.length;
    }
    forms.forEach((form, index) => {
        const inputs = form.querySelectorAll("input, select, textarea");
        inputs.forEach(input => {
            const oldName = input.getAttribute("name");
            if (oldName) {
                let baseName = oldName.replace(/ingredients-\d+-/, '');
                const newName = `ingredients-${index}-${baseName}`;
                input.setAttribute("name", newName);
            }
            const oldId = input.getAttribute("id");
            if (oldId) {
                let baseId = oldId.replace(/id_ingredients-\d+-/, 'id_ingredients-');
                const newId = `id_ingredients-${index}-${baseId.split('-').pop()}`;
                input.setAttribute("id", newId);
            }
        });
        const labels = form.querySelectorAll("label");
        labels.forEach(label => {
            const forAttr = label.getAttribute("for");
            if (forAttr && forAttr.includes('id_ingredients')) {
                let baseFor = forAttr.replace(/id_ingredients-\d+-/, 'id_ingredients-');
                const newFor = `id_ingredients-${index}-${baseFor.split('-').pop()}`;
                label.setAttribute("for", newFor);
            }
        });
    });
}

function addRemoveButtonsAndHandlers() {
    const forms = document.querySelectorAll(".ingredient-form");
    forms.forEach((form, index) => {
        // Убираем кнопку "Удалить" для первой формы
        if (index === 0) {
            // Если кнопка есть — удаляем
            const existingButton = form.querySelector(".btn-remove-ingredient");
            if (existingButton) {
                existingButton.remove();
            }
        } else {
            // Для остальных форм добавляем кнопку, если её нет
            let removeButton = form.querySelector(".btn-remove-ingredient");
            if (!removeButton) {
                removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.className = "btn-remove-ingredient";
                removeButton.textContent = "Удалить";
                form.appendChild(removeButton);
            }
            // Удаляем старый обработчик и добавляем новый
            removeButton.removeEventListener("click", removeIngredient);
            removeButton.addEventListener("click", removeIngredient);
        }
    });
}

function removeIngredient(e) {
    e.preventDefault();
    const formToRemove = e.target.closest(".ingredient-form");
    // Удаляем форму
    formToRemove.remove();
    // Обновляем индексы
    updateFormIndices();
    // Перезапускаем добавление кнопок
    addRemoveButtonsAndHandlers();
}

document.addEventListener("DOMContentLoaded", function () {
    updateFormIndices();
    addRemoveButtonsAndHandlers();
});

document.addEventListener("htmx:afterSwap", function (event) {
    if (event.target.id === "ingredients-container") {
        updateFormIndices();
        addRemoveButtonsAndHandlers();
    }
});
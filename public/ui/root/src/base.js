class Language {
    constructor() {
        this.selector = document.getElementById("language").children[0];
        this.options = document.getElementById("language").children[1];
        this.selector.addEventListener("click", (evt) => this.selectorClicked(evt));
        this.options.addEventListener("click", (evt) => this.optionClicked(evt));
        this.toogled = false;
    }
    selectorClicked(evt) {
        if (this.toogled) {
            this.options.classList.replace("enabled", "disabled");
        }
        else {
            this.options.classList.replace("disabled", "enabled");
        }
        this.toogled = !this.toogled;
    }
    optionClicked(evt) {
        this.setLanguage(evt.target);
    }
    setLanguage(selected_element) {
        let languageElement = selected_element;
        if (selected_element.nodeName == "IMG") {
            languageElement = selected_element.parentNode;
        }
        console.log(languageElement.dataset.lang);
    }
}
function on_load() {
    console.debug(new Language());
}
window.addEventListener("load", on_load);
//# sourceMappingURL=base.js.map
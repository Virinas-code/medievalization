class Language {
    selector: Element;
    options: Element;

    toogled: boolean;

    constructor() {
        this.selector = document.getElementById("language").children[0];
        this.options = document.getElementById("language").children[1];

        this.selector.addEventListener("click", (evt) => this.selectorClicked(evt as MouseEvent))
        this.options.addEventListener("click", (evt) => this.optionClicked(evt as MouseEvent));

        this.toogled = false;
    }

    selectorClicked(evt: MouseEvent): void {
        if (this.toogled) {
            this.options.classList.replace("enabled", "disabled");
        } else {
            this.options.classList.replace("disabled", "enabled");
        }

        this.toogled = !this.toogled;
    }

    optionClicked(evt: MouseEvent): void {
        this.setLanguage(evt.target as HTMLElement);
    }

    setLanguage(selected_element: HTMLElement): void {
        let languageElement: HTMLElement = selected_element;
        if (selected_element.nodeName == "IMG") {
            languageElement = selected_element.parentNode as HTMLElement;
        }

        console.log(languageElement.dataset.lang);
    }
}

function on_load(): void {
    console.debug(new Language());
}

window.addEventListener("load", on_load);

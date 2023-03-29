export { load, ready };
import { Component } from "./component.js";

let ready: Event = new Event("medievalization.components.ready");

export class SmallCombo implements Component {
    element: HTMLElement;
    selector: HTMLElement;
    options: HTMLElement;

    open: boolean;

    constructor(from: HTMLElement) {
        this.element = from;

        this.selector = from.children[0] as HTMLElement;
        this.options = from.children[1] as HTMLElement;

        this.selector.addEventListener("click", (ev: MouseEvent): void => this.selectorClicked(ev));
        this.open = false;

        this.options.addEventListener("click", (ev: MouseEvent): void => this.optionClicked(ev));
    }

    selectorClicked(ev: MouseEvent): void {
        if (this.open) {
            this.options.classList.replace("scbo-open", "scbo-closed");
        } else {
            this.options.classList.replace("scbo-closed", "scbo-open");
        }
        this.open = !this.open;
    }

    optionClicked(ev: MouseEvent): void {
        if (ev.target == this.options) {
            return;
        }

        let targetElement: HTMLElement = ev.target as HTMLElement;

        let data: DOMStringMap = targetElement.dataset;
        if (Object.keys(targetElement.dataset).indexOf("scboitemid") == -1) {
            let parentData: DOMStringMap = targetElement.parentElement.dataset;
            if (Object.keys(parentData).indexOf("scboitemid") == -1) {
                return;
            } else {
                data = parentData;
            }
        }

        this.handle(data.scboitemid);
    }

    handle(data: string): void {
        return;
    }

    setHandle(newHandle: (data: string) => void): void {
        this.handle = newHandle;
    }
}

function load(): void {
    window.Components = {};
    window.Components["SCBO"] = [];

    for (const element of document.getElementsByClassName("scbo")) {
        window.Components["SCBO"].push(new SmallCombo(element as HTMLElement));
    }

    window.dispatchEvent(ready);
}
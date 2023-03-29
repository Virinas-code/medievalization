export { load, ready };
let ready = new Event("medievalization.components.ready");
export class SmallCombo {
    constructor(from) {
        this.element = from;
        this.selector = from.children[0];
        this.options = from.children[1];
        this.selector.addEventListener("click", (ev) => this.selectorClicked(ev));
        this.open = false;
        this.options.addEventListener("click", (ev) => this.optionClicked(ev));
    }
    selectorClicked(ev) {
        if (this.open) {
            this.options.classList.replace("scbo-open", "scbo-closed");
        }
        else {
            this.options.classList.replace("scbo-closed", "scbo-open");
        }
        this.open = !this.open;
    }
    optionClicked(ev) {
        if (ev.target == this.options) {
            return;
        }
        let targetElement = ev.target;
        let data = targetElement.dataset;
        if (Object.keys(targetElement.dataset).indexOf("scboitemid") == -1) {
            let parentData = targetElement.parentElement.dataset;
            if (Object.keys(parentData).indexOf("scboitemid") == -1) {
                return;
            }
            else {
                data = parentData;
            }
        }
        this.handle(data.scboitemid);
    }
    handle(data) {
        return;
    }
    setHandle(newHandle) {
        this.handle = newHandle;
    }
}
function load() {
    window.Components = {};
    window.Components["SCBO"] = [];
    for (const element of document.getElementsByClassName("scbo")) {
        window.Components["SCBO"].push(new SmallCombo(element));
    }
    window.dispatchEvent(ready);
}
//# sourceMappingURL=scbo.js.map
class SmallCombo {
    element: HTMLElement;

    constructor(from: HTMLElement) {
        this.element = from;
    }
}

export function init(): void {
    let combos: Array<SmallCombo> = new Array();
    for (const combo of document.getElementsByClassName("scbo")) {
        combos.push(new SmallCombo(combo as HTMLElement));
    }
}
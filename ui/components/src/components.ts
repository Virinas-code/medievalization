export {};

import { Component } from "./component.js";
import { load as load_scbo } from "./scbo.js";

type ComponentsList = {
    [key: string]: Array<Component>,
}

declare global {
    interface Window {
        Components: ComponentsList,
    }
}

function load_all(): void {
    load_scbo();
}

window.addEventListener("DOMContentLoaded", load_all);
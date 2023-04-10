export {};
import { SmallCombo, ready } from "../../components/src/scbo.js";

function changeLanguage(language: string): void {
    fetch("/api/i18n/" + language).then(() => {location.reload();});
}

function loadSCBO(): void {
    (window.Components["SCBO"][0] as SmallCombo).setHandle(changeLanguage);
}

window.addEventListener(ready.type, loadSCBO);

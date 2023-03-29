export {};
import { SmallCombo, ready } from "../../components/src/scbo.js";

function loadSCBO(): void {
    (window.Components["SCBO"][0] as SmallCombo).setHandle(console.log);
}

window.addEventListener(ready.type, loadSCBO);
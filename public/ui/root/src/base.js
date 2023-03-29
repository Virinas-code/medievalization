import { ready } from "../../components/src/scbo.js";
function loadSCBO() {
    window.Components["SCBO"][0].setHandle(console.log);
}
window.addEventListener(ready.type, loadSCBO);
//# sourceMappingURL=base.js.map
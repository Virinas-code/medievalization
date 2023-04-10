import { ready } from "../../components/src/scbo.js";
function changeLanguage(language) {
    fetch("/api/i18n/" + language).then(() => { location.reload(); });
}
function loadSCBO() {
    window.Components["SCBO"][0].setHandle(changeLanguage);
}
window.addEventListener(ready.type, loadSCBO);
//# sourceMappingURL=base.js.map
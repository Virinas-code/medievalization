define(["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    exports.init = void 0;
    class SmallCombo {
        constructor(from) {
            this.element = from;
        }
    }
    function init() {
        let combos = new Array();
        for (const combo of document.getElementsByClassName("scbo")) {
            combos.push(new SmallCombo(combo));
        }
    }
    exports.init = init;
});
//# sourceMappingURL=scbo.js.map
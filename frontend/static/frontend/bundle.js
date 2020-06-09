(function (f) {
    if (typeof exports === "object" && typeof module !== "undefined") {
        module.exports = f()
    } else if (typeof define === "function" && define.amd) {
        define([], f)
    } else {
        var g;
        if (typeof window !== "undefined") {
            g = window
        } else if (typeof global !== "undefined") {
            g = global
        } else if (typeof self !== "undefined") {
            g = self
        } else {
            g = this
        }
        g.lib = f()
    }
})(function () {
    var define, module, exports;
    return (function () {
        function r(e, n, t) {
            function o(i, f) {
                if (!n[i]) {
                    if (!e[i]) {
                        var c = "function" == typeof require && require;
                        if (!f && c) return c(i, !0);
                        if (u) return u(i, !0);
                        var a = new Error("Cannot find module '" + i + "'");
                        throw a.code = "MODULE_NOT_FOUND", a
                    }
                    var p = n[i] = {exports: {}};
                    e[i][0].call(p.exports, function (r) {
                        var n = e[i][1][r];
                        return o(n || r)
                    }, p, p.exports, r, e, n, t)
                }
                return n[i].exports
            }

            for (var u = "function" == typeof require && require, i = 0; i < t.length; i++) o(t[i]);
            return o
        }

        return r
    })()({
        1: [function (require, module, exports) {
//EXPORT
            exports.add = add;
            exports.remove = remove;
            exports.getCount = getCount;


//DEFINITIONS
            function getCount(parent, getChildrensChildren) {
                var relevantChildren = 0;
                var children = parent.childNodes.length;
                for (var i = 0; i < children; i++) {
                    if (parent.childNodes[i].nodeType != 3) {
                        if (getChildrensChildren)
                            relevantChildren += getCount(parent.childNodes[i], true);
                        relevantChildren++;
                    }
                }
                return relevantChildren;
            }

            function add(containerName, type, name) {
                var container = document.getElementById(containerName);
                var input = document.createElement("input");
                input.type = type;

                input.name = name;
                container.appendChild(document.createElement("br"));
                container.appendChild(input);
                // Append a line break
                container.appendChild(document.createElement("br"));
                return false;
            }

            function remove(containerName) {
                var numElementsInSelection = 3
                var container = document.getElementById(containerName);
                for (var i = 0; i < numElementsInSelection; i++) {
                    container.childNodes.item(container.childElementCount - 1).remove();
                }
                return false;
            }

        }, {}], 2: [function (require, module, exports) {
            module.exports = require('./lib')

        }, {"./lib": 1}]
    }, {}, [2])(2)
});

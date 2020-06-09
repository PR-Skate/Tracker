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

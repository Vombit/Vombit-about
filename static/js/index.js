function openPopup(title, description, dependencies) {
    var popup = document.getElementById('popup');
    var popupTitle = document.getElementById('popup-title');
    var popupDescription = document.getElementById('popup-description');
    var popupDependencies = document.getElementById('popup-dependencies');

    popupTitle.innerHTML = title;
    popupDescription.innerHTML = description;
    popupDependencies.innerHTML = '';

    var listItems = dependencies.map(function(dependency) {
        var listItem = document.createElement('li');
        listItem.textContent = dependency;
        return listItem;
    });

    listItems.forEach(function(listItem) {
        popupDependencies.appendChild(listItem);
    });

    popup.style.display = 'block';
}

function closePopup() {
    document.getElementById('popup').style.display = 'none';
}
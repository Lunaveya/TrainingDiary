function createSelector(name, isClass = false) {
    const prefix = isClass ? '.' : '#';

    return `${prefix}${name}`
}

function search() {
    const searchValue = $(createSelector(SEARCH_INPUT_SELECTOR_NAME)).val();

            if (!searchValue) {
                alert('Введите значение для поиска');
            }

            location.href = `/search/${searchValue}`;
}

$(() => {
    $(createSelector(SEARCH_BTN_SELECTOR_NAME)).click(
        () => {search()}
    );
    $(createSelector(SEARCH_INPUT_SELECTOR_NAME)).keydown(function(event) {
        if (event.key === 'Enter') {
            search();
        }
    });
    $(createSelector(LOGOUT_BTN_SELECTOR)).click((event) => {
        event.preventDefault();
        const csrfmiddlewaretoken = $('[name="csrfmiddlewaretoken"]').val();

        $.post('/logout/', {csrfmiddlewaretoken}, () => {
        location.reload();
        });

    });
});


//кнопки лайк и дизлайк

$(createSelector(LIKE_BTN_SELECTOR)).click(
    () => {
        setMark(true);
    }
);

$(createSelector(DISLIKE_BTN_SELECTOR)).click(
    () => {
        setMark(false);
    }
);

function setMark(isPositive) {
    const articleId = Number(location.pathname.split('/')[2]);
    const csrfmiddlewaretoken = $('[name="csrfmiddlewaretoken"]').val();
    $.post(
        '/article/mark', {csrfmiddlewaretoken, articleId, isPositive}, () => {location.reload();}
    )
}
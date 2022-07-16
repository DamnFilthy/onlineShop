 /**
  * Class implements breadcrumbs on the site
  * @param {string} element - main block in template
  * */
class Breadcrumbs {
    constructor(element) {
        this.$element = $(element);
        this.setListeners();
    }

    setListeners() {
        // URL to array
        const filteredLinks = document.location.pathname.split('/').filter(el => el !== '');

        // Add main link
        if (filteredLinks.length >= 1) {
            this.$element.append(`/ <a href="/">Главная</a> /`)
        }

        // Add other links && capitalise && translate text
        filteredLinks.forEach((item, index) => {
            let completeUrl = filteredLinks.slice(0, index + 1).join('/')
            Translater.TransalteString(filteredLinks[index], 'ru').then(response => {
                this.$element.append(
                    `<a href="/${completeUrl}">${Capitalize.CapitalizeSting((response.split('%').join('')))}</a> /`
                )
            })
        })
    }
}

$(() => {
    $('.js-breadcrumb').each((i, item) => new Breadcrumbs(item));
});

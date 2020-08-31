import { createElement } from '../helpers/domHelper.js';
import { createGetButton, createSetButton } from './wallpaperControl.js';

export function createFilters(filters) {
    const container = createElement({ tagName: 'div', className: 'wallpaper__root' });
    const controlElement = createElement({ tagName: 'div', className: 'control__root' });
    
    const getElement = createElement({ tagName: 'div', className: 'get-wallpaper__root' });
    const { categories, resolutions } = filters;
    const categoriesElement = createSelector('category', categories);
    const resolutionsElement = createSelector('resolution', resolutions);
    const getBtn = createGetButton();
    getElement.append(categoriesElement, resolutionsElement, getBtn);
    
    const setElement = createElement({ tagName: 'div', className: 'set-wallpaper__root' });
    const pathElement = createPathElement();
    const setBtn = createSetButton();
    setElement.append(pathElement, setBtn);
    setElement.style.visibility = 'hidden';

    const previewElement = createElement({ tagName: 'div', className: 'wallpaper-preview__root' });
    const preview = createElement({ tagName: 'img', className: 'wallpaper-preview', attributes:{ id: 'preview' } });
    previewElement.append(preview);

    controlElement.append(getElement, setElement);
    container.append(controlElement, previewElement);

    return container;
}

function createSelector(parameter, options) {
    const attributes = {
        id: `${parameter}-filter`
    };
    const selectorElement = createElement({
        tagName: 'select',
        className: 'filter',
        attributes
    });

    const optionElements = options.map((option) => createOption(option));
    selectorElement.append(...optionElements);
    
    return selectorElement;
}

function createOption(value) {
    const attributes = {
        value
    };
    const optionElement = createElement({
        tagName: 'option',
        attributes
    });
    optionElement.innerText = value;
   
    return optionElement;
}

function createPathElement() {
    const attributes = {
        type: 'text',
        id: 'download-path'
    }
    const pathElement = createElement({ tagName: 'input', className: 'download-path__input', attributes});

    return pathElement;
}
import {wallpaperService} from '../services/wallpaperService.js';
import { createElement } from '../helpers/domHelper.js';
import { renderPreview } from './preview.js';

export function createGetButton() {
    const onClink = () => getPicture();
    const btn = createElement({ tagName: 'button', className: 'btn-get' });
    btn.innerText = 'Get random picture';
    btn.addEventListener('click', onClink, false);

    return btn;
}


export function createSetButton() {
    const onClick = () => setPicture();
    const btn = createElement({ tagName: 'button', className: 'btn-set' });
    btn.innerText = 'Download and set wallpaper';
    btn.addEventListener('click', onClick, false);

    return btn;
}

async function getPicture() {
    const categoriesElement = document.getElementById('category-filter');
    const selectedCategory = categoriesElement[categoriesElement.selectedIndex].value;

    const resolurionsElement = document.getElementById('resolution-filter');
    const selectedResolution = resolurionsElement[resolurionsElement.selectedIndex].value;
    
    try {
        const pictureUrl = await wallpaperService.getPicture(selectedCategory, selectedResolution);
        await renderPreview(pictureUrl);
        const [ setElement ] = document.getElementsByClassName('set-wallpaper__root');
        setElement.style.visibility = 'visible';
    } catch (error) {
        console.warn(error);
    }
    
}

async function setPicture() {
    const preview = document.getElementById('preview');
    const url = preview.src;
    const pathElement = document.getElementById('download-path');
    const path = pathElement.value;
    
    const categoriesElement = document.getElementById('category-filter');
    const selectedCategory = categoriesElement[categoriesElement.selectedIndex].value;

    const resolurionsElement = document.getElementById('resolution-filter');
    const selectedResolution = resolurionsElement[resolurionsElement.selectedIndex].value;

    try {
        console.log(url, path);
        await wallpaperService.setPicture(url, path, selectedCategory, selectedResolution);
    } catch (error) {
        console.warn(error);
    }
}

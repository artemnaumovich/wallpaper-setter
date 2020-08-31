import { wallpaperService } from './services/wallpaperService.js';
import { createFilters } from './components/filtersView.js';

class App {
    constructor() {
        this.startApp();
    }

    static rootElement = document.getElementById('root');
    static loadingElement = document.getElementById('loading-overlay');

    async startApp() {
        try {
            App.loadingElement.style.visibility = 'visible';

            const filters = await wallpaperService.getFilters();
            const filtersElement = createFilters(filters); 
            
            App.rootElement.appendChild(filtersElement);
        } catch (error) {
            console.warn(error);
            App.rootElement.innerText = 'Failed to load data(check your connection and/or try again)';
        } finally {
            App.loadingElement.style.visibility = 'hidden';
        }
    }
}

export default App;
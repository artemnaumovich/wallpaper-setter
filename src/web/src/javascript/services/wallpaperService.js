class WallpaperService {
    async getFilters() {
        try {
            const result = await eel.get_filters()();
            return result;
        } catch (error) {
            throw error;
        }
    }

    async getPicture(category, resolution) {
        try {
            const result = await eel.get_picture_url(category, resolution)();
            return result;
        } catch (error) {
            throw error;
        }
    }

    async setPicture(url, path, category, resolution) {
        try {
            await eel.set_picture(path, url, category, resolution)();
        } catch (error) {
            throw error;
        }
    }
}

export const wallpaperService = new WallpaperService();
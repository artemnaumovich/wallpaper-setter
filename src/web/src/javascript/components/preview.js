export async function renderPreview(url) {
    const preview = document.getElementById('preview');
    preview.src = url;
}
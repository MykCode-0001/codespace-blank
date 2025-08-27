function navigate(page) {
    const contentDiv = document.getElementById('content');
    let content = '';
    switch (page) {
        case 'home':
            content = '<h1>Home Page</h1><p>Welcome to the home page!</p>';
            history.pushState({ page }, '', `/dashboard/home`);
            break;
        case 'about':
            content = '<h1>About Page</h1><p>This is the about page.</p>';
            history.pushState({ page }, '', `/dashboard/about`);
            break;
        default:
            content = '<h1>404 Not Found</h1>';
    }
    contentDiv.innerHTML = content;
}
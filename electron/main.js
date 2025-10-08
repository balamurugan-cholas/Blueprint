// electron/main.js
const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const isDev = process.env.NODE_ENV !== 'production';

let win; // global reference to prevent garbage collection

function createWindow() {
  win = new BrowserWindow({
    width: 1280,
    height: 800,
    frame: false,
    show: false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  const djangoURL = 'http://127.0.0.1:8000';

  // Load Django URL in dev or bundled HTML in production
  if (isDev) {
    win.loadURL(djangoURL);
  } else {
    win.loadFile(path.join(__dirname, '..', 'dist', 'index.html'));
  }

  // Show window when ready
  win.once('ready-to-show', () => win.show());

  // Open DevTools in dev mode
  if (isDev) {
    win.webContents.openDevTools({ mode: 'detach' });
  }

  // Optional: Log any window events for debugging
  win.on('minimize', () => console.log('Window minimized'));
  win.on('maximize', () => console.log('Window maximized'));
  win.on('unmaximize', () => console.log('Window unmaximized'));
  win.on('close', () => console.log('Window closed'));
}

// IPC listener for window controls
ipcMain.on('window-control', (event, action) => {
  if (!win) {
    console.warn('No window instance available for IPC');
    return;
  }

  console.log('Received window-control action:', action); // Debug log

  switch (action) {
    case 'minimize':
      win.minimize();
      break;
    case 'maximize':
      if (win.isMaximized()) win.unmaximize();
      else win.maximize();
      break;
    case 'close':
      win.close();
      break;
    default:
      console.warn('Unknown window-control action:', action);
  }
});

// IPC listener for Always on Top
ipcMain.on('always-on-top', (event, flag) => {
  if (!win) {
    console.warn('No window instance available for Always on Top');
    return;
  }
  console.log('Setting Always on Top:', flag); // Debug log
  win.setAlwaysOnTop(flag);
});

// App lifecycle
app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) createWindow();
});

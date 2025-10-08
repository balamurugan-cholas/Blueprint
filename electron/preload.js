// electron/preload.js
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  // Electron / Node versions
  versions: process.versions,

  // 🪟 Window controls
  windowControl: (action) => ipcRenderer.send('window-control', action),
  minimize: () => ipcRenderer.send('window-control', 'minimize'),
  maximize: () => ipcRenderer.send('window-control', 'maximize'),
  close: () => ipcRenderer.send('window-control', 'close'),

  // 🏷 Always on Top
  setAlwaysOnTop: (flag) => ipcRenderer.send('always-on-top', flag),
});

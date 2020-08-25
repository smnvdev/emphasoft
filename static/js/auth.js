function popupWindow(url,  w, h) {
        const dualScreenLeft = window.screenLeft !==  undefined ? window.screenLeft : window.screenX;
        const dualScreenTop = window.screenTop !==  undefined   ? window.screenTop  : window.screenY;

        const width = window.innerWidth ? window.innerWidth : document.documentElement.clientWidth ? document.documentElement.clientWidth : screen.width;
        const height = window.innerHeight ? window.innerHeight : document.documentElement.clientHeight ? document.documentElement.clientHeight : screen.height;


        const systemZoom = width / window.screen.availWidth;
        const left = (width - w) / 2 / systemZoom + dualScreenLeft
        const top = (height - h) / 2 / systemZoom + dualScreenTop
        const newWindow = window.open(url, 'newwindow',
          `
          width=${w / systemZoom},
          height=${h / systemZoom},
          top=${top},
          left=${left},
          toolbar=no,
          location=no,
          directories=no,
          status=no,
          menubar=no,
          scrollbars=no,
          resizable=no,
          copyhistory=no,
          `
        )
        if (window.focus) newWindow.focus();
        setInterval(() => {
                if (localStorage.getItem("successAuth") !== null) {
                        localStorage.removeItem("successAuth")
                        newWindow.close();
                        window.location = '/';
                }
        }, 100)
    }
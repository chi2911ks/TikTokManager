var background = (function () {
  let tmp = {};
  /*  */
  chrome.runtime.onMessage.addListener(function (request) {
    for (let id in tmp) {
      if (tmp[id] && (typeof tmp[id] === "function")) {
        if (request.path === "background-to-page") {
          if (request.method === id) {
            tmp[id](request.data);
          }
        }
      }
    }
  });
  /*  */
  return {
    "receive": function (id, callback) {
      tmp[id] = callback;
    },
    "send": function (id, data) {
      chrome.runtime.sendMessage({
        "method": id, 
        "data": data,
        "path": "page-to-background"
      }, function () {
        return chrome.runtime.lastError;
      });
    }
  }
})();

var inject = function () {
  let config = {
    "random": {
      "value": function () {
        return Math.random();
      },
      "item": function (e) {
        let rand = e.length * config.random.value();
        return e[Math.floor(rand)];
      },
      "number": function (power) {
        let tmp = [];
        for (let i = 0; i < power.length; i++) {
          tmp.push(Math.pow(2, power[i]));
        }
        /*  */
        return config.random.item(tmp);
      },
      "int": function (power) {
        let tmp = [];
        for (let i = 0; i < power.length; i++) {
          let n = Math.pow(2, power[i]);
          tmp.push(new Int32Array([n, n]));
        }
        /*  */
        return config.random.item(tmp);
      },
      "float": function (power) {
        let tmp = [];
        for (let i = 0; i < power.length; i++) {
          let n = Math.pow(2, power[i]);
          tmp.push(new Float32Array([1, n]));
        }
        /*  */
        return config.random.item(tmp);
      }
    },
    "spoof": {
      "webgl": {
        "buffer": function (target) {
          let proto = target.prototype ? target.prototype : target.__proto__;
          //
          proto.bufferData = new Proxy(proto.bufferData, {
            apply(target, self, args) {
              let index = Math.floor(config.random.value() * args[1].length);
              let noise = args[1][index] !== undefined ? 0.1 * config.random.value() * args[1][index] : 0;
              //
              args[1][index] = args[1][index] + noise;
              window.top.postMessage("webgl-fingerprint-defender-alert", '*');
              //
              return Reflect.apply(target, self, args);
            }
          });
        },
        "parameter": function (target) {
          let proto = target.prototype ? target.prototype : target.__proto__;
          //
          proto.getParameter = new Proxy(proto.getParameter, {
            apply(target, self, args) {
              window.top.postMessage("webgl-fingerprint-defender-alert", '*');
              //
              if (args[0] === 3415) return 0;
              else if (args[0] === 3414) return 24;
              else if (args[0] === 36348) return 30;
              else if (args[0] === 7936) return "WebKit";
              else if (args[0] === 37445) return "Google Inc.";
              else if (args[0] === 7937) return "WebKit WebGL";
              else if (args[0] === 3379) return config.random.number([14, 15]);
              else if (args[0] === 36347) return config.random.number([12, 13]);
              else if (args[0] === 34076) return config.random.number([14, 15]);
              else if (args[0] === 34024) return config.random.number([14, 15]);
              else if (args[0] === 3386) return config.random.int([13, 14, 15]);
              else if (args[0] === 3413) return config.random.number([1, 2, 3, 4]);
              else if (args[0] === 3412) return config.random.number([1, 2, 3, 4]);
              else if (args[0] === 3411) return config.random.number([1, 2, 3, 4]);
              else if (args[0] === 3410) return config.random.number([1, 2, 3, 4]);
              else if (args[0] === 34047) return config.random.number([1, 2, 3, 4]);
              else if (args[0] === 34930) return config.random.number([1, 2, 3, 4]);
              else if (args[0] === 34921) return config.random.number([1, 2, 3, 4]);
              else if (args[0] === 35660) return config.random.number([1, 2, 3, 4]);
              else if (args[0] === 35661) return config.random.number([4, 5, 6, 7, 8]);
              else if (args[0] === 36349) return config.random.number([10, 11, 12, 13]);
              else if (args[0] === 33902) return config.random.float([0, 10, 11, 12, 13]);
              else if (args[0] === 33901) return config.random.float([0, 10, 11, 12, 13]);
              else if (args[0] === 37446) return config.random.item(["Graphics", "HD Graphics", "Intel(R) HD Graphics"]);
              else if (args[0] === 7938) return config.random.item(["WebGL 1.0", "WebGL 1.0 (OpenGL)", "WebGL 1.0 (OpenGL Chromium)"]);
              else if (args[0] === 35724) return config.random.item(["WebGL", "WebGL GLSL", "WebGL GLSL ES", "WebGL GLSL ES (OpenGL Chromium"]);
              //
              return Reflect.apply(target, self, args);
            }
          });
        }
      }
    }
  };
  //
  config.spoof.webgl.buffer(WebGLRenderingContext);
  config.spoof.webgl.buffer(WebGL2RenderingContext);
  config.spoof.webgl.parameter(WebGLRenderingContext);
  config.spoof.webgl.parameter(WebGL2RenderingContext);
  //
  // Note: this variable is for targeting sandboxed iframes
  document.documentElement.dataset.wgscriptallow = true;
};

let script_1 = document.createElement("script");
script_1.textContent = "(" + inject + ")()";
document.documentElement.appendChild(script_1);
script_1.remove();

if (document.documentElement.dataset.wgscriptallow !== "true") {
  let script_2 = document.createElement("script");
  //
  script_2.textContent = `{
    const iframes = [...window.top.document.querySelectorAll("iframe[sandbox]")];
    for (let i = 0; i < iframes.length; i++) {
      if (iframes[i].contentWindow) {
        if (iframes[i].contentWindow.WebGLRenderingContext) {
          iframes[i].contentWindow.WebGLRenderingContext.prototype.bufferData = WebGLRenderingContext.prototype.bufferData;
          iframes[i].contentWindow.WebGLRenderingContext.prototype.getParameter = WebGLRenderingContext.prototype.getParameter;
        }
        //
        if (iframes[i].contentWindow.WebGL2RenderingContext) {
          iframes[i].contentWindow.WebGL2RenderingContext.prototype.bufferData = WebGL2RenderingContext.prototype.bufferData;
          iframes[i].contentWindow.WebGL2RenderingContext.prototype.getParameter = WebGL2RenderingContext.prototype.getParameter;
        }
      }
    }
  }`;
  //
  window.top.document.documentElement.appendChild(script_2);
  script_2.remove();
}

window.addEventListener("message", function (e) {
  if (e.data && e.data === "webgl-fingerprint-defender-alert") {
    background.send("fingerprint", {
      "host": document.location.host
    });
  }
}, false);

import execjs

js_code = """
function v() {
return (
    (v = Object.assign
    ? Object.assign.bind()
    : function (e) {
        for (var t = 1; t < arguments.length; t++) {
            var r = arguments[t];
            for (var o in r)
            Object.prototype.hasOwnProperty.call(r, o) && (e[o] = r[o]);
        }
        return e;
        }),
    v.apply(this, arguments)
);
}
var U,
    B,
    G,
    H = function (e) {
        var t,
        r = [];
        if (void 0 === e) return "";
        t = (function (e) {
        for (var t, r = e.toString(), o = [], i = 0; i < r.length; i++)
            0 <= (t = r.charCodeAt(i)) && t <= 127
            ? o.push(t)
            : 128 <= t && t <= 2047
            ? (o.push(192 | (31 & (t >> 6))), o.push(128 | (63 & t)))
            : ((2048 <= t && t <= 55295) || (57344 <= t && t <= 65535)) &&
                (o.push(224 | (15 & (t >> 12))),
                o.push(128 | (63 & (t >> 6))),
                o.push(128 | (63 & t)));
        for (var a = 0; a < o.length; a++) o[a] &= 255;
        return o;
        })(e);
        for (var o = 0, i = t.length; o < i; ++o)
        r.push((5 ^ t[o]).toString(16));
        return r.join("");
    }
var V = function (e, t) {
    var r,
    o = 0,
    i = 0;
    if ("object" != typeof e) return e;
    if (!t || t.length <= 0) return e;
    for (
    var a = v(
        {
            mix_mode: o,
        },
        e
        ),
        n = 0,
        s = t.length;
    n < s;
    ++n
    )
    void 0 !== (r = a[t[n]]) && ((o |= 1), (i |= 1), (a[t[n]] = H(r)));
    return (a.mix_mode = o), (a.fixed_mix_mode = i), a;
}
var data = function(e) {
    var r = e.mobile
        , o = e.registerOnly
        , i = void 0 !== o && o
        , a = e.extra_params
        , n = V(v({
        mobile: r,
        type: i ? 16 : 24
    }, void 0 === a ? {} : a), ["mobile", "type"]);
    return n;
}
"""
data = {
    "extra_params": {
        "account_sdk_source": "web",
        "aid": 1459,
        "did": "7289460409617827346",
        "is6Digits": 1,
        "is_sso": False,
        "language": "vi",
        "mobile": "+84 332350491",
        "region": "VN",
    },
    "mobile": "+84 332350491",
}


context = execjs.compile(js_code)
result = context.call("data", data)
print(result)

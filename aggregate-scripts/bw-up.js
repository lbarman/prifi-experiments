var b3 = json2.groupBy(s => s._key)
var c = b3.map(obj => [obj[0]._key, _.map(obj, i => i.tp_up)])
var d = c.map(obj => [obj[0], stats(obj[1])])
var e = d.map(obj => _.flatten(obj))
var f = e.map(obj => list2Gnu(obj))
var h = f.value().join("\r\n")
out = h

var b3 = json2.groupBy(s => s.info)
var c = b3.map(obj => [obj[0].info, _.map(obj, i => i.duration_ns / parseFloat(1000000))])
var d = c.map(obj => [obj[0], stats(obj[1])])
var e = d.map(obj => _.flatten(obj))
var f = e.map(obj => list2Gnu(obj))
var h = f.value().join("\r\n")
out = h

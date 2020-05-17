var percentage = 0.3 // we get the latest 20% records

var b3 = json2.groupBy(s => s._key)

var res = {}

b3.forEach(function myFunction(objects, key) {
    var sortedObjects = _.sortBy(objects, function(el){ return parseInt(el.reportId); })
    var startIndex = objects.length-Math.ceil(percentage * objects.length)
    key = objects[0]._key
    res[key] = objects.slice(startIndex)
});

b4 = _.chain(res)

var c = b4.map(obj => [obj[0]._key, _.map(obj, i => i.duration_mean)])
var d = c.map(obj => [obj[0], stats(obj[1])])
var e = d.map(obj => _.flatten(obj))
var f = e.map(obj => list2Gnu(obj))
var h = f.value().join("\r\n")
out = h
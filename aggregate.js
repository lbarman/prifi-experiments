fs = require('fs')
_ = require('underscore');

var input = process.argv[2];
var script = process.argv[3];

if (typeof input === "undefined") {
    //console.log("Argument 1 need to be the input file");
    process.exit(0);
}
if (typeof script === "undefined") {
    //console.log("Argument 2 need to be the script file");
    process.exit(0);
}

if (!fs.existsSync(input)){
    //console.log("File", input, "does not exists/is not readable")
    process.exit(0);
}
if (!fs.existsSync(script)){
    //console.log("File", script, "does not exists/is not readable")
    process.exit(0);
}

//console.log("Gonna parse file", input, "using script", script);

fs.readFile(input, 'utf8', function (err,inputData) {
  if (err) {
    return console.log(err);
  }
  fs.readFile(script, 'utf8', function (err,scriptData) {
      if (err) {
        return console.log(err);
      }
      var parsedData = parseRaw(inputData);
      var json2 = _.chain(parsedData);
      eval("" + scriptData);
      console.log(out);
  });
});


function quotes(s) {
    return '"' + s + '"';
}

function list2Gnu(arr) {
    return arr.join(",\t")
}

function printSmth(smth) {
    if (typeof smth == 'string' || smth instanceof String) {
        return smth;
    } else if ($.isArray(smth)) {
        var builder = ""
        _.each(smth, function(i) {
            builder += printSmth(i) + "\n";
        });
        return builder.substring(0, builder.length - 1);
    } else {
        return JSON.stringify(smth);
    }
}

function parseRaw(data) {
    var parsed = formatRaw(data);
    if (!IsJsonString(parsed)) {
        return "Unable to parse";
    } else {
        return JSON.parse(parsed);
    }
}

function IsJsonString(data) {
    try {
        JSON.parse(data);
    } catch (e) {
        console.log(e)
        return false;
    }
    return true;
}

function formatRaw(data) {
    arrayOfLines = data.match(/[^\r\n]+/g)
    var jsonInner = _.chain(arrayOfLines).map(function(s) {
        return s.trim()
    }).filter(function(s) {
        return s.lastIndexOf('{', 0) === 0
    }).map(function(s) {
        return s.replace("},", "}")
    }).value().join(",")
    var json = "[" + jsonInner + "]"
    return json;
}

function stats(arr) {
    var m = Math.round(mean(arr))
    var v = Math.round(variance(arr))
    return [m, v];
}

function sum(x) {
    var value = 0;
    for (var i = 0; i < x.length; i++) {
        value += parseInt("" + x[i]);
    }
    return value;
}

function mean(x) {
    if (x.length === 0) return null;
    return sum(x) / x.length;
}

function min(x) {
    var value;
    for (var i = 0; i < x.length; i++) {
        if (x[i] < value || value === undefined) value = x[i];
    }
    return value;
}

function max(x) {
    var value;
    for (var i = 0; i < x.length; i++) {
        if (x[i] > value || value === undefined) value = x[i];
    }
    return value;
}

function variance(x) {
    if (x.length === 0) return null;
    var mean_value = mean(x),
        deviations = [];
    for (var i = 0; i < x.length; i++) {
        deviations.push(Math.pow(x[i] - mean_value, 2));
    }
    var std = mean(deviations);
    var sterr = Math.sqrt(std)
    var z_value_95 = 1.96
    var margin_error = sterr * z_value_95
    return margin_error;
}

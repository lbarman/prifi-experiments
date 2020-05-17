var percentage = 0.3 // we get the latest X% records corresponding to the steady-state
var minRecordsToKeep = 10 // if X > percentage * nRecords, keep X instead
var nBestRuns = 5 // we get only the most stable X runs

var b3 = json2.groupBy(s => s._key)

var bestRunsAndMeans = {}

// for each _key (which is: number of clients, or window)
b3.forEach(function myFunction(objects, key) {

    var objects2 = _.chain(objects)

    // group the objects by "run" or repetition of the experiment
    var groupedPerRun = objects2.groupBy(s => s._key2)

    var runs = {}

    // for each "run" or repetition of the experiment
    groupedPerRun.forEach(function myFunction(objectsOfThisRun, key) {

        //sort the object by ID to keep only the steady-state at the end
        var sortedObjects = _.sortBy(objectsOfThisRun, function(el){ return parseInt(el.reportId); })

        // keep either percentage or minRecordsToKeep, whatever is higher
        var nToKeep = Math.ceil(percentage * objectsOfThisRun.length);
        if(nToKeep < minRecordsToKeep) {
            nToKeep = minRecordsToKeep;
        }

        var startIndex = objectsOfThisRun.length-nToKeep;
        if (startIndex < 0) {
            startIndex = 0;
        }

        var steadyStateObjects = objectsOfThisRun.slice(startIndex)

        // now keep only the statistics
        var meanOnly = steadyStateObjects.map(s => parseFloat(s.duration_mean))

        key = objectsOfThisRun[0]._key2
        runs[key] = { key: key, data: meanOnly}
    });

    var runsAndStats = _.map(runs, obj => [obj.key, stats(obj.data)])

    var sortedRuns = _.sortBy(runsAndStats, function(run){ return run[1][1]; })

    var nRunsToKeep = nBestRuns;
    if  (sortedRuns.length < nRunsToKeep) {
        nRunsToKeep = sortedRuns.length
    }

    var bestRuns = sortedRuns.slice(0, nRunsToKeep)

    var bestRunsMeans = bestRuns.map(run => run[1][0]);

    key = objects[0]._key
    bestRunsAndMeans[key] = bestRunsMeans
});

var d = _.map(bestRunsAndMeans, (obj, key) => [key, stats(obj)])
var e = d.map(obj => _.flatten(obj))
var f = e.map(obj => list2Gnu(obj))
var h = f.join("\r\n")
out = h
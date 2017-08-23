

// var config = require('./config')

var AWS = require('aws-sdk');

var uuid = require('node-uuid');
var fs = require('fs-extra');
var path = require('path');
// var FileReader = require('FileReader');

// AWS.config.region = config.region;
var rekognition = new AWS.Rekognition({region: 'us-west-2'});


function deleteCollection(){
rekognition.deleteCollection({CollectionId: 'facematching'}, function(err,data){


    if(err){
        console.log('error  in delete colelction', err);
    } else {
        console.log('returned deletions', data);
    }
})
}
// AWS allows you to create separate collections of faces to search in.
// This creates the collection we'll use.
function createCollection() {
	// Index a dir of faces
	rekognition.createCollection( { "CollectionId": 'facematching' }, function(err, data) {
	  if (err) {
		console.log('errorrr creatng collection', err); // an error occurred
	  } else {
		console.log('data is ', data);           // successful response
	  }
	});
}


// This loads a bunch of named faces into a db. It uses the name of the image as the 'externalId'
// Reads from a sub folder named 'faces'
function indexFaces() {
	var klawSync = require('klaw-sync')
	var paths = klawSync('./faces', { nodir: true, ignore: [ "*.json" ] });

	paths.forEach((file) => {
		// console.log(file.path);
		var p = path.parse(file.path);
		var name = p.name.replace(/\W/g, "");
		var bitmap = fs.readFileSync(file.path);

		rekognition.indexFaces({
		   "CollectionId": "facematching",
		   "DetectionAttributes": [ "ALL" ],
		//    "ExternalImageId": name,
		   "Image": {
			  "Bytes": bitmap
		   }
		}, function(err, data) {
			if (err) {
				console.log(err, err.stack); // an error occurred
			} else {
				console.log(data);           // successful response
				fs.writeJson(file.path + ".json", data, err => {
					if (err) return console.error(err)
				});
			}
		});
	});
}

// Once you've created your collection you can run this to test it out.
// function FaceSearchTest(imagePath)
// {
// 	var bitmap = fs.readFileSync(imagePath);
//
// 	rekognition.searchFacesByImage({
// 		"CollectionId": collectionName,
// 		"FaceMatchThreshold": 80,
// 		"Image": {
// 			"Bytes": bitmap,
// 		},
// 		"MaxFaces": 1
// 	}, function(err, data) {
// 		if (err) {
// 			console.log(err, err.stack); // an error occurred
// 		} else {
// 			console.log(data);           // successful response
// 			console.log(data.FaceMatches[0].Face);
// 		}
// 	});
// }

// This uses the detect labels API call on a local image.
// function DetectLabelsTest(imagePath)
// {
// 	var bitmap = fs.readFileSync(imagePath);
//
// 	var params = {
// 		Image: {
// 			Bytes: bitmap
// 		},
// 		MaxLabels: 10,
// 		MinConfidence: 50.0
// 	};
//
// 	rekognition.detectLabels(params, function(err, data) {
// 		if (err) {
// 			console.log(err, err.stack); // an error occurred
// 		} else {
// 			console.log(data);           // successful response
// 		}
// 	});
// }
deleteCollection();
createCollection();
indexFaces();
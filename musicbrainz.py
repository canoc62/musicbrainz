import musicbrainzngs
import json

musicbrainzngs.set_useragent(
	"musicbrainz-practice",
	"0.1",
	"canoc4262@gmail.com"
)

artist_list = {
	"artist_list": [

	]
}

artist_object = {
	"meta": {

	},

	"album_list": [

	]
}

#Coldplay
artist_id = "cc197bad-dc9c-440d-a5b5-d52ba2e14234"
#Eminem
single_artist_id = "b95ce3ff-3d05-4e87-9e01-c97b66af13d4"

artist_query = musicbrainzngs.get_artist_by_id(
	single_artist_id, 
	includes=['artist-rels', 'release-groups']
)
#print("ARTIST: ", artist_query)

#The Marshall Mathers LP (For Testing and Viewing Python Dict)
album_id = "b1fdc9cc-8680-44da-abab-59edca6b2ad3"
album2_id = "1dc4c347-a1db-32aa-b14f-bc9cc507b843"
album_query = musicbrainzngs.get_release_group_by_id(
	album2_id, 
	includes=['label-rels', 'ratings'],
	#release_status=['official'], 
	#release_type=['album']
)
print("ALBUM: ", album_query)


artist_name = artist_query["artist"]["name"]

# Get members through artist id query
members_of_group = []
if artist_query['artist']['type'] == 'Group':
	for member in artist_query['artist']['artist-relation-list']:

		if member['type'] == 'member of band':
			members_of_group.append(member['artist']['name'])
	print("Members of group: ", members_of_group)
else:
	for member in artist_query['artist']['artist-relation-list']:

		if member['type'] == 'is person':
			members_of_group.append(member['artist']['name'])
	print("Members of group: ", members_of_group)


releases = artist_query['artist']['release-group-list']

album_list = []
for release in releases:
		
		if release['type'] == 'Album' :
			#can get album id to get more info
			album = {
				"name": release['title'],
				"label": "",#release['label'],
				"release_date": ""
			}
			artist_object["album_list"].append(album)

meta = {
	"name": artist_name,
	"members": members_of_group
}
artist_object["meta"].update(meta)


artist_list["artist_list"].append(
	artist_object
)


artists_file = '%s.json' %(artist_name)
f = open(artists_file, 'w')
f.write(json.dumps(artist_list, indent=4, sort_keys=False))
f.close()





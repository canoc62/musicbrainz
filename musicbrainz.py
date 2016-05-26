import musicbrainzngs
import json

musicbrainzngs.set_useragent(
	"musicbrainz-practice",
	"0.1",
	"canoc4262@gmail.com"
)

#Coldplay
artist_id = "cc197bad-dc9c-440d-a5b5-d52ba2e14234"
#Eminem
single_artist_id = "b95ce3ff-3d05-4e87-9e01-c97b66af13d4"

artist_query = musicbrainzngs.get_artist_by_id(single_artist_id, includes=['artist-rels', 'release-groups'])
print("ARTIST: ", artist_query)


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

artist_name = artist_query["artist"]["name"]
print("Artist: {artist}".format(artist=artist_query['artist']["name"]))


meta = {
	"name": artist_name,
	"members": members_of_group
}
artist_object["meta"].update(meta)



releases = musicbrainzngs.browse_release_groups(
	artist=single_artist_id,
	limit=20,
	#release_status=['official'],
	release_type=['album']
)
#print(releases)
album_list = []


for release in releases['release-group-list']:
		
		if release['type'] == 'Album':
			#can get album id to get more info
			album = {
				"name": release['title'],
				"label": "",#release['label'],
				"release_date": "",
				"cover-art": ""
			}
			artist_object["album_list"].append(album)


artist_list["artist_list"].append(
	artist_object
)


'''
releases = musicbrainzngs.browse_releases(
	artist=artist_query['id'],
	format='CD',
	limit=2000, 
	release_status=['official'],
	release_type=['album']
)

album_list = []

for release in releases['release-list']:
	album_list.append("Album: {title}".format(title=release['title']))

for release in set(album_list):
	print(release)
'''

'''
recordings = musicbrainzngs.search_recordings(
	arid=artist['id'],
	format='CD',
	primarytype='album',
	limit=5000
)


album_list = []

for recording in recordings['recording-list']:
	album_list.append("Album: {title}".format(title=recording['title']))

for recording in set(album_list):
	print(recording)
'''

artists_file = '%s.json' %(artist_name)
f = open(artists_file, 'w')
f.write(json.dumps(artist_list, indent=4, sort_keys=False))
f.close()





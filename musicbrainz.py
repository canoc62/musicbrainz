import musicbrainzngs
import json

def check_for_official_album(album_release_list):
	for release_list in album_release_list:
		if release_list['status'] == 'Official':
			return True
	return False

def check_for_release_event_list(album_release_list):
	pass

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
album3_id = "73ccdc34-3877-4509-9d82-8a6fe9941957"#Whiteboy Wasted
album4_id = "715be5e7-3677-35c0-a39a-abf300ff9ba1" #Infinite
album5_id = "67e94a91-f48e-3e59-9701-38a4dba28d0b" #ReUp
album6_id = "ab7577c4-641d-49ad-ab02-cef742f7dea2" #Collision Course 3
album_query = musicbrainzngs.get_release_group_by_id(
	album4_id, 
	includes=['label-rels', 'ratings', 'releases']#, 'release-rels']
)
print("ALBUM: ", album_query)


artist_name = artist_query["artist"]["name"]

# Get members through artist id query
members_of_group = []
if artist_query['artist']['type'] == 'Group':
	for member in artist_query['artist']['artist-relation-list']:

		if member['type'] == 'member of band':
			members_of_group.append(member['artist']['name'])
	#print("Members of group: ", members_of_group)
else:
	for member in artist_query['artist']['artist-relation-list']:

		if member['type'] == 'is person':
			members_of_group.append(member['artist']['name'])
	#print("Members of group: ", members_of_group)


releases = artist_query['artist']['release-group-list']

album_list = []
for release in releases:
		
		if release['type'] == 'Album':
			album_info = musicbrainzngs.get_release_group_by_id(
				release['id'], 
				includes=['releases']
			)
			
			#album_status = album_info['release-group']['release-list'][0]['status']
			album_release_list = album_info['release-group']['release-list']
			if check_for_official_album(album_release_list) == True:# and :
				album = {
					"name": release['title'],
					"release_date": release['first-release-date']
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

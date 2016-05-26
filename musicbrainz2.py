import musicbrainzngs
import json

musicbrainzngs.set_useragent(
	"musicbrainz-practice",
	"0.1",
	"canoc4262@gmail.com"
)

#Coldplay (Will have to get artist id in the first place somehow)
artist_id = "cc197bad-dc9c-440d-a5b5-d52ba2e14234"
artist_query = musicbrainzngs.get_artist_by_id(artist_id, includes=['artist-rels'])
print("ARTIST: ", artist_query)

#Eminem
single_artist_id = "b95ce3ff-3d05-4e87-9e01-c97b66af13d4"
single_artist_query = musicbrainzngs.get_artist_by_id(single_artist_id, includes=['artist-rels'])
print("SINGLE ARTIST: ", single_artist_query)

#Can get by browsing for release_groups through artist musicbrainz artist id
release_group_id = "120c786d-a3b2-3c19-b4ff-2b7b3b4435bf"
release_group_query = musicbrainzngs.get_release_group_by_id(release_group_id)
#print("RELEASE GROUP", release_group_query)

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
#print("Artist: {artist}".format(artist=artist_query['artist']["name"]))


# Get members through release group query
members = musicbrainzngs.browse_artists(
	release_group=release_group_id,
	includes=["artist-rels"]
)
#print("MEMBERS: ", members)

members_of_group = []


#for group in members['artist-list']:#['artist-relation-list']:

#	for artist in group['artist-relation-list']:
#		if artist['type'] == 'member of band':
#			members_of_group.append(artist['artist']['name'])


for artist in members['artist-list'][0]['artist-relation-list']:

	#for artist in group['artist-relation-list']:
	if artist['type'] == 'member of band':
		members_of_group.append(artist['artist']['name'])
print(members_of_group)





# Get members through artist id query
members_of_group2 = []
for member in artist_query['artist']['artist-relation-list']:

	if member['type'] == 'member of band':
		members_of_group2.append(member['artist']['name'])
print("Members of group: ", members_of_group2)









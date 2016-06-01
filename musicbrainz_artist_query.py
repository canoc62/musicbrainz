import musicbrainzngs
import json

def musicbrainz_set_user(email):
    user = musicbrainzngs.set_useragent(
        "musicbrainz-practice",
	   "0.1",
	   email
    )	
    return user


def query_artist(artist_id):

    def check_for_official_album(album_release_list):
        for release_list in album_release_list:
            if release_list['status'] == 'Official':
                return True
        return False

    artist_query = musicbrainzngs.get_artist_by_id(
        artist_id, 
        includes=['artist-rels', 'release-groups']
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

    artist_name = artist_query["artist"]["name"]

    # Get members through artist id query
    members_of_group = []
    if artist_query['artist']['type'] == 'Group':
        for member in artist_query['artist']['artist-relation-list']:

            if member['type'] == 'member of band':
                members_of_group.append(member['artist']['name'])
    else:
        for member in artist_query['artist']['artist-relation-list']:

            if member['type'] == 'is person':
                members_of_group.append(member['artist']['name'])

    # Get albums through the release group relationship
    releases = artist_query['artist']['release-group-list']

    album_list = []
    for release in releases:
        
            if release['type'] == 'Album':
                album_info = musicbrainzngs.get_release_group_by_id(
                    release['id'], 
                    includes=['releases']
                )
            
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

actor_dict = {}

def cast_as_list( g ):
    if type(g) is str:
        return g.split('|')
    return []

for index, row in data.iterrows():
    for g in cast_as_list(row.cast):
        actor_dict[ g ] = actor_dict.get( g, [] ) + [ row.imdb_id ]

act_imdb_id  = []
act_name = []
for g,imdb_ids in actor_dict.items():
    for imdb_id in imdb_ids:
        act_name.append( g )
        act_imdb_id.append( imdb_id )

actors = pd.DataFrame( {"actor": act_name, "imdb_id": act_imdb_id} )
actors
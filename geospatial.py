def get_affected_regions(disaster):
    # Later use geospatial data
    regions = {
        'flood': ['Region A', 'Region B'],
        'earthquake': ['Region C'],
        'cyclone': ['Region D', 'Region E']
    }
    return regions.get(disaster, [])

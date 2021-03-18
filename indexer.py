# Method to Index Stations:
# This method is important because we can search the array only by using numbers(not Station Names).
# The AIM of this method is to give index to each station:
def indexer(station):
    dict={
        'Pune':0,
        'Shivajinagar':1,
        'Khadki':2,
        'Dapodi':3,
        'Kasarwadi':4,
        'Pimpri':5,
        'Chinchwad':6,
        'Akurdi':7,
        'Dehu-Road':8,
        'Begdewadi':9,
        'Ghorawadi':10,
        'Talegaon':11,
        'Vadgaon':12,
        'Kanhe':13,
        'Kamshet':14,
        'Malavli':15,
        'Lonavala':16
    }

    # dict={
    #     'Virar':0,
    #     'Vasai':1,
    #     'Borivali':2,
    #     'Kandivali':3,
    #     'Malad':4,
    #     'Goregaon':5,
    #     'Andheri':6,
    #     'Santazruz':7,
    #     'Airport':8,
    #     'Bandra':9,
    #     'Dadar':10,
    #     'Mumbai Central':11,
    #     'Marine Lines':12,
    #     'Churchgate':13,
    #     'CSMT':14,
    #     'Kurla':15,
    #     'Thane':16,
    #     'Vashi':17,
    #     'Panvel':18,
    #     'Dombivali':19,
    #     'Kalyan':20,
    #     'Badlapur':21,
    #     'Karjat':22,
    #     'Khopoli':23
    # }

    return dict[station]
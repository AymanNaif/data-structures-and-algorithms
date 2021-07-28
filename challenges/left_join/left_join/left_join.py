from .hash_table import HashTable


def left_join(hash_table_one, hash_table_two):

    lists = []
    for item in hash_table_one:
        if item:

            i = 0
            curr_item = item[i]

            while curr_item:

                key = curr_item[0]

                if hash_table_two.contains(key):
                    lists.append([key, curr_item[1], hash_table_two.get(key)])

                else:
                    lists.append([key, curr_item[1], None])
                try:
                    if item[i+1]:
                        i += 1
                        curr_item = item[i]
                    else:
                        curr_item = None
                except:
                    break

    return lists

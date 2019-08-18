def has_permission(page):
    def inner(username):
        if username == 'Admin':
            return "'{0}' does have access to {1}.".format(username, page)
        else:
            return "'{0}' does NOT have access to {1}.".format(username, page)

    def inner_2(username_2):
        return username_2

    if 1 > 0:
        return inner
    else:
        return inner_2


a = has_permission('Admin Area')
b = a('inner')
c = b('inner-2')
print(b)


# random_user = has_permission('Admin Area')
# print(random_user('Not Admin'))
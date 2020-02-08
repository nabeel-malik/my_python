def _remove_comments(clear_comments, tmp_in):
    """
    Remove comments, when needed, in the tmp_in string.
    In-line comments will not be removed.

    :param clear_comments: Boolean describing whether to remove comments.
    :param tmp_in: String of text to remove Eclipse comments.
    :return: tmp_in or tmp_in without comments depending on clear_comments
    """
    tmp_out = tmp_in
    if clear_comments:
        if "--" in tmp_out:
            tmp_out = "%s\n" % tmp_out.split("--")[0]
    return tmp_out


str1 = '-- 2 regions '
str2 = "'include/CASE_70_PROP_FIPNUM.GRDECL' / "
str3 = "INCLUDE                                -- Generated : Petrel "
str4 = "'include/CASE_70_PROP_FIPNUM.GRDECL' / -- dummy "

print(_remove_comments(True, str1))
print(_remove_comments(True, str2))
print(_remove_comments(True, str3))
print(_remove_comments(True, str4))
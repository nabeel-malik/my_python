
read_file = 'work_directory/remove_comments/lgr_0skin'

with open(read_file, 'r') as rf:
    with open(read_file + '_comments_removed', 'w+') as wf:
        for line in rf:
            if line.startswith('-- Perforation Completion :') or line.startswith('-- ----'):
                pass
            else:
                wf.write(line)

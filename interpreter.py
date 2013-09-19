# Parses arguments and commands

# <msg "foo bar, foo foo bar"> will add the note "foo bar, foo foo bar"
# to the default category: "todo".

# <msg -c "shopping list" "foo bar, foo foo bar"> will add the note
# "foo bar, foo foo bar" to the "shopping list" category.


# <msg -e "doomsday commands" "foo bar, foo foo bar"> will add the
# note "foo bar, foo foo bar" to the "doomsday commands" category
# and mark "doomsday commands" as an executable category

# <msg -x "dommsday commands"> will execute the commands in the
# "doomsday commands" category.


# <msg -d "useless"> will delete everything in the "useless" category

# <msg -p "useful"> will dump(print) everything in the "useful" category




# IDEAS: TODO: filtered printing

def interpreter():
    parser = argparse.ArgumentParser(description='msg is a todo-list and
    procrastination manager')

    parser.add_argument("category", help = "CATEGORY is the category of
    messages in use")



    main_commands = parser.add_mutually_exclusive_group()

    main_commands.add_argument("-p", "--print", help = "Use PULL to dump
    or print all messages from an existing category", action = "store_true")

    main_commands.add_argument("-d", "--delete", help = "Use DELETE to
    delete a category")

    parser.add_argument("-e", "--exec", help = "Use EXECUTABLE to mark
    the message as executable", action = "store_true")

    parser.add_argument("x", "--execute", help = "Use EXECUTE to execute
    the commands in the file", action = "store_true")


    return parser

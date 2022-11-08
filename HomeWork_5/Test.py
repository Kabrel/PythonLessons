import cursesmenu

menu = cursesmenu.CursesMenu("This is a menu!", "It has a subtitle too!")

command_item = cursesmenu.items.CommandItem("Run a console command", "touch hello.txt")

function_item = cursesmenu.items.FunctionItem("Call a function", input, ["Enter some input"])

submenu = cursesmenu.CursesMenu("This is the submenu")

submenu.items.append(command_item)
submenu.items.append(function_item)
submenu_item = cursesmenu.items.SubmenuItem("Show a submenu", submenu, menu=menu)



menu.items.append(submenu_item)


menu.show()

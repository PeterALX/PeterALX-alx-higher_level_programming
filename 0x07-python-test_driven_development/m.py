add = __import__("0-add_integer").add_integer
divmat = __import__("2-matrix_divided").matrix_divided
say_name = __import__("3-say_my_name").say_my_name
print_square = __import__("4-print_square").print_square
text_indentation = __import__("5-text_indentation").text_indentation
print()


#add_integer
print(r"##add integer")
a = add(3.35,4.5)
print(a)
print()


#matrix_divided
list = [[2,4,6],[2,4,8]]
print("##matrix_divided")
divlist = divmat(list, 2)
print(divlist)
print()

#say_my_name
print("##say_my_name")
say_name("Peter", "Kioko")
print()

#print_square
print("##print_square")
print_square(5)
print()
print_square(9)
print()

#text_indentation
print("##text_indentation")
text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres")



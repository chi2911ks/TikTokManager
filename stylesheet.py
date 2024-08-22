class StyleSheet:

    QMenu = """
QMenu {
    border: 1px solid rgb(40, 44, 90);
    border-radius: 4px;
    padding: 4px;
    background-color: rgb(40, 44, 52);
    color: white;
    
}
QMenu::item:selected {
    background-color: rgba(196, 167, 231, 0.5);
    color: white;
}         """
    QPushButton = '''QPushButton {
	border: 2px solid %s;
	border-radius: 5px;	
	background-color: %s;
}
 QPushButton:hover {
	background-color: %s;
	border: 2px solid %s;
}
 QPushButton:pressed {	
	background-color: %s;
	border: 2px solid %s;
}'''
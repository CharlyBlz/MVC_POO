from contactos_view import ContactoNuevo, ContactosView

class ContactosController(object):
    def __init__(self, repo, view):
        self.selection = None
        self.view = view
        self.repo = repo
        self.contacts = list(repo.get_contacts())
        




    def create_contact(self):
        print("Función create_contact")
        nuevo_contacto = ContactoNuevo(self.view).show()
        if nuevo_contacto:
            contact = self.repo.add_contact(nuevo_contacto)
            self.contacts.append(contact)
            self.view.add_contact(contact)

    def start(self):
        # 15 método iterador para mostrar los contactos, actualizar la lista
        self.view.mainloop()
        for c in self.contacts:
            self.view.add_contact(c)
        self.view.mainloop()

    def select_contact(self, index):
        self.selection = index
        contact = self.contacts[index]
        self.view.load_details(contact)

    # 6 Agregar métodos al controller
    def update_contact(self):
        if not self.selection:
            return
        rowid = self.contacts[self.selection].rowid
        update_contact = self.voew.get_data()
        update_contact.rowid = rowid
        contact = self.repo.update_contact(update_contact)
        self.contacts[self.selection] = contact
        self.view.update_contact(contact, self.selection)
        print("Función update_contact")

    def delete_contact(self):
        print("Función delete_contact")
        if not self.selection:
            return
        contact = self.contacts[self.selection]
        self.repo.delete_contact(contact)
        self.view.remove(self.selection)
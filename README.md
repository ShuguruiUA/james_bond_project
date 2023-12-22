# JAMES-BOND-ASSISTANT

Персональний помічник cправжнього агенту ;)

Дозволяє робити, змінювати та шукати нотатки та записи в записній та адресній книзі.
Зберігає дані після введеня команди або виходу з програми, при запуску програми дані відновлюються.
Додаткова функція clean-folder допоможе навести лад у вашій папці з несортованим файлами.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [License](#license)

## Install

This project uses [Python 3.10](https://www.python.org/). Go check them out if you don't have them locally installed.

Required dependencies:
[prompt-toolkit 3.0.43](https://rich.readthedocs.io/en/stable/index.html)
[rich 13.7.0](https://python-prompt-toolkit.readthedocs.io/en/master/)


Download all files.
Requires pip to install.

```sh
$ pip install [folder path setup.py]
$ pip install -i https://test.pypi.org/simple/ james-bond-assistant
```



## Usage

Console script.

Command for start script:

```commandline
    007-assistant
```

Commands:

```sh
  For work with address book:
    create-contact - create a new contact. Required data = name, phone, birthday. Additional = email, address
    add-phone - add additional phone for existing contact
    add-email - add/change email address for existing contact
    add-birthday - add/change birthday for existing contact
    add-address - add/change address for existing contact
    edit-phone - change for number for existing contact
    show-contacts - show all contacts in address book
    find-record - searching for records in address book by contact name
    find-phone - looking for phone number in the address book if exists return all data for the contact
    remove-phone - remove phone number from the existing record
    delete-contact - delete record from address book
    uncoming-birthdays - shows days to birthday by period setted by user, by default 7 days
  For work with note book:
    create-note - create new note. Requires note title, note data, at least one tag, for exiting from adding tag please put 'e'
    edit-note - allowed user to change note data in existing note by title
    show-notes - shows all available notes
    find-tag - searching for note by its tag, return table of notes with this tag
    delete-note - delete note user should input note title
  For work with data:
    save-data - saving data for address and note books
    load-data - loading data for address and note books

  Additional functionality:
    clean-folder - Some useful function to cleanup mess in yours "trash" folder

  For exit:
    exit
    quit
    
    
  
```

## License

[MIT](LICENSE) ©   Daryna, Serhii, Svitlana, Khrystyna, Iurii

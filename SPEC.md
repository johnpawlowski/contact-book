# Contact Book

> A Python CLI application for managing a book of contacts with add, remove, update, search, and list view capabilities.

## What it does
Implements a `ContactBook`, `Record`, `Contact(Record)`, and `Address` classes, as well as custom error classes, with an interactive CLI that allows users to create and manage multiple contacts. Demonstrates advanced OOP including inheritance, composition, property decorators, and custom error handling.


## Inputs
- Contact Name (string) provided at contact creation
- Contact Email (string) provided at contact creation
- Contact Address (obj) instantiated at contact creation with Street (string), City (string), and Country (string) as arguments
- Contact Phone (string) provided at contact creation
- Menu selections (integer) for navigating the CLI

## Outputs
- User-facing messages when contacts added, updated, or removed
- Full contact list via `ContactBook.list()`
- Individual contact cards via `ContactBook.summary()`

## Success criteria
- Contacts can be added, updated, and removed
- Duplicate emails rejected before collecting further input
- Invalid fields rejected on update with descriptive error
- Contact state persists across sessions via JSON save file
- Original creation timestamp preserved on reload
- All errors handled with clear user-facing messages
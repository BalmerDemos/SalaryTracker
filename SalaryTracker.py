"""Add for precision in salary calculation."""
from decimal import *
import math

"""Define two dictionaries to store user information to
   facilitate program execuation logic.
"""

empleados = {}
"""Stores whether the emploee received their incrment or not."""
old_empleados = {}


"""Message declaration section, it faciliate the use of message
during the program execuation in case that the same message used
also keep a better order in case other developer sees your code."""

def msg_welcome():
  print("\n")
  print("--------------------------------------------")
  print("PROJECT:  Demo with menus and use of dictioany.    ")
  print("AUDIENCE: Open to comunity.                         ")
  print("AUTHOR:   BalmerDemos                               ")
  print("--------------------------------------------")

"""User will be inform when exiting the program.."""
def msg_goodbye():
  print("\n")
  print("--------------------------------------------")
  print("     Exiting the payroll progam.NA          ")
  print("--------------------------------------------")

def msg_list_empleados():
  print("\n")
  print("--------------------------------------------")
  print("          Employee Report                   ")
  print("--------------------------------------------")

def  msg_buscar_empleados():
  print("\n")
  print("--------------------------------------------")
  print("            Find Employee                   ")
  print("--------------------------------------------")

def msg_create_empleado():
  print("\n")
  print("--------------------------------------------")
  print("          Create Employee Menu              ")
  print("--------------------------------------------")

def msg_contiuar_capturas():
  print("\n")
  print("--------------------------------------------")
  print("           Please continue with             ")
  print("          employee data capture             ")
  print("          could you exit when desired.      ")
  print("--------------------------------------------")

def msg_processing():
  print("\n")
  print("--------------------------------------------")
  print("        Saving employee information .....   ")
  print("--------------------------------------------")

def msg_completed():
  print("\n")
  print("--------------------------------------------")
  print("     ......Saving employee completed        ")
  print("--------------------------------------------")

def msg_sin_datos():
  print("\n")
  print("--------------------------------------------")
  print("       You did not enter any valueOR        ")
  print("       Plese enter a emploey name           ")
  print("       to continue.                         ")
  print("--------------------------------------------")

def msg_error_name_numerico():
  print("\n")
  print("--------------------------------------------")
  print("       You entered a numeric valueO         ")
  print("       PLease enter a employee name         ")
  print("       to continue.                         ")
  print("--------------------------------------------")

def msg_salario_invalido():
  print("\n")
  print("--------------------------------------------")
  print("       You have not enter a correct value   ")
  print("       Please enter a employee salary       ")
  print("       to continue.                         ")
  print("--------------------------------------------")

def msg_salario_negativo():
  print("\n")
  print("--------------------------------------------")
  print("       You entered a value <= cero          ")
  print("       Please enter a employee salary       ")
  print("       to continue.                         ")
  print("--------------------------------------------")

def msg_no_records():
  print("\n")
  print("--------------------------------------------")
  print("       There is not data                    ")
  print("       the employees database               ")
  print("       Please enter employee data           ")
  print("       to continue.                         ")
  print("--------------------------------------------")

def menu_():
  print("\n")
  print("--------------------------------------------")
  print("     Queries and user createion menu.       ")
  print("--------------------------------------------")


"""End message section."""

"""Function to validate if the user entered a blank value
for the employee name, or if the user entered a numeric
value for the name. It will return false if name is blank
or a full numeric value, this version does not handle
alfanumeric values, please implement it."""
def validate_name(emp_name):
  if len(emp_name) <= 0:
    msg_sin_datos()
    return False
  elif emp_name.isnumeric():
    msg_error_name_numerico()
    return False
  else:
    return True


"""Funcion to validate if the salary is cero or blank.
an employee will not earn cero amount for services."""
def validar_salario(emp_salario):
  if emp_salario.isnumeric() != True:
    msg_salario_invalido()
    return False
  elif float(emp_salario) <= 0:
    msg_salario_negativo()
    return False
  else:
    return True


"""Fucntio to capture and valdiate employee data entered
by the user."""
def create_empleado():
    is_create = True
    while is_create:
      is_name = False
      while is_name != True:
        emp_name = input("\nPlease enter the employee name: ")
        is_name = validate_name(emp_name)

      is_salario = False
      while is_salario != True:
        emp_salario = input("\nPlease enter the employee salary: ")
        is_salario = validar_salario(emp_salario)

      """Data is valid, we can store the employee informaiton. Salary with which it was initially created."""
      """The increase of 10% to wages < 2'000,000 will be make duing the sub process to show employee."""
      """Valdiate if the salary is less than 2000000 and make the 10% increase and save the new salary."""


      emp_salario = int(emp_salario) # Cast the user input, string to interger and store it.
      empleados[emp_name] = emp_salario

      print("Do you want to continue with another user?\n",
       "1. Yes\n",
       "2. No\n")
      user_input = input("Please enter your option to continue: ")
      is_create = validar_input_continuar(user_input)



# FUNCION PARA VALIDAR INGRESO DE USUARIO
"""Function to validate of the user want to enter to the program,
it will give the feeling of login into app. """
def validar_input_continuar(user_input):
  try:
    val = int(user_input)
    # 1 and create
    if val == 1:
      return True # it continues to the main menu.
    elif val == 2:
      return False
    else:
      print("\nPlesae enter 1 or 2 to continue only!")
      return True
  except  Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    return True


"""Function to search for an employ and determina if the user has a increment or not.
here we will make a calculation base on the salary with increment, in other works
find the real salary, and provide details about increment."""
def buscar_empleado():
  nom_empleado = input("\nPlesae enter the employee name to find: ")
  try:
    salario = int(empleados.get(nom_empleado))

    """We need to know if the starting salary was less thatn 2000000.
       so we remove the 10% of the current salary and valdiate the salary."""

    if salario >= 2000000:
      print("--------------- " + nom_empleado + " Employees with salaies over 2000000 have not changes in their salaris.")
      print("--------------- Basic salary:        " + str(math.ceil(salario)))
      print("--------------- Your increase 0%:    " + str(0))
      print("--------------- Increased salary:    " + str(salario) + "\n")
    else:
      salario_basico = salario / 1.1
      incremento = salario - math.ceil(salario_basico)
      if salario_basico < 2000000:
        print("--------------- " + nom_empleado + " Employees with salary less than 2000000 have changes in their salaries.")
        print("--------------- Basic salary:          " + str(math.ceil(salario_basico)))
        print("--------------- Your increase 10%:     " + str(incremento))
        print("--------------- Increased salary:      " + str(salario) + "\n")
  except:
    print("\n----- No data was found in the employee record\n----- Please enter an employee for queries.\n")


"""Function to generate a report with changes in employees's salaries"""
"""Criterion salaries less than 2 million receive increase only."""
def reporte_nuevos_empleados():
  print("\n")
  for nombre, salario in empleados.items():
    print("Employee:   " + nombre + " Basic salary: " + str(salario) + "\n")

    """Validate if the employee is former or not to increase your salary, you should only increase one time."""
    """Recieve increase during employee creation."""
    status = old_empleados.get(nombre)
    if status == None:
      """We need to make an increase if the salary is less thatn 2000000 and update the new salary."""
      if salario < 2000000:
        incremento = salario * 0.10
        print("Its increase is:             " + str(incremento))
        salario += incremento
        print("Your increase salary is:"      + str(salario) + "\n")
        empleados.update({nombre:salario})

        """We need to know if the employee is former in order to not increae his salary again."""
        """We use the second dictionary and we set a string value which can later use as a flag
        the true or false at the end with a slip (_)."""
        old_empleados[nombre] = "INCREMENTO_TRUE"
      else:
        old_empleados[nombre] = "INCREMENTO_FALSE"
        print("----------------------- " + nombre + " Employee with salary of 2000000 or above do not receive any type of increase..\n")
    elif status ==  "INCREMENTO_FALSE":
      print("------------------------- " + nombre + " Your salary is not the range of salary increases.\n")
    elif status ==  "INCREMENTO_TRUE":
      print("------------------------- " + nombre + " --------" + " count on our salary increase!\n")

"""Function to validate the user entry."""
def validar_input(user_input):
  try:
    val = int(user_input)
    # 1 and create
    if val == 1:
      create_empleado()
      reporte_nuevos_empleados()
      return True # continue to main menu
    elif val == 2:
      return False  # exit program
    elif val == 3:
      # "3. Employee Report\n"
      if len(empleados) == 0: # There is not data in the dictionary. Nothing to report
        msg_no_records()
      else:
        msg_list_empleados()
        reporte_nuevos_empleados()
      return True
    elif val == 4:
      "4. Employee Search\n"
      if len(empleados) == 0:  # There is not data in the dictionary. NOthing to search for.
        msg_no_records()
      else:
        msg_buscar_empleados()
        buscar_empleado()
      return True
    elif val == 5:
      if len(empleados) == 0: # There is not data in the dictionary. Nothing to clear.
        msg_no_records()
      else:
        empleados.clear()
        old_empleados.clear()
        print("\nEmployee records successfully deleted!!!\n")
      return True
    else:
      print("\nPlease enter 1 or 2 to continue!")
      return True
  except  Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    return True


"""Function that defines the entry options of the employees and queries."""
def menu_principal():
    print("\n")
    is_seguir = True
    while is_seguir:
      print("MENU PRINCIPAL\n",
        "1. You want to enter employees?\n",
        "2. Desea salir\n",
        "3. Employee Report\n",
        "4. Employee Search\n",
        "5. Clear Records - Validation Test\n")
      user_input = input("Plese enter an option to continue: ")
      is_seguir = validar_input(user_input)


"""Star of the employee capturing data and increase salary."""
is_inicio = True
while is_inicio:
  msg_welcome()
  is_inicio = menu_principal()
msg_goodbye()
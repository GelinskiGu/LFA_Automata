from automathon import NFA
from automathon.errors.errors import InputError

sigma = {'a', 'p', 'i', 'd', 'l', 's'}
# a = assumir direção
# p = piloto automático
# i = interromper
# d = desligar
# r = definir rota
# l = ligar
# s = seguir
states1 = {'1', '2', '3', '4', '5'}
# 1 = Desligado
# 2 = Ligado
# 3 = Parado
# 4 = Dirigindo
# 5 = Automático
delta1 = {
    '1': {'l': {'2'}},
    '2': {'': {'3'}, 'd': {'1'}},
    '3': {'d': {'1'}, 'a': {'4'}, 'p': {'5'}, 's': {'5', '4'}},
    '4': {'p': {'5'}, 'i': {'3'}},
    '5': {'a': {'4'}, 'i': {'3'}}
}
initial_state1 = '1'
final_states1 = {'1'}
automata1 = NFA(states1, sigma, delta1, initial_state1, final_states1)
automata1.view("Automato 1")

states2 = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
# A = Desligado
# B = Ligado
# C = Seguindo
# D = Cruzamento
# E = Parada
# F = Semaforo
# G = Chegada
delta2 = {
    'A': {'l': {'B'}},
    'B': {'p': {'C'}, 'a': {'C'}, 'd': {'A'}},
    'C': {'': {'D', 'F'}, 'i': {'E'}, 'a': {'C'}, 'p': {'C'}},
    'D': {'s': {'C'}, 'i': {'E'}},
    'E': {'s': {'C'}, '': {'G'}},
    'F': {'i': {'E'}, 's': {'D'}},
    'G': {'d': {'A'}}
}
initial_state2 = 'A'
final_states2 = {'A'}
automata2 = NFA(states2, sigma, delta2, initial_state2, final_states2)
automata2.view("Automato 2")


product = automata1.product(automata2)
product_minimized = product.minimize()
product_minimized.view("Automato produto minimizado")
product.view("Automato produto")


def print_transitions(automaton, word):
    current_states = {automaton.initial_state}
    for i, letter in enumerate(word):
        next_states = set()
        for state in current_states:
            if letter in automaton.delta[state]:
                next_states.update(automaton.delta[state][letter])
        for state in current_states:
            for next_state in next_states:
                print(f"({state}, {letter}) => {next_state}")
        current_states = next_states

    if automaton.accept(word):
        print("Palavra aceita!")
    else:
        print("Palavra rejeitada!")


try:
    while True:
        word = input("Insira sua entrada: ")
        if word == "exit":
            break

        print_transitions(product_minimized, word)
except InputError as e:
    print("Entrada inválida! Favor inserir apenas palavras que contenham letras do alfabeto {a, p, i, d, l, s}!")
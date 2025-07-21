#!/usr/bin/env python3
# test_cash.py - Test the numerical cash system

from game_actions import buy_tech_parts_action, display_inventory
from game_data import game_state

def test_cash_system():
    print("=== Testing Cash System ===")
    
    # Test initial state
    print(f"Initial cash: {game_state['cash']}")
    print(f"Initial tech parts: {game_state['tech_parts']}")
    
    # Test buying tech parts with no cash
    print("\n--- Testing buy tech parts with 0 cash ---")
    buy_tech_parts_action()
    print(f"Cash after failed purchase: {game_state['cash']}")
    print(f"Tech parts after failed purchase: {game_state['tech_parts']}")
    
    # Test buying tech parts with cash
    print("\n--- Testing buy tech parts with 1 cash ---")
    game_state['cash'] = 1
    print(f"Set cash to: {game_state['cash']}")
    buy_tech_parts_action()
    print(f"Cash after successful purchase: {game_state['cash']}")
    print(f"Tech parts after successful purchase: {game_state['tech_parts']}")
    
    # Test inventory display
    print("\n--- Testing inventory display ---")
    display_inventory()
    
    print("\n=== Cash System Test Complete ===")

if __name__ == "__main__":
    test_cash_system() 
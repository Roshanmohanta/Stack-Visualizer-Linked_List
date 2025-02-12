import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self, max_size=100000):
        self.top = None
        self.size = 0
        self.max_size = max_size

    def push(self, value):
        if self.size >= self.max_size:
            return False
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        return True

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return self.size >= self.max_size

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    def search(self, value):
        current = self.top
        position_from_top = 0
        while current:
            if current.value == value:
                position_from_bottom = self.size - position_from_top - 1
                return position_from_bottom
            current = current.next
            position_from_top += 1
        return -1

    def get_stack_elements(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.value)
            current = current.next
        return elements
    

    # New method to get the element by position
    def get_by_position(self, position):
    # Counting positions from the bottom, so we need to calculate from the top
     if position >= self.size or position < 0:
        return None  # Position out of bounds
    # Calculate equivalent position from top (0-indexed from the bottom)
     position_from_top = self.size - 1 - position
     current = self.top
     index = 0
     while current:
        if index == position_from_top:
            return current.value
        current = current.next
        index += 1
     return None



class StackVisualizer2D:
    def __init__(self, root):
        self.stack = LinkedListStack()
        self.canvas_width = 500
        self.canvas_height = 500
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()
        self.container_base_y = 450
        self.container_height = 200
        self.container_width = 200
        self.update_visual()

        self.input_label = tk.Label(root, text="Enter data :-",font=("Arial",14))
        self.input_label.pack()

        self.entry = tk.Entry(root, font=("Arial", 14), width=10)
        self.entry.pack(pady=10)

        self.temp_label = tk.Label(root, text="", font=("Arial", 14), bg="yellow")
        self.temp_label.pack(pady=6)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        button_style = {"font": ("Arial", 14, "bold"), "bg": "#4CAF50", "fg": "white", "width": 8, "height": 1}
        push_button = tk.Button(self.button_frame, text="Push", command=self.animate_push, **button_style)
        push_button.grid(row=0, column=0, padx=1, pady=1)

        pop_button = tk.Button(self.button_frame, text="Pop", command=self.animate_pop, **button_style)
        pop_button.grid(row=0, column=1, padx=1, pady=1)

        peek_button = tk.Button(self.button_frame, text="Peek", command=self.peek, **button_style)
        peek_button.grid(row=0, column=2, padx=1, pady=1)

        search_button = tk.Button(self.button_frame, text="Search", command=self.search, **button_style)
        search_button.grid(row=0, column=3, padx=1, pady=1)

        is_empty_button = tk.Button(self.button_frame, text="Is Empty?", command=self.is_empty, **button_style)
        is_empty_button.grid(row=0, column=4, padx=1, pady=1)

        search_by_position_button = tk.Button(self.button_frame, text="Search Pos", command=self.search_by_position, **button_style)
        search_by_position_button.grid(row=0, column=5, padx=1, pady=1)

        

    def show_temp_message(self, message):
        self.temp_label.config(text=message)
        self.temp_label.after(20000, lambda: self.temp_label.config(text=""))
    
    
    def push(self):
        if self.stack.is_full():
            self.show_temp_message("Stack is full! Maximum size is 10.")
            return
        value = self.entry.get()
        if value:
            if self.stack.push(int(value)):
                self.update_visual()
                self.show_temp_message(f"Pushed: {value}")
            self.entry.delete(0, tk.END)

    def pop(self):
        if self.stack.is_empty():
            self.show_temp_message("Stack is already empty!")
        else:
            value = self.stack.top.value
            self.stack.pop()
            self.update_visual()
            self.show_temp_message(f"Popped: {value}")

    def is_empty(self):
        if self.stack .is_empty():
            self.show_temp_message("The stack is empty!")
        else:
            self.show_temp_message("The stack is not empty!")

    def is_full(self):
        if self.stack.is_full():
            self.show_temp_message("The stack is full!")
        else:
            self.show_temp_message("The stack is not full! Maximum size is 10. You can add more elements.")

    def peek(self):
        if self.stack.is_empty():
            self.show_temp_message("Stack is empty!")
        else:
            value = self.stack.peek()
            self.show_temp_message(f"Top element: {value}")

    def search(self):
        value = self.entry.get()
        if value:
            position = self.stack.search(int(value))
            if position == -1:
                self.show_temp_message(f"Element {value} not found in the stack.")
            else:
                self.show_temp_message(f"Element {value} found at position {position+1}.")
            self.entry.delete(0, tk.END)



    # New method to search for an element by its position
    
    
    
    def search_by_position(self):
     position = self.entry.get()
     if position.isdigit():  # Check if input is a valid integer
        position = int(position)
        # Get element by position counted from the bottom
        element = self.stack.get_by_position(position-1)
        if element is None:
            self.show_temp_message(f"No element found at position {position}.")
        else:
            self.show_temp_message(f"Element at position {position}  is {element}.")
     else:
        self.show_temp_message("Please enter a valid integer.")
     self.entry.delete(0, tk.END)



    def animate_push(self):
        if self.stack.is_full():
            self.show_temp_message("Stack is full! Maximum size is 10.")
            return
        value = self.entry.get()
        if value:
            self.animate_push_element(int(value))
            self.entry.delete(0, tk.END)
            self.show_temp_message(f"Pushed: {value}")

    def animate_pop(self):
        if self.stack.is_empty():
            self.show_temp_message("Stack is already empty!")
        else:
            value = self.stack.top.value
            self.animate_pop_element(value)
            self.show_temp_message(f"Popped: {value}")

    def animate_push_element(self, value):
        elements = self.stack.get_stack_elements()

        # Draw the new element at the top of the canvas and move it down into the container
        box_width, box_height = 100, 30
        start_x = (self.canvas_width - box_width) /  2
        start_y = -50  # Start above the canvas
        target_y = self.container_base_y - len(elements) * (box_height + 20) - box_height / 2  # Target with gaps

        # Create the box (element)
        box = self.canvas.create_rectangle(start_x, start_y, start_x + box_width, start_y + box_height,
                                           fill="lightblue", outline="black")
        text = self.canvas.create_text(start_x + box_width / 2, start_y + box_height / 2,
                                       text=str(value), font=("Arial", 12))

        # Animate the box moving into the container
        steps = 50
        dx = 0
        dy = (target_y - start_y) / steps

        for _ in range(steps):
            self.canvas.move(box, dx, dy)
            self.canvas.move(text, dx, dy)
            self.canvas.update()
            self.canvas.after(10)

        # Update the stack after animation
        if self.stack.push(value):
            self.update_visual()
            self.update_top_label()  # Add this to show the top label
        else:
            return False
        return True

    def animate_pop_element(self, value):
        elements = self.stack.get_stack_elements()

        # Parameters for popping animation
        box_width, box_height = 100, 30
        start_x = (self.canvas_width - box_width) / 2
        start_y = self.container_base_y - (len(elements) - 1) * (box_height + 20) - box_height / 2  # Current top of the stack

        # Create the top box to pop
        box = self.canvas.create_rectangle(start_x, start_y, start_x + box_width, start_y + box_height,
                                           fill="lightblue", outline="black")
        text = self.canvas.create_text(start_x + box_width / 2, start_y + box_height / 2,
                                       text=str(value), font=("Arial", 12))

        # Animate the box moving out of the container
        steps = 50
        dx = 0
        dy = -(start_y + box_height) / steps

        for _ in range(steps):
            self.canvas.move(box, dx, dy)
            self.canvas.move(text, dx, dy)
            self.canvas.update()
            self.canvas.after(10)

        # Remove the box and update the stack
        self.canvas.delete(box)
        self.canvas.delete(text)
        self.stack.pop()
        self.update_visual()
        self.update_top_label()  # Update the top label after popping

    def update_visual(self):
        self.canvas.delete("all")
        self.draw_bucket_container()
        elements = self.stack.get_stack_elements()
        self.draw_stack_elements(elements)
        if not elements:
            self.canvas.create_text(self.canvas_width / 2, self.container_base_y - self.container_height / 2,
                                    text="The stack is empty!", font=("Arial", 16), fill="red")
            self.canvas.create_text(self.canvas_width / 2, self.container_base_y + 20,
                                    text="Top = NULL", font=("Arial", 14), fill="black")

    def draw_bucket_container(self):
        x1 = (self.canvas_width - self.container_width) / 2
        x2 = (self.canvas_width + self.container_width) / 2
        bottom_y = self.container_base_y
        top_y = self.container_base_y - self.container_height - 150

        self.canvas.create_line(x1, bottom_y, x2, bottom_y, fill="blue", width=2)  # Bottom line
        self.canvas.create_line(x1, bottom_y, x1, top_y, fill="blue", width=2)  # Left side
        self.canvas.create_line(x2, bottom_y, x2, top_y, fill="blue", width=2)  # Right side



       

    def draw_stack_elements(self, elements):
       box_width, box_height = 100, 30  # Adjust width for two sub-boxes
       sub_box_height = box_height
       value_box_width = 50
       address_box_width = 50
       start_x = (self.canvas_width - box_width) / 2
    
    # Create a list to store random addresses for each element
       addresses = [str(random.randint(1000, 99999)) for _ in range(len(elements))]

    # Iterate over the elements in the stack and draw each with value and address
       for i, value in enumerate(reversed(elements)):
        y_position = self.container_base_y - (i + 1) * (box_height + 20) - box_height / 2  # with gap

        # Draw the element box (split into two sub-boxes: value and address)
        value_box = self.canvas.create_rectangle(start_x, y_position, start_x + value_box_width, y_position + sub_box_height,
                                                 fill="lightblue", outline="black")
        address_box = self.canvas.create_rectangle(start_x + value_box_width, y_position, start_x + box_width,
                                                   y_position + sub_box_height, fill="lightgreen", outline="black")

        # Display the value inside the value box
        self.canvas.create_text(start_x  + value_box_width / 2, y_position + sub_box_height / 2,
                                text=str(value), font=("Arial", 12))

        # Logic for address management:
        if i == 0:  # Bottom-most element should store "NULL" in its address box
            self.canvas.create_text(start_x + value_box_width + address_box_width / 2, y_position + sub_box_height / 2,
                                    text="NULL", font=("Arial", 12))
        else:  # For other elements, store the address of the element below it
            self.canvas.create_text(start_x + value_box_width + address_box_width / 2, y_position + sub_box_height / 2,
                                    text=addresses[i - 1], font=("Arial", 12))

        # Display the current element's own address outside the box (on the right-hand side)
        self.canvas.create_text(start_x +70 + box_width + 50, y_position + sub_box_height / 2,
                                text=f"Address = {addresses[i]}", font=("Arial", 12))

        # Draw an arrow for the next pointer (skip drawing for the last element)
        if i > 0:  # Only draw arrow for the second element and below
                arrow_start_y = y_position + box_height
                arrow_end_y = arrow_start_y + 20
                self.canvas.create_line(start_x+20 + box_width / 2, arrow_start_y, start_x+20 + box_width / 2, arrow_end_y,
                                        arrow=tk.LAST, fill="black")
    
    
    
        


    def update_top_label(self):
        # Remove any existing 'Top = x' labels from the canvas
        self.canvas.delete("top_label")
        elements = self.stack.get_stack_elements()
        
        # Add top labels for each element in the stack
        box_width, box_height = 100, 30
        start_x = (self.canvas_width - box_width) / 2

        for i, value in enumerate(reversed(elements)):
            y_position = self.container_base_y - (i + 1) * (box_height + 20) - box_height / 2  # with gap
            # Display "Top = i" on the left side of each pushed element
            self.canvas.create_text(start_x - 90, y_position + box_height / 2, 
                                    text=f"Top = {i}", font=("Arial", 12), tag="top_label")
            

    

    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stack Visualizer")
    title_label = tk.Label(root, text="Implementation of Stacks using Linked List", font=("Arial", 16), pady=3)
    title_label.pack()

    app = StackVisualizer2D(root)
    root.mainloop()
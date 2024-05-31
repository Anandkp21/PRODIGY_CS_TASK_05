import tkinter as tk
import pyshark
import threading

class PacketSnifferGUI:
    def __init__(self, master):
        self.master = master
        master.title("Packet Sniffer")

        self.capturing = False
        self.capture_thread = None

        self.create_widgets()

        # Configure row and column weights to make the GUI responsive
        master.columnconfigure(0, weight=1)
        master.rowconfigure(2, weight=1)

    def create_widgets(self):
        # Interface Entry
        self.interface_frame = tk.Frame(self.master)
        self.interface_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        self.interface_label = tk.Label(self.interface_frame, text="Interface:")
        self.interface_label.pack(side="left")

        self.interface_entry = tk.Entry(self.interface_frame)
        self.interface_entry.pack(side="left", expand=True, fill="x")

        # Start Capture Button
        self.capture_button = tk.Button(self.master, text="Start Capture", command=self.start_capture)
        self.capture_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Stop Capture Button
        self.stop_button = tk.Button(self.master, text="Stop Capture", command=self.stop_capture, state=tk.DISABLED)
        self.stop_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Output Text
        self.output_text = tk.Text(self.master, wrap="word", height=20, width=80)
        self.output_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    def start_capture(self):
        interface = self.interface_entry.get().strip()
        if not interface:
            self.output_text.insert(tk.END, "Please enter a network interface.\n")
            return

        self.capturing = True
        self.capture_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.capture_thread = threading.Thread(target=self.capture_packets, args=(interface,))
        self.capture_thread.start()

    def capture_packets(self, interface):
        try:
            capture = pyshark.LiveCapture(interface=interface)
            for packet in capture.sniff_continuously():
                if not self.capturing:
                    break
                self.display_packet_info(packet)
        except pyshark.capture.live_capture.UnknownInterfaceException as e:
            self.output_text.insert(tk.END, f"Error: {e}\n")
        except Exception as e:
            self.output_text.insert(tk.END, f"An error occurred: {e}\n")

    def stop_capture(self):
        self.capturing = False
        if self.capture_thread is not None:
            self.capture_thread.join()

        self.capture_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def display_packet_info(self, packet):
        self.output_text.insert(tk.END, f"Packet: {packet}\n")
        self.output_text.see(tk.END)  # Auto-scroll to the end

def main():
    root = tk.Tk()
    gui = PacketSnifferGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

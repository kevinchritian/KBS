import tkinter as tk
from tkinter import messagebox

class Ask():
    def __init__(self, choices=['yes', 'no']):
        self.choices = choices

    def ask(self, question):
        def set_choice(value):
            self.answer = value
            window.quit()

        self.answer = None
        window = tk.Tk()
        window.title("Stroke Detection")
        
        window.geometry("1000x600")
        window.resizable(False, False)
        label = tk.Label(window, text="Jawab pertanyaan-pertanyaan berikut ini dengan Yes atau No!", font=("Helvetica", 14), wraplength=350, justify="center")
        label.pack(pady=20)
        label = tk.Label(window, text="Apakah anda mengalami gejala-gejala berikut: ", font=("Helvetica", 14), wraplength=350, justify="center")
        label.pack(pady=20)
        label = tk.Label(window, text=question, font=("Helvetica", 12), wraplength=350, justify="center")
        label.pack(pady=20)

        button_frame = tk.Frame(window)
        button_frame.pack(pady=10)

        yes_button = tk.Button(button_frame, text="Yes", command=lambda: set_choice('yes'), font=("Helvetica", 10), width=10)
        yes_button.pack(side=tk.LEFT, padx=10)

        no_button = tk.Button(button_frame, text="No", command=lambda: set_choice('no'), font=("Helvetica", 10), width=10)
        no_button.pack(side=tk.RIGHT, padx=10)

        window.mainloop()
        window.destroy()
        return self.answer

class Content():
    def __init__(self, x):
        self.x = x

class If(Content):
    pass

class AND(Content):
    pass

class OR(Content):
    pass

rules={
    'default': Ask(['yes','no']),
    'Onset saat Beraktivitas(G16)' : Ask(['yes','no']),
    'Nyeri atau Kram saat berjalan(G10)' : Ask(['yes','no']),
    'Susah menggerakan kaki atau tangan(G35)' : Ask(['yes','no']),
    'Onset saat istirahat(G20)' : Ask(['yes','no']),
    'Sesak nafas(G13)' : Ask(['yes','no']),
    'Gangguan Bicara(G1)'  :  Ask(['yes','no']),
    'Penurunan kesadaran(G14)' : Ask(['yes','no']),
    'Telinga Berdenging(G30)' : Ask(['yes','no']),
    'Gangguan memori(G34)' : Ask(['yes','no']),
    'Tidak dapat berubah sikap dari berbaring ke duduk(G22)' : Ask(['yes','no']),
    'Kelemahan Anggota gerak kiri atau kanan(G15)' : Ask(['yes','no']),
    'Sering kesemutan(G28)' : Ask(['yes','no']),
    'Demam(G43)' : Ask(['yes','no']),
    'Batuk(G39)' : Ask(['yes','no']),
    'Bingung(G32)' : Ask(['yes','no']),
    'Cemas(G38)' : Ask(['yes','no']),
    'Lemas(G27)':Ask(['yes','no']),
    'Status Fungsional perlu bantuan(G2)' : Ask(['yes','no']),
    'Nyeri di bagian dada(G40)' : Ask(['yes','no']),
    
    
#     Rule
    'goal:Thrombosis Stroke_8':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):yes',
                                   'Kelemahan Anggota gerak kiri atau kanan(G15):yes']),
    
    'goal:Thrombosis Stroke_7':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):yes',
                                   'Kelemahan Anggota gerak kiri atau kanan(G15):no','Sering kesemutan(G28):yes','Demam(G43):yes']),
    
    'goal:Embolism Stroke_6':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):yes',
                                 'Kelemahan Anggota gerak kiri atau kanan(G15):no','Sering kesemutan(G28):yes','Demam(G43):no']),

    'goal:Thrombosis Stroke_6':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):yes',
                                   'Kelemahan Anggota gerak kiri atau kanan(G15):no','Sering kesemutan(G28):no']),
    
    'goal:Thrombosis Stroke_5':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):no',
                                   'Nyeri atau Kram saat berjalan(G10):yes','Penurunan kesadaran(G14):yes']),
    
    'goal:Thrombosis Stroke_4':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):no',
                                   'Nyeri atau Kram saat berjalan(G10):yes','Penurunan kesadaran(G14):no','Telinga Berdenging(G30):yes']),

    'goal:Thrombosis Stroke_3':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):no',
                                   'Nyeri atau Kram saat berjalan(G10):yes','Penurunan kesadaran(G14):no',
                                   'Telinga Berdenging(G30):no','Gangguan Bicara(G1):yes','Gangguan memori(G34):yes']),

    'goal:Embolism Stroke_5':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):no',
                                 'Nyeri atau Kram saat berjalan(G10):yes','Penurunan kesadaran(G14):no'
                                 ,'Telinga Berdenging(G30):no','Gangguan Bicara(G1):yes','Gangguan memori(G34):no',
                                 'Tidak dapat berubah sikap dari berbaring ke duduk(G22):yes','Kelemahan Anggota gerak kiri atau kanan(G15):yes']),

    'goal:Thrombosis Stroke_2':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):no',
                                   'Nyeri atau Kram saat berjalan(G10):yes','Penurunan kesadaran(G14):no',
                                   'Telinga Berdenging(G30):no','Gangguan Bicara(G1):yes','Gangguan memori(G34):no',
                                   'Tidak dapat berubah sikap dari berbaring ke duduk(G22):yes','Kelemahan Anggota gerak kiri atau kanan(G15):no']),
    
    'goal:Embolism Stroke_4':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):no',
                                 'Nyeri atau Kram saat berjalan(G10):yes','Penurunan kesadaran(G14):no',
                                 'Telinga Berdenging(G30):no','Gangguan Bicara(G1):yes','Gangguan memori(G34):no'
                                 ,'Tidak dapat berubah sikap dari berbaring ke duduk(G22):no']),

    'goal:Embolism Stroke_3':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):no',
                                 'Nyeri atau Kram saat berjalan(G10):yes','Penurunan kesadaran(G14):no',
                                 'Telinga Berdenging(G30):no','Gangguan Bicara(G1):no']),

    'goal:Embolism Stroke_2' :If(['Nyeri di bagian dada(G40):yes', 'Onset saat Beraktivitas(G16):no',
                                  'Nyeri atau Kram saat berjalan(G10):no', 'Susah menggerakan kaki atau tangan(G35):yes']),

    'goal:Thrombosis Stroke_1':If(['Nyeri di bagian dada(G40):yes', 'Onset saat Beraktivitas(G16):no',
                                   'Nyeri atau Kram saat berjalan(G10):no','Susah menggerakan kaki atau tangan(G35):no'
                                   ,'Onset saat istirahat(G20):yes','Gangguan Bicara(G1):yes']),
    
    'goal:Embolism Stroke_1':If(['Nyeri di bagian dada(G40):yes','Onset saat Beraktivitas(G16):no',
                                 'Nyeri atau Kram saat berjalan(G10):no','Susah menggerakan kaki atau tangan(G35):no',
                                 'Onset saat istirahat(G20):yes','Gangguan Bicara(G1):no']),
    
    'goal:Non Stroke':If(['Nyeri di bagian dada(G40):yes', 'Onset saat Beraktivitas(G16):no', 'Nyeri atau Kram saat berjalan(G10):no'
                          , 'Susah menggerakan kaki atau tangan(G35):no', 'Onset saat istirahat(G20):no']),
    
    'goal:Thrombosis Stroke_11':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):yes',
                                    'Lemas(G27):yes','Gangguan Bicara(G1):yes']),
    
    'goal:Thrombosis Stroke_10':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):yes',
                                    'Lemas(G27):yes','Gangguan Bicara(G1):no','Status Fungsional perlu bantuan(G2):yes']),

    'goal:Embolism Stroke_8':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):yes','Lemas(G27):yes'
                                 ,'Gangguan Bicara(G1):no','Status Fungsional perlu bantuan(G2):no']),
    
    'goal:Embolism Stroke_7':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):yes','Lemas(G27):no'
                                 ,'Sering kesemutan(G28):yes']),
    
    'goal:Revise':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):yes','Lemas(G27):no',
                      'Sering kesemutan(G28):no']),

    'goal:Intracerebral hemorrhage_2':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):no',
                                          'Sesak nafas(G13):yes','Onset saat Beraktivitas(G16):yes','Batuk(G39):yes']),
    
    'goal:Subarachnoid hermorrhage_1':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):no',
                                          'Sesak nafas(G13):yes','Onset saat Beraktivitas(G16):yes','Batuk(G39):no']),
    
    'goal:Intracerebral hemorrhage_1':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):no',
                                          'Sesak nafas(G13):yes','Onset saat Beraktivitas(G16):no']),

    'goal:Intracerebral hemorrhage_4':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):no',
                                          'Sesak nafas(G13):no','Bingung(G32):yes']),

    'goal:Subarachnoid hermorrhage_2':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):no',
                                          'Sesak nafas(G13):no','Bingung(G32):no','Cemas(G38):yes']),
    
    'goal:Thrombosis Stroke_9':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):no','Sesak nafas(G13):no'
                                   ,'Bingung(G32):no','Cemas(G38):no','Gangguan Bicara(G1):yes']),
    
    'goal:Intracerebral hemorrhage_3':If(['Nyeri di bagian dada(G40):no','Nyeri atau Kram saat berjalan(G10):no',
                                          'Sesak nafas(G13):no','Bingung(G32):no','Cemas(G38):no','Gangguan Bicara(G1):no'])
    
    
}


# rules ={
#     'default': Ask(['yes','no']),
#     'very big' : Ask(['yes','no']),
#     'squeak' : Ask(['yes','no']),
#     'Long neck' : Ask(['yes','no']),
#     'have a trunk' : Ask(['yes','no']),
#     'Like to be in water' : Ask(['yes','no']),
    
#     'goal:squirrel':If(['very big:no','squeak:no']),
#     'goal:mouse':If(['very big:no','squeak:yes']),
#     'goal:Rhiho':If(['very big:yes','Long neck:no','have a trunk:no','like to be in water:no']),
#     'goal:Elephant':If(['very big:yes','Long neck:no','have a trunk:yes']),
#     'goal:Giraffe':If(['very big:yes','Long neck:yes'])
# }

class Forward():
    def __init__(self, rules):
        self.rules = rules
        self.memory = {}

    def get(self, name):
        if ':' in name:
            k, v = name.split(':')
            vv = self.get(k)
            return 'y' if v == vv else 'n'
        if name in self.memory.keys():
            return self.memory[name]
        for fld in self.rules.keys():
            if fld == name or fld.startswith(name + ":"):
                value = 'y' if fld == name else fld.split(':')[1]
                res = self.eval(self.rules[fld], field=name)
                if res != 'y' and res != 'n' and value == 'y':
                    self.memory[name] = res
                    return res
                if res == 'y':
                    self.memory[name] = value
                    return value
        res = self.eval(self.rules['default'], field=name)
        self.memory[name] = res
        return res

    def eval(self, expr, field=None):
        if isinstance(expr, Ask):
            return expr.ask(field)
        elif isinstance(expr, If):
            return self.eval(expr.x)
        elif isinstance(expr, AND) or isinstance(expr, list):
            expr = expr.x if isinstance(expr, AND) else expr
            for x in (expr):
                if self.eval(x) == 'n':
                    return 'n'
            return 'y'
        elif isinstance(expr, OR):
            for x in (expr.x):
                if self.eval(x) == 'y':
                    return 'y'
            return 'n'
        elif isinstance(expr, str):
            return self.get(expr)
        else:
            print("Unknown expr: {}".format(expr))

class Backward():
    def __init__(self, rules):
        self.rules = rules
        self.memory = {}

    def get(self, name):
        if ':' in name:
            k, v = name.split(':')
            vv = self.get(k)
            return 'y' if v == vv else 'n'
        if name in self.memory.keys():
            return self.memory[name]
        for fld in self.rules.keys():
            if fld == name or fld.startswith(name + ":"):
                value = 'y' if fld == name else fld.split(':')[1]
                res = self.eval(self.rules[fld], field=name)
                if res != 'y' and res != 'n' and value == 'y':
                    self.memory[name] = res
                    return res
                if res == 'y':
                    self.memory[name] = value
                    return value
        res = self.eval(self.rules['default'], field=name)
        self.memory[name] = res
        return res

    def eval(self, expr, field=None):
        if isinstance(expr, Ask):
            return expr.ask(field)
        elif isinstance(expr, If):
            return self.eval(expr.x)
        elif isinstance(expr, AND) or isinstance(expr, list):
            expr = expr.x if isinstance(expr, AND) else expr
            for x in reversed(expr):  
                if self.eval(x) == 'n':
                    return 'n'
            return 'y'
        elif isinstance(expr, OR):
            for x in reversed(expr.x):  
                if self.eval(x) == 'y':
                    return 'y'
            return 'n'
        elif isinstance(expr, str):
            return self.get(expr)
        else:
            print("Unknown expr: {}".format(expr))

def infer():
    kb = Forward(rules)
    goal = kb.get('goal')
    messagebox.showinfo("Stroke Detection Result", f"Anda Didiagnosis menderita: {goal}")

def infer_alternative():
    kb2 = Backward(rules)
    goal = kb2.get('goal')
    messagebox.showinfo("Stroke Detection Result", f"Anda Didiagnosis menderita: {goal}")

def main():
    root = tk.Tk()
    root.title("Stroke Detection System")
    root.geometry("1000x600")
    root.resizable(False, False)

    tk.Label(root, text="Sistem Pendeteksi Stroke", font=("Helvetica", 14)).pack(pady=10)
    tk.Label(root, text="Pilih metode inferensi yang ingin kamu gunakan:", font=("Helvetica", 14)).pack(pady=10)

    infer_button = tk.Button(root, text="Forward Chaining", command=infer, font=("Helvetica", 12), width=20)
    infer_button.pack(pady=10)

    alt_infer_button = tk.Button(root, text="Backward Chaining", command=infer_alternative, font=("Helvetica", 12), width=20)
    alt_infer_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

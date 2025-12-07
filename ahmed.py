from tkinter import *
import math

def calculate_circumference(r):
    """
    تحسب محيط الدائرة باستخدام العلاقة: 2 * π * نصف القطر
    """
    return 2 * math.pi * 

def perform_calculation():
    try:
        radius = float(myentry.get())
        result = calculate_circumference(radius)

        mylabel_result.config(
            text=f"✅ المحيط: {result:.2f} وحدة",
            fg="#28a745",
            font=("Segoe UI", 13, "bold")
        )

    except ValueError:
        mylabel_result.config(
            text="❌ خطأ: يرجى إدخال رقم صحيح.",
            fg="#dc3545",
            font=("Segoe UI", 11, "bold")
        )
    except Exception as e:
        mylabel_result.config(text=f"حدث خطأ: {e}", fg="red")


myframe = Tk()
myframe.title("حاسبة محيط الدائرة")
myframe.geometry("450x320")
myframe.config(bg="#f0f0f0")


Label(
    myframe,
    text="حاسبة محيط الدائرة باستخدام Tkinter",
    bg="#3f51b5",
    fg="white",
    font=("Segoe UI", 16, "bold"),
    pady=15
).pack(fill=X)


Label(
    myframe,
    text="أدخل قيمة نصف القطر:",
    bg="#f0f0f0",
    font=("Segoe UI", 13)
).pack(pady=(25, 5))


myentry = Entry(
    myframe,
    width=35,
    font=("Arial", 12),
    bd=1,
    relief="sunken",
    justify="center"
)
myentry.pack(pady=5)


# الزر
mybutton = Button(
    myframe,
    text="احسب المحيط",
    fg="white",
    bg="#4CAF50",
    activebackground="#45a049",
    font=("Segoe UI", 14, "bold"),
    padx=30,
    pady=10,
    relief="raised",
    cursor="hand2",
    command=perform_calculation,
)
mybutton.pack(pady=25)


mylabel_result = Label(
    myframe,
    text="النتيجة ستظهر هنا",
    bg="#f0f0f0",
    fg="gray",
    font=("Segoe UI", 12, "italic")
)
mylabel_result.pack(pady=10)


myframe.mainloop()

import math
import tkinter as Tkinter


# Checks whether the inputs less of than the other one
def Less(x, y):
    if x < y:
        return x
    else:
        return y


# Checks whether the inputs are greater than the other one
def Greater(x,y):
    if(x>y):
        return x
    else:
        return y


# This function calculates the complex value of the transfer function at the given frequency
def HejwtCalculate(H_n, N, w, T):
    w=2*math.pi*w
    Hejwt_w = complex(0, 0)
    for looper in range(0, int(N)):
        Hejwt_w += H_n[looper]*complex(math.cos(-1*w*T*looper), math.sin(-1*w*T*looper))
    return Hejwt_w


# This function calculates the final weight series. Inputs: window and raw weight series
def ResultWeightsCalculate(Wk, Hi, N):
    H_n = []
    looper = int(0)
    for looper in range(0,int(N)):
        H_n.append(Wk[looper]*Hi[looper])
    return H_n


def DrawHejwt(Canvas, H, minFreq, maxFreq, fs, N, width, height):
    global DrawOffset
    Canvas.delete("all")
    Canvas.create_line(1*width / 8, 0, 1*width / 8, (DrawCoeff + 1) * height / 2, fill="gray", width=1)
    Canvas.create_line(2*width / 8, 0, 2*width / 8, (DrawCoeff + 1) * height / 2, fill="gray", width=1)
    Canvas.create_line(3*width / 8, 0, 3*width / 8, (DrawCoeff + 1) * height / 2, fill="gray", width=1)
    Canvas.create_line(4*width / 8, 0, 4*width / 8, (DrawCoeff + 1) * height / 2, fill="gray", width=1)
    Canvas.create_line(5*width / 8, 0, 5*width / 8, (DrawCoeff + 1) * height / 2, fill="gray", width=1)
    Canvas.create_line(6*width / 8, 0, 6*width / 8, (DrawCoeff + 1) * height / 2, fill="gray", width=1)
    Canvas.create_line(7*width / 8, 0, 7*width / 8, (DrawCoeff + 1) * height / 2, fill="gray", width=1)
    Canvas.create_line(0, 1*((DrawCoeff + 1) * height / 2)/8, width, 1*((DrawCoeff + 1) * height / 2)/8, fill="gray", width=1)
    Canvas.create_line(0, 2 * ((DrawCoeff + 1) * height / 2) / 8, width, 2 * ((DrawCoeff + 1) * height / 2) / 8, fill="gray", width=1)
    Canvas.create_line(0, 3 * ((DrawCoeff + 1) * height / 2) / 8, width, 3 * ((DrawCoeff + 1) * height / 2) / 8, fill="gray", width=1)
    Canvas.create_line(0, 4 * ((DrawCoeff + 1) * height / 2) / 8, width, 4 * ((DrawCoeff + 1) * height / 2) / 8, fill="gray", width=1)
    Canvas.create_line(0, 5 * ((DrawCoeff + 1) * height / 2) / 8, width, 5 * ((DrawCoeff + 1) * height / 2) / 8, fill="gray", width=1)
    Canvas.create_line(0, 6 * ((DrawCoeff + 1) * height / 2) / 8, width, 6 * ((DrawCoeff + 1) * height / 2) / 8, fill="gray", width=1)
    Canvas.create_line(0, 7 * ((DrawCoeff + 1) * height / 2) / 8, width, 7 * ((DrawCoeff + 1) * height / 2) / 8, fill="gray", width=1)
    Canvas.create_line(0, 8 * ((DrawCoeff + 1) * height / 2) / 8, width, 8 * ((DrawCoeff + 1) * height / 2) / 8, fill="gray", width=1)
    Tkinter.Label(Canvas, text=str(1 * (maxFreq - minFreq) / 8)).place(x=1 * width / 8 - 18, y=height - 12)
    Tkinter.Label(Canvas, text=str(2 * (maxFreq - minFreq) / 8)).place(x=2 * width / 8 - 18, y=height - 12)
    Tkinter.Label(Canvas, text=str(3 * (maxFreq - minFreq) / 8)).place(x=3 * width / 8 - 18, y=height - 12)
    Tkinter.Label(Canvas, text=str(4 * (maxFreq - minFreq) / 8)).place(x=4 * width / 8 - 18, y=height - 12)
    Tkinter.Label(Canvas, text=str(5 * (maxFreq - minFreq) / 8)).place(x=5 * width / 8 - 18, y=height - 12)
    Tkinter.Label(Canvas, text=str(6 * (maxFreq - minFreq) / 8)).place(x=6 * width / 8 - 18, y=height - 12)
    Tkinter.Label(Canvas, text=str(7 * (maxFreq - minFreq) / 8)).place(x=7 * width / 8 - 18, y=height - 12)
    Tkinter.Label(Canvas, text=str(8 * (maxFreq - minFreq) / 8)).place(x=8 * width / 8 - 18, y=height - 12)

    Prev=0
    HeightCoeff=height*DrawCoeff
    Offs=(height-HeightCoeff)/2
    FreqPix=(maxFreq-minFreq)/width
    for looper in range(0, width-1):
        temp = Offs+HeightCoeff*(1-abs(HejwtCalculate(H, N, looper*FreqPix+minFreq, 1/fs)))
        Canvas.create_line(looper, Prev, looper+1, temp, fill="blue", width=1)
        Prev=temp


# This function implements the modified Bessel function
def ModifiedBessel_I0(x):
    I0 = float(0)
    for looper in range(1, 16):
        I0 += math.pow((math.pow(x / 2, float(looper)) / float(math.factorial(looper))), 2)
    I0 += 1
    return I0


# This function calculates the elements of the Kaiser windowing serial
def KaislerWindowing(Beta, Degree):
    Wk = []
    BesselForBeta = ModifiedBessel_I0(Beta)
    for looper in range(0, int(Degree)):
        Wk.append(ModifiedBessel_I0(Beta * math.sqrt(1 - math.pow((1 - 2 * looper / (Degree - 1)), 2))) / BesselForBeta)
    return Wk


# This function calculatest the base wieght coefficients in high pass case
def BaseWindowCoefficientForHighPass(fA, fZ, fs, Degree):
    ret = []
    Omegai = 2*math.pi*math.fabs(fA+fZ)/2
    T = 1/fs
    print("omegai = "+str(Omegai) + " T = " + str(T))

    # The number of the coefficients is always an odd number and the middle one in the serial must be calculated
    # otherwise. Therefore there are 2 loop and between them there is the middle calculation.
    for looper in range(0, int(Degree/2)):
        temp = looper-(Degree-1)/2
        ret.append(-1*math.sin(Omegai*T*temp)/(math.pi*temp))
    ret.append(1-((fA+fZ)/fs))
    for looper in range(int(Degree/2)+1, int(Degree)):
        temp = looper - (Degree - 1) / 2
        ret.append(-1 * math.sin(Omegai * T * temp) / (math.pi * temp))
    return ret


def BaseWindowCoefficientForLowPass(fA, fZ, fs, Degree):
    ret = []
    Omegai = 2 * math.pi * math.fabs(fA + fZ) / 2
    T = 1 / fs
    print("omegai = " + str(Omegai) + " T = " + str(T))
    offs=0
    # The number of the coefficients is always an odd number and the middle one in the serial must be calculated
    # otherwise. Therefore there are 2 loop and between them there is the middle calculation.
    for looper in range(0, int(Degree / 2)):
        temp = looper - (Degree - 1) / 2
        ret.append(math.sin(Omegai * T * temp) / (math.pi * temp))
    if(Degree%2 != 0):
        ret.append((fA + fZ) / fs)
        offs = 1
    for looper in range(int(Degree / 2)+offs, int(Degree)):
        temp = looper - (Degree - 1) / 2
        ret.append(math.sin(Omegai * T * temp) / (math.pi * temp))
    return ret


# This function calls the appropriate function according to the standing of the radiobuttons.
def RadioButtonSelecter():
    global RadioButtonSelectorVariable
    global MainWindow
    print(RadioButtonSelectorVariable)
    if(RadioButtonSelectorVariable.get() == 1):
        LowOrHighPassRadioButtonPressed()
    elif(RadioButtonSelectorVariable.get() == 2):
        LowOrHighPassRadioButtonPressed()
    elif (RadioButtonSelectorVariable.get() == 3):
        BandStopOrPassRadioButtonSelected()
    elif (RadioButtonSelectorVariable.get() == 4):
        BandStopOrPassRadioButtonSelected()


# This function immediately checks the entry if its content is number after changing.
def EntryChecker(EntryVar):
    if (len(EntryVar.get()) != 0):
        CurrentChar = EntryVar.get()[len(EntryVar.get()) - 1]
        if (CurrentChar not in "0123456789."):
            EntryVar.set(EntryVar.get()[0:len(EntryVar.get())-1])
        elif (CurrentChar == '.' and CurrentChar in EntryVar.get()[0:len(EntryVar.get())-1]):
            EntryVar.set(EntryVar.get()[0:len(EntryVar.get()) - 1])


def LowOrHighPassRadioButtonPressed():
    global F3Entry
    global F4Entry
    global F3Label
    global F4Label
    F3Entry.place_forget()
    F4Entry.place_forget()
    F3Label.place_forget()
    F4Label.place_forget()


def BandStopOrPassRadioButtonSelected():
    global F3Entry
    global F4Entry
    global F3Label
    global F4Label
    F3Entry.place(x=200, y=116)
    F4Entry.place(x=200, y=137)
    F3Label.place(x=100, y=115)
    F4Label.place(x=100, y=136)


# This function implements the calculating of the weight series and the drawing of the transmission function after pressing of the Start button calculate.
def StartButtonPressed():
    try:
        SamplingFrequency = float(SamplingFreqEntryVar.get())
        Break2Freq = float(F1EntryVar.get())
        Break1Freq = float(F2EntryVar.get())
        AmplitudeSuppressing = float(AmpEntryVar.get())
        Fluctuation = float(DeltaEntryVar.get())

        if (RadioButtonSelectorVariable.get() == 1):
            H, N = LowPassDesign(SamplingFrequency, Break1Freq, Break2Freq, AmplitudeSuppressing, Fluctuation)
        elif (RadioButtonSelectorVariable.get() == 2):
            H,N = HighPassDesign(SamplingFrequency, Break1Freq, Break2Freq, AmplitudeSuppressing, Fluctuation)
        elif (RadioButtonSelectorVariable.get() == 3):
            print("Band pass")
        elif (RadioButtonSelectorVariable.get() == 4):
            print("Band stop")
        print("Filter order: "+str(N))
        FilterOrder.config(text=str(int(N)))
        for looper in range(0, int(N)):
            print(H[looper])
        if(DrawCheckButtonVar.get()==1):
            global DrawerWindow
            DrawerWindow = Tkinter.Toplevel(MainWindow)
            DrawerWindow.geometry("1040x310")
            DrawerWindowHeight=300
            DrawerWindowWidth=1000

            # Creating a canvas and binding its click event to a function that places a label on the canvas with some information about the diagramm.
            Canvas1 = Tkinter.Canvas(DrawerWindow, width=DrawerWindowWidth, height=DrawerWindowHeight)
            Canvas1.place(x=30, y=0)
            Canvas1.bind('<Button-1>', lambda e: ClickOnDraw(e, H, N, SamplingFrequency,DrawerWindowWidth,DrawerWindowHeight, Canvas1))

            MinFreqEntry = Tkinter.Entry(DrawerWindow,textvariable = MinFreqEntryVar)
            #MinFreqEntry.place(x=DrawerWindowWidth-75,y=0, width=70)
            MinFreqEntry.place(x=30, y=DrawerWindowHeight-10, width=50)
            MaxFreqEntry = Tkinter.Entry(DrawerWindow, textvariable=MaxFreqEntryVar)
            #MaxFreqEntry.place(x=DrawerWindowWidth - 75, y=20, width=70)
            MaxFreqEntry.place(x=DrawerWindowWidth - 10, y=DrawerWindowHeight-10, width=50)
            MaxFreqEntryVar.set(str(SamplingFrequency))
            MinFreqEntryVar.set(str(0))
            ReDrawButton = Tkinter.Button(DrawerWindow, text="Redraw", command=lambda:DrawHejwt(Canvas1, H, float(MinFreqEntryVar.get()), float(MaxFreqEntryVar.get()), SamplingFrequency, N, DrawerWindowWidth, DrawerWindowHeight))
            ReDrawButton.place(x=DrawerWindowWidth-65,y=45)
            MinFreqEntryVar.trace("w", lambda name, index, mode: EntryChecker(MinFreqEntryVar))
            MaxFreqEntryVar.trace("w", lambda name, index, mode: EntryChecker(MaxFreqEntryVar))

            # This line shows the 0 amplitude
            Canvas1.create_line(0, (DrawCoeff+1)*DrawerWindowHeight/2, DrawerWindowWidth, (DrawCoeff+1)*DrawerWindowHeight/2, fill="blue", width=1)
            DrawHejwt(Canvas1, H, 0, SamplingFrequency, SamplingFrequency, N, DrawerWindowWidth, DrawerWindowHeight)
    except:
        print("szar")


# This function deletes the helper lines with information label from the canvas if right mouse click occures on it.
def DeleteHelperLine(ClickEvent, Canvas):
    for looper in range(0, len(ValueLabelArray)):
        if(ValueLabelArray[looper][0] == ClickEvent.widget):
            ValueLabelArray[looper][0].destroy()
            Canvas.delete(ValueLabelArray[looper][1])
            ValueLabelArray.remove(ValueLabelArray[looper])
            break


# This function implements the drawing of the helper lines and information labels.
def ClickOnDraw(ClickEvent, H, N, WindowMaxFreq, CanvasWidth, CanvasHeight, DrawableCanvas):
    global DrawerWindow
    # It shows the amplitude in dB
    FreqPix = WindowMaxFreq / CanvasWidth
    temp = abs(HejwtCalculate(H, N, ClickEvent.x * FreqPix, 1 / WindowMaxFreq))
    temp = 20*math.log10(temp)
    TemporaryLabel = Tkinter.Label(DrawerWindow, text="A="+str(round(temp,3))+"\nf="+str(round(ClickEvent.x * FreqPix)))
    TemporaryLine = DrawableCanvas.create_line(ClickEvent.x, 0, ClickEvent.x, (DrawCoeff + 1) * CanvasHeight / 2, fill="gray", width=1)
    TemporaryLabLine = TemporaryLabel, TemporaryLine
    # Appending the new helper line and label to their list
    ValueLabelArray.append(TemporaryLabLine)
    ValueLabelArray[len(ValueLabelArray)-1][0].place(x=ClickEvent.x, y=ClickEvent.y)
    ValueLabelArray[len(ValueLabelArray) - 1][0].bind('<Button-3>', lambda e: DeleteHelperLine(e, DrawableCanvas))


def HighPassDesign(SamplingFreq, ClosingFrequency, TransitionFrequency, SuppressGain, Fluctuation):
    # ClosingFrequency: From lower to higher frequencies at this point the supressing is higher than the prescribed
    # TransitionFrequency: At this point the transmission is ideally one
    dW = math.fabs(ClosingFrequency - TransitionFrequency) / SamplingFreq
    Delta2 = math.pow(0.1, SuppressGain / 20)

    N = (((-20 * math.log10(Less(Fluctuation, Delta2))) - 7.95) / (14.36 * dW)) + 1
    if (N > int(N)):
        N = float(int(N) + 1)
    if(0 == N%2):
        N += 1
    Beta = 0.1102 * (SuppressGain - 8.7)

    Wk_n = KaislerWindowing(Beta, N)
    Hi_n = BaseWindowCoefficientForHighPass(ClosingFrequency, TransitionFrequency, SamplingFreq, N)
    H = ResultWeightsCalculate(Wk_n, Hi_n, N)
    return H, N


def LowPassDesign(SamplingFreq, ClosingFrequency, TransitionFrequency, SuppressGain, Fluctuation):
    dW = math.fabs(ClosingFrequency - TransitionFrequency) / SamplingFreq
    Delta2 = math.pow(0.1, SuppressGain / 20)

    N = (((-20 * math.log10(Less(Fluctuation, Delta2))) - 7.95) / (14.36 * dW)) + 1
    if (N > int(N)):
        N = float(int(N) + 1)
    Beta = 0.1102 * (SuppressGain - 8.7)

    Wk_n = KaislerWindowing(Beta, N)
    Hi_n = BaseWindowCoefficientForLowPass(ClosingFrequency, TransitionFrequency, SamplingFreq, N)
    H = ResultWeightsCalculate(Wk_n, Hi_n, N)
    return H, N


MainWindow = Tkinter.Tk()
MainWindow.geometry("350x200")

# Initialization of the widget variables
RadioButtonSelectorVariable = Tkinter.IntVar()
DrawCheckButtonVar = Tkinter.IntVar()
F1EntryVar = Tkinter.StringVar()
F2EntryVar = Tkinter.StringVar()
F3EntryVar = Tkinter.StringVar()
F4EntryVar = Tkinter.StringVar()
AmpEntryVar = Tkinter.StringVar()
DeltaEntryVar = Tkinter.StringVar()
SamplingFreqEntryVar = Tkinter.StringVar()
MinFreqEntryVar = Tkinter.StringVar()
MaxFreqEntryVar = Tkinter.StringVar()

F1EntryVar.set("2000")
F2EntryVar.set("3000")
AmpEntryVar.set("66")
DeltaEntryVar.set("0.001")
SamplingFreqEntryVar.set("13000")
RadioButtonSelectorVariable.set(1)

DrawCoeff = 0.9

ValueLabelArray = []
DrawerWindow = []

# End of initialization of the widget variables

StartButton = Tkinter.Button(MainWindow, text="Start", command=StartButtonPressed).place(x=35, y=115)
RadioButton1 = Tkinter.Radiobutton(MainWindow, text="Low-pass", variable=RadioButtonSelectorVariable, value=1, command=RadioButtonSelecter).place(x=10, y=10)
RadioButton2 = Tkinter.Radiobutton(MainWindow, text="High-pass", variable=RadioButtonSelectorVariable, value=2, command=RadioButtonSelecter).place(x=10, y=30)
RadioButton3 = Tkinter.Radiobutton(MainWindow, text="Band-pass", variable=RadioButtonSelectorVariable, value=3, command=RadioButtonSelecter).place(x=10, y=50)
RadioButton4 = Tkinter.Radiobutton(MainWindow, text="Band-stop", variable=RadioButtonSelectorVariable, value=4, command=RadioButtonSelecter).place(x=10, y=70)

F1EntryVar.trace("w", lambda name, index, mode: EntryChecker(F1EntryVar))
F2EntryVar.trace("w", lambda name, index, mode: EntryChecker(F2EntryVar))
F3EntryVar.trace("w", lambda name, index, mode: EntryChecker(F3EntryVar))
F4EntryVar.trace("w", lambda name, index, mode: EntryChecker(F4EntryVar))
AmpEntryVar.trace("w", lambda name, index, mode: EntryChecker(AmpEntryVar))
DeltaEntryVar.trace("w", lambda name, index, mode: EntryChecker(DeltaEntryVar))
SamplingFreqEntryVar.trace("w", lambda name, index, mode: EntryChecker(SamplingFreqEntryVar))

DeltaEntry = Tkinter.Entry(MainWindow, textvariable=DeltaEntryVar, selectforeground="red")
DeltaEntry.place(x=200, y=11)
AmpEntry = Tkinter.Entry(MainWindow, textvariable=AmpEntryVar, selectforeground="red")
AmpEntry.place(x=200, y=32)
SamplingFreqEntry = Tkinter.Entry(MainWindow, textvariable=SamplingFreqEntryVar, selectforeground="red")
SamplingFreqEntry.place(x=200, y=53)
F1Entry = Tkinter.Entry(MainWindow, textvariable=F1EntryVar, selectforeground="red")
F1Entry.place(x=200, y=74)
F2Entry = Tkinter.Entry(MainWindow, textvariable=F2EntryVar, selectforeground="red")
F2Entry.place(x=200, y=95)
F3Entry = Tkinter.Entry(MainWindow, textvariable=F3EntryVar, selectforeground="red")
F3Entry.place(x=200, y=116)
F4Entry = Tkinter.Entry(MainWindow, textvariable=F4EntryVar, selectforeground="red")
F4Entry.place(x=200, y=137)

DeltaLabel = Tkinter.Label(MainWindow, text="Max fluctuation")
DeltaLabel.place(x=100, y=10)
AmpLabel = Tkinter.Label(MainWindow, text="Min. suppression")
AmpLabel.place(x=100, y=31)
SamplingFreqLabel = Tkinter.Label(MainWindow, text="Sampling freq.:")
SamplingFreqLabel.place(x=100, y=52)
F1Label = Tkinter.Label(MainWindow, text="1. break freq")
F1Label.place(x=100, y=73)
F2Label = Tkinter.Label(MainWindow, text="2. break freq")
F2Label.place(x=100, y=94)
F3Label = Tkinter.Label(MainWindow, text="3. break freq")
F3Label.place(x=100, y=136)
F4Label = Tkinter.Label(MainWindow, text="4. break freq")
F4Label.place(x=100, y=115)

FilterOrder = Tkinter.Label(MainWindow)
FilterOrder.place(x=10, y=140)

DrawCheckButton = Tkinter.Checkbutton(MainWindow, text="Draw", variable=DrawCheckButtonVar, onvalue=1, offvalue=0)
DrawCheckButton.place(x=10, y=90)

LowOrHighPassRadioButtonPressed()

MainWindow.mainloop()

import math
import sys
if sys.version[0] == '3':
    import tkinter as Tkinter
else:
    import Tkinter as Tkinter

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


def DrawHejwt(canvas, H, minFreq, maxFreq, fs, N, width, height):
    global drawOffset
    canvas.delete("all")
    offsetBetweenDiagrams=50
    # vertical lines
    canvas.create_line(0*width/8+40, 0,0*width/8+40, 40*8, fill="gray", width=1)
    canvas.create_line(1 * width / 8+40, 0, 1 * width / 8+40, 40*8, fill="gray", width=1)
    canvas.create_line(2 * width / 8+40, 0, 2 * width / 8+40, 40*8, fill="gray", width=1)
    canvas.create_line(3 * width / 8+40, 0, 3 * width / 8+40, 40*8, fill="gray", width=1)
    canvas.create_line(4 * width / 8+40, 0, 4 * width / 8+40, 40*8, fill="gray", width=1)
    canvas.create_line(5 * width / 8+40, 0, 5 * width / 8+40, 40*8, fill="gray", width=1)
    canvas.create_line(6 * width / 8+40, 0, 6 * width / 8+40, 40*8, fill="gray", width=1)
    canvas.create_line(7 * width / 8+40, 0, 7 * width / 8+40, 40*8, fill="gray", width=1)
    canvas.create_line(8*width/8+40, 0, 8*width/8+40, 40*8, fill="gray", width=1)

    #horizontal lines
    canvas.create_line(40, 1 * 40, width+40, 1 * 40, fill="gray", width=1)
    canvas.create_line(40, 2 * 40, width+40, 2 * 40, fill="gray", width=1)
    canvas.create_line(40, 3 * 40, width+40, 3 * 40, fill="gray", width=1)
    canvas.create_line(40, 4 * 40, width+40, 4 * 40, fill="gray", width=1)
    canvas.create_line(40, 5 * 40, width+40, 5 * 40, fill="gray", width=1)
    canvas.create_line(40, 6 * 40, width+40, 6 * 40, fill="gray", width=1)
    canvas.create_line(40, 7 * 40, width+40, 7 * 40, fill="gray", width=1)
    canvas.create_line(40, 8 * 40, width+40, 8 * 40, fill="gray", width=1)

    #texts
    canvas.create_text(1 * width / 8+40, height - 5+offset, text=str(1 * (maxFreq - minFreq) / 8+minFreq))
    canvas.create_text(2 * width / 8+40, height - 5+offset, text=str(2 * (maxFreq - minFreq) / 8+minFreq))
    canvas.create_text(3 * width / 8+40, height - 5+offset, text=str(3 * (maxFreq - minFreq) / 8+minFreq))
    canvas.create_text(4 * width / 8+40, height - 5+offset, text=str(4 * (maxFreq - minFreq) / 8+minFreq))
    canvas.create_text(5 * width / 8+40, height - 5+offset, text=str(5 * (maxFreq - minFreq) / 8+minFreq))
    canvas.create_text(6 * width / 8+40, height - 5+offset, text=str(6 * (maxFreq - minFreq) / 8+minFreq))
    canvas.create_text(7 * width / 8+40, height - 5+offset, text=str(7 * (maxFreq - minFreq) / 8+minFreq))

    canvas.create_text(20, 1*40, text="0 dB")
    canvas.create_text(20, 2*40, text="-20 dB")
    canvas.create_text(20, 3*40, text="-40 dB")
    canvas.create_text(20, 4*40, text="-60 dB")
    canvas.create_text(20, 5*40, text="-80 dB")
    canvas.create_text(20, 6*40, text="-100 dB")
    canvas.create_text(20, 7*40, text="-120 dB")
    canvas.create_text(20, 8*40, text="-140 dB")


    canvas.create_line(40, 110+8*40, width+40, 110+8*40, fill="gray", width=1)
    canvas.create_line(40, 200+8*40, width+40, 200+8*40, fill="gray", width=1)
    canvas.create_line(40, 290+8*40, width+40, 290+8*40, fill="gray", width=1)

    canvas.create_text(20, 110+8*40, text="-90 dB")
    canvas.create_text(20, 200+8*40, text="0 dB")
    canvas.create_text(20, 290+8*40, text="-90 dB")

    Offs=40
    previousAbsOrdinate=Offs
    previousAngleOrdinate=200+8*40

    FreqPix=(maxFreq-minFreq)/width
    for looper in range(0, width-1):
        temp = Offs-20*math.log10(abs(HejwtCalculate(H, N, looper*FreqPix+minFreq, 1/fs)))
        temp2 = HejwtCalculate(H, N, looper*FreqPix+minFreq, 1/fs)
        #temp2 = 300+math.degrees(math.asin(temp2.imag/temp))*100
        temp2 = 200+8*40+math.degrees(math.atan(temp2.imag/temp2.real))
        #print("angle: "+str(temp2))
        canvas.create_line(40+looper, previousAbsOrdinate, 40+looper + 1, temp, fill="blue", width=1)
        canvas.create_line(40+looper, previousAngleOrdinate, 40+looper+1, temp2, fill="blue", width=1)
        previousAbsOrdinate=temp
        previousAngleOrdinate=temp2


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
        #for looper in range(0, int(N)):
        #    print(H[looper])
        if(SaveCheckButtonVar.get()==1):
            F=open("WeightSerial.txt","w")
            for looper in range(0,len(H)):
                F.write(str(H[looper])+"\n")
            F.close()
        if(DrawCheckButtonVar.get()==1):
            global DrawerWindowWidth
            global DrawerWindowHeight
            global DrawerWindowWidthOffs
            global DrawerWindowHeightOffs
            DrawerWindow = Tkinter.Toplevel(MainWindow)
            DrawerWindow.geometry(str(DrawerWindowWidth+DrawerWindowWidthOffs)+"x"+str(2*(DrawerWindowHeight)))
            DrawerWindowHeight=300
            DrawerWindowWidth=1000

            # Creating a canvas and binding its click event to a function that places a label on the canvas with some information about the diagramm.
            Canvas1 = Tkinter.Canvas(DrawerWindow, width=DrawerWindowWidth+40, height=2*(DrawerWindowHeight+offset))
            Canvas1.place(x=0, y=0)
            Canvas1.bind('<Button-1>', lambda e: ClickOnDraw(e, H, N, SamplingFrequency,DrawerWindowWidth,DrawerWindowHeight, Canvas1,DrawerWindow))

            MinFreqEntry = Tkinter.Entry(DrawerWindow,textvariable = MinFreqEntryVar)
            MinFreqEntry.place(x=30, y=40*8+5, width=50)
            MaxFreqEntry = Tkinter.Entry(DrawerWindow, textvariable=MaxFreqEntryVar)
            MaxFreqEntry.place(x=DrawerWindowWidth - 10, y=40*8+5, width=50)
            MaxFreqEntryVar.set(str(SamplingFrequency))
            MinFreqEntryVar.set(str(0))
            ReDrawButton = Tkinter.Button(DrawerWindow, text="Re", command=lambda:DrawHejwt(Canvas1, H, float(MinFreqEntryVar.get()), float(MaxFreqEntryVar.get()), SamplingFrequency, N, DrawerWindowWidth, DrawerWindowHeight))
            ReDrawButton.place(x=5,y=5)
            MinFreqEntryVar.trace("w", lambda name, index, mode: EntryChecker(MinFreqEntryVar))
            MaxFreqEntryVar.trace("w", lambda name, index, mode: EntryChecker(MaxFreqEntryVar))

            # This line shows the 0 amplitude
            Canvas1.create_line(0, (DrawCoeff+1)*DrawerWindowHeight/2, DrawerWindowWidth, (DrawCoeff+1)*DrawerWindowHeight/2, fill="blue", width=1)
            DrawHejwt(Canvas1, H, 0, SamplingFrequency, SamplingFrequency, N, DrawerWindowWidth, DrawerWindowHeight)
    except:
        print("Exception occured")


def SecondLoadButtonPressed(Var,Var2):
    try:
        F=open(Var.get(),"r")
        File = F.read()
        F.close()
        H=[]
        looper=0
        looper2=0
        while looper < len(File):
            TemporaryStr = ""
            while((looper<len(File)) and (File[looper] != '\n')):
                TemporaryStr+=(File[looper])
                looper+=1
            H.append(float(TemporaryStr))
            looper += 1
            looper2+=1
        N=looper2
        global DrawerWindowWidth
        global DrawerWindowHeight
        global DrawerWindowWidthOffs
        global DrawerWindowHeightOffs
        DrawerWindow = Tkinter.Toplevel(MainWindow)
        DrawerWindow.geometry(str(DrawerWindowWidth+DrawerWindowWidthOffs)+"x"+str(2*(DrawerWindowHeight)))
        DrawerWindowHeight = 300
        DrawerWindowWidth = 1000

        # Creating a canvas and binding its click event to a function that places a label on the canvas with some information about the diagramm.
        Canvas1 = Tkinter.Canvas(DrawerWindow, width=DrawerWindowWidth+40, height=2*(DrawerWindowHeight+offset))
        Canvas1.place(x=0, y=0)
        Canvas1.bind('<Button-1>', lambda e: ClickOnDraw(e, H, N, float(Var2.get()), DrawerWindowWidth, DrawerWindowHeight, Canvas1,DrawerWindow))

        MinFreqEntry = Tkinter.Entry(DrawerWindow, textvariable=MinFreqEntryVar)
        MinFreqEntry.place(x=30, y=40*8+5, width=50)
        MaxFreqEntry = Tkinter.Entry(DrawerWindow, textvariable=MaxFreqEntryVar)
        MaxFreqEntry.place(x=DrawerWindowWidth-10, y=40*8+5, width=50)
        MaxFreqEntryVar.set(str(float(Var2.get())))
        MinFreqEntryVar.set(str(0))
        ReDrawButton = Tkinter.Button(DrawerWindow, text="Re",
                                      command=lambda: DrawHejwt(Canvas1, H, float(MinFreqEntryVar.get()), float(MaxFreqEntryVar.get()), SamplingFrequency, N, DrawerWindowWidth, DrawerWindowHeight))
        ReDrawButton.place(x=5, y=5)
        MinFreqEntryVar.trace("w", lambda name, index, mode: EntryChecker(MinFreqEntryVar))
        MaxFreqEntryVar.trace("w", lambda name, index, mode: EntryChecker(MaxFreqEntryVar))

        # This line shows the 0 amplitude
        Canvas1.create_line(0, (DrawCoeff+1)*DrawerWindowHeight/2, DrawerWindowWidth, (DrawCoeff+1)*DrawerWindowHeight/2, fill="blue", width=1)
        DrawHejwt(Canvas1, H, 0, float(Var2.get()), float(Var2.get()), N, DrawerWindowWidth, DrawerWindowHeight)
    except:
        Var.set("P")

def LoadButtonPressed():
    LoaderWindow = Tkinter.Toplevel(MainWindow)
    LoaderWindow.geometry("300x50")
    LoaderEntryVar = Tkinter.StringVar()
    LoaderEntry = Tkinter.Entry(LoaderWindow, width=35,textvariable=LoaderEntryVar)
    LoaderEntry.place(x=0,y=0)
    LoaderSamplingFreqEntryVar = Tkinter.StringVar()
    LoaderSamplingFreqEntry = Tkinter.Entry(LoaderWindow, width=10,textvariable=LoaderSamplingFreqEntryVar)
    LoaderSamplingFreqEntry.place(x=230,y=0)
    LoaderSamplingFreqEntryVar.trace("w", lambda name, index, mode: EntryChecker(LoaderSamplingFreqEntryVar))
    LB=Tkinter.Button(LoaderWindow, text="Load",command=lambda:SecondLoadButtonPressed(LoaderEntryVar,LoaderSamplingFreqEntryVar))
    LB.place(x=0,y=20)


# This function deletes the helper lines with information label from the canvas if right mouse click occures on it.
def DeleteHelperLine(ClickEvent, Canvas):
    for looper in range(0, len(ValueLabelArray)):
        if(ValueLabelArray[looper][0] == ClickEvent.widget):
            ValueLabelArray[looper][0].destroy()
            Canvas.delete(ValueLabelArray[looper][1])
            ValueLabelArray.remove(ValueLabelArray[looper])
            break


# This function implements the drawing of the helper lines and information labels.
def ClickOnDraw(ClickEvent, H, N, WindowMaxFreq, CanvasWidth, CanvasHeight, DrawableCanvas,DrawerWindow):
    # It shows the amplitude in dB
    FreqPix = (float(MaxFreqEntryVar.get())-float(MinFreqEntryVar.get())) / CanvasWidth
    t=HejwtCalculate(H, N, (ClickEvent.x-40) * FreqPix+float(MinFreqEntryVar.get()), 1 / WindowMaxFreq)
    temp = abs(t)
    temp = 20*math.log10(temp)
    TemporaryLabel = Tkinter.Label(DrawerWindow, text="A="+str(round(temp,3))+"\nD="+str(round(math.degrees(math.atan(t.imag/t.real)),3))+"\nf="+str(round((ClickEvent.x-40) * FreqPix+float(MinFreqEntryVar.get()))))
    TemporaryLine = DrawableCanvas.create_line(ClickEvent.x, 0, ClickEvent.x, 290+8*40, fill="#ff9900", width=1)
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

DrawerWindowHeight = 320
DrawerWindowWidth = 1000
DrawerWindowHeightOffs = 40
DrawerWindowWidthOffs = 45
MainWindow = Tkinter.Tk()
MainWindow.geometry("350x200")
offset = 40
# Initialization of the widget variables
RadioButtonSelectorVariable = Tkinter.IntVar()
DrawCheckButtonVar = Tkinter.IntVar()
SaveCheckButtonVar = Tkinter.IntVar()
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

StartButton = Tkinter.Button(MainWindow, text="Start", command=StartButtonPressed).place(x=35, y=135, width=38)
LoadButton = Tkinter.Button(MainWindow, text="Load", command=LoadButtonPressed).place(x=35, y=165,width=38)
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
SaveCheckButton = Tkinter.Checkbutton(MainWindow, text="Save", variable=SaveCheckButtonVar, onvalue=1, offvalue=0)
SaveCheckButton.place(x=10, y=108)

LowOrHighPassRadioButtonPressed()

MainWindow.mainloop()
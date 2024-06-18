import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import font as tkfont
import numpy as np
from open_program import run_program

def is_decimal_string(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def on_combo_configure(event): # Function to adjust the width of the combobox based on the longest string in the list
    combo = event.widget
    style = ttk.Style()
    long = max(combo.cget('values'), key=len)

    font = tkfont.nametofont(str(combo.cget('font')))
    width = max(0,font.measure(long.strip() + '0') - combo.winfo_width())

    style.configure('TCombobox', postoffset=(0,0,width,0))

# Function to update the values of the list based on the user input
def update_values(var,indx,mode,arr,val,i):
    if len(arr)>0:
        if len(arr)==i:
            arr.pop()
            arr.append(val)
        elif len(arr)>i:
            arr.pop(i-1)
            arr.insert(i-1,val)
        else:
            arr.append(val)
    else:
        if i==1:
            arr.append(val)
        else:
            for j in range(i-1):
                arr.append('')
            arr.append(val)
    print(arr)
    return


        
# Function to show or hide additional fields based on the TURBO_TYP selection
def update_turbo_typ():
    turbo_typ = turbo_typ_var.get()
    return

#variables for the stage fields: axial flow machines
intype_axi=[]
statorin_angle=[]
statorex_angle=[]
rotorin_angle=[]
rotorex_angle=[]
stage_reaction=[]
rad_typ=[]
dirInput_designRadius=[]
stage_enthalpy_change=[]
blade_axialChord1=[]
blade_axialChord2=[]
rowGap=[]
stageGap=[]
flow_coeff=[]
stage_loading_coeff=[]
stagein_angle=[]
stageex_angle=[]
fblock_le=[]
fblock_te=[]
isentropic_efficiency=[]
dev1=[]
dev2=[]
incid1=[]
incid2=[]
blade_twist=[]
blade_rotation=[]
bld_rot_angle=[]
q01_le=[]
q01_te=[]
q02_le=[]
q02_te=[]
copy_stage=[]






   

def stage_values_axi(i): # Function to get the values of the stage parameters for axial flow machines
    
    stage = tk.Toplevel()
    stage.title(f"Stage {i+1}")
    stage.geometry("1366x768")
    i=i+1

    def copy_function(*args):
        if copyPrevious.get()==1: # Copy the values from the previous stage
            blade_axialChord1.pop()
            blade_axialChord2.pop()
            rowGap.pop()
            stageGap.pop()
            isentropic_efficiency.pop()
            dev1.pop()
            dev2.pop()
            incid1.pop()
            incid2.pop()
            q01_le.pop()
            q01_te.pop()
            q02_le.pop()
            q02_te.pop()
            update_values(0,0,0,copy_stage,'Y',i)
            update_values(0,0,0,intype_axi,intype_axi[-1],i)
            entry_intype_axi.set(intype_axi[-1])
            if intype_axi[-1] == "A. Reaction, flow coefficient and stage loading coefficient":
                entry_stage_reaction.insert(0,stage_reaction[-1])
                update_values(0,0,0,stage_reaction,stage_reaction[-1],i)
                entry_flow_coeff.insert(0,flow_coeff[-1])
                update_values(0,0,0,flow_coeff,flow_coeff[-1],i)
                entry_stage_loading_coeff.insert(0,stage_loading_coeff[-1])
                update_values(0,0,0,stage_loading_coeff,stage_loading_coeff[-1],i)
            elif intype_axi[-1] == "B. Flow coefficient, stator and rotor exit angles":
                entry_flow_coeff.insert(0,flow_coeff[-1])
                update_values(0,0,0,flow_coeff,flow_coeff[-1],i)
                entry_statorex_angle.insert(0,statorex_angle[-1])
                update_values(0,0,0,statorex_angle,statorex_angle[-1],i)
                entry_rotorex_angle.insert(0,rotorex_angle[-1])
                update_values(0,0,0,rotorex_angle,rotorex_angle[-1],i)
            elif intype_axi[-1] == "C. flow coefficient, rotor inlet and exit angles":
                entry_flow_coeff.insert(0,flow_coeff[-1])
                update_values(0,0,0,flow_coeff,flow_coeff[-1],i)
                entry_rotorin_angle.insert(0,rotorin_angle[-1])
                update_values(0,0,0,rotorin_angle,rotorin_angle[-1],i)
                entry_rotorex_angle.insert(0,rotorex_angle[-1])
                update_values(0,0,0,rotorex_angle,rotorex_angle[-1],i)
            elif intype_axi[-1] == "D. Stage reaction, first blade row inlet and exit angles":
                entry_stage_reaction.insert(0,stage_reaction[-1])
                update_values(0,0,0,stage_reaction,stage_reaction[-1],i)
                entry_statorin_angle.insert(0,statorin_angle[-1])
                update_values(0,0,0,statorin_angle,statorin_angle[-1],i)
                entry_statorex_angle.insert(0,statorex_angle[-1])
                update_values(0,0,0,statorex_angle,statorex_angle[-1],i)
            entry_set_designRadius.set(rad_typ[-1])
            if rad_typ[-1]=="A. Input design radius directly":
                entry_dirInput_designRadius.insert(0, dirInput_designRadius[-1])
                update_values(0,0,0,dirInput_designRadius,dirInput_designRadius[-1],i)
            elif rad_typ[-1]=="B. Input stage enthalpy change":
                entry_stage_enthalpy_change.insert(0, stage_enthalpy_change[-1])
                update_values(0,0,0,stage_enthalpy_change,stage_enthalpy_change[-1],i)
            entry_blade_axialChord1.insert(0, blade_axialChord1[-1])
            update_values(0,0,0,blade_axialChord1,blade_axialChord1[-1],i)
            entry_blade_axialChord2.insert(0,blade_axialChord2[-1])
            update_values(0,0,0,blade_axialChord2,blade_axialChord2[-1],i)
            entry_rowGap.insert(0, rowGap[-1])
            update_values(0,0,0,rowGap,rowGap[-1],i)
            entry_stageGap.insert(0, stageGap[-1])
            update_values(0,0,0,stageGap,stageGap[-1],i)
            entry_guess_efficiency.insert(0, isentropic_efficiency[-1])
            update_values(0,0,0,isentropic_efficiency,isentropic_efficiency[-1],i)
            entry_dev1.insert(0, dev1[-1])
            update_values(0,0,0,dev1,dev1[-1],i)
            entry_dev2.insert(0, dev2[-1])
            update_values(0,0,0,dev2,dev2[-1],i)
            entry_incid1.insert(0,incid1[-1])
            update_values(0,0,0,incid1,incid1[-1],i)
            entry_incid2.insert(0,incid2[-1])
            update_values(0,0,0,incid2,incid2[-1],i)
            entry_blade_twist.insert(0,blade_twist[-1])
            update_values(0,0,0,blade_twist,blade_twist[-1],i)
            update_values(0,0,0,blade_rotation,blade_rotation[-1],i)
            if blade_rotation[-1]=="Y":
                entry_bldRot_yes.select()
            else:
                entry_bldRot_no.select()
            entry_q01_le.insert(0, q01_le[-1])
            update_values(0,0,0,q01_le,q01_le[-1],i)
            entry_q01_te.insert(0, q01_te[-1])
            update_values(0,0,0,q01_te,q01_te[-1],i)
            entry_q02_le.insert(0, q02_le[-1])
            update_values(0,0,0,q02_le,q02_le[-1],i)
            entry_q02_te.insert(0, q02_te[-1])
            update_values(0,0,0,q02_te,q02_te[-1],i)
        else: 
            copy_stage.append('N')
        return
    
    if i==1:
        intype_axi.clear()
        statorin_angle.clear()
        statorex_angle.clear()
        rotorin_angle.clear()
        rotorex_angle.clear()
        stage_reaction.clear()
        flow_coeff.clear()
        stage_loading_coeff.clear()
        stagein_angle.clear()
        stageex_angle.clear()
        fblock_le.clear()
        fblock_te.clear()
        isentropic_efficiency.clear()
        rad_typ.clear()
        dirInput_designRadius.clear()
        stage_enthalpy_change.clear()
        blade_axialChord1.clear()
        blade_axialChord2.clear()
        rowGap.clear()
        stageGap.clear()
        dev1.clear()
        dev2.clear()
        incid1.clear()
        incid2.clear()
        blade_twist.clear()
        blade_rotation.clear()
        q01_le.clear()
        q01_te.clear()
        q02_le.clear()
        q02_te.clear()
        copy_stage.clear()
    else:
        copyPrevious= tk.IntVar()
        check_copyPrevious = tk.Checkbutton(stage, text="Do you want to repeat the last stage input type and velocity triangles?", variable=copyPrevious, onvalue=1, offvalue=0)
        check_copyPrevious.grid(row=0, column=4, pady=5)
        copyPrevious.set(0)
        copyPrevious.trace_add('write', copy_function )
    

    def update_intype_axi(event): # Function to show or hide additional fields based on the INTYPE selection for axial flow machines
        intype = entry_intype_axi.get()
        if intype == "A. Reaction, flow coefficient and stage loading coefficient":
            label_stage_reaction.grid(row=1, column=0, pady=5)
            entry_stage_reaction.grid(row=1, column=1, pady=5)
            label_flow_coeff.grid(row=2, column=0, pady=5)
            entry_flow_coeff.grid(row=2, column=1, pady=5)
            label_stage_loading_coeff.grid(row=3, column=0, pady=5)
            entry_stage_loading_coeff.grid(row=3, column=1, pady=5)
            label_statorin_angle.grid_forget()
            entry_statorin_angle.grid_forget()
            label_statorex_angle.grid_forget()
            entry_statorex_angle.grid_forget()
            label_rotorin_angle.grid_forget()
            entry_rotorin_angle.grid_forget()
            label_rotorex_angle.grid_forget()
            entry_rotorex_angle.grid_forget()
        elif intype == "B. Flow coefficient, stator and rotor exit angles":
            label_flow_coeff.grid(row=1, column=0, pady=5)
            entry_flow_coeff.grid(row=1, column=1, pady=5)
            label_statorex_angle.grid(row=2, column=0, pady=5)
            entry_statorex_angle.grid(row=2, column=1, pady=5)
            label_rotorex_angle.grid(row=3, column=0, pady=5)
            entry_rotorex_angle.grid(row=3, column=1, pady=5)
            label_stage_reaction.grid_forget()
            entry_stage_reaction.grid_forget()
            label_stage_loading_coeff.grid_forget()
            entry_stage_loading_coeff.grid_forget()
            label_statorin_angle.grid_forget()
            entry_statorin_angle.grid_forget()
            label_rotorin_angle.grid_forget()
            entry_rotorin_angle.grid_forget()
        elif intype == "C. flow coefficient, rotor inlet and exit angles":
            label_flow_coeff.grid(row=1, column=0, pady=5)
            entry_flow_coeff.grid(row=1, column=1, pady=5)
            label_rotorin_angle.grid(row=2, column=0, pady=5)
            entry_rotorin_angle.grid(row=2, column=1, pady=5)
            label_rotorex_angle.grid(row=3, column=0, pady=5)
            entry_rotorex_angle.grid(row=3, column=1, pady=5)
            label_stage_reaction.grid_forget()
            entry_stage_reaction.grid_forget()
            label_stage_loading_coeff.grid_forget()
            entry_stage_loading_coeff.grid_forget()
            label_statorin_angle.grid_forget()
            entry_statorin_angle.grid_forget()
            label_statorex_angle.grid_forget()
            entry_statorex_angle.grid_forget()
        elif intype == "D. Stage reaction, first blade row inlet and exit angles":
            label_stage_reaction.grid(row=1, column=0, pady=5)
            entry_stage_reaction.grid(row=1, column=1, pady=5)

            label_statorin_angle.grid(row=2, column=0, pady=5)
            entry_statorin_angle.grid(row=2, column=1, pady=5)
            label_statorex_angle.grid(row=3, column=0, pady=5)
            entry_statorex_angle.grid(row=3, column=1, pady=5)
            label_rotorin_angle.grid_forget()
            entry_rotorin_angle.grid_forget()
            label_rotorex_angle.grid_forget()
            entry_rotorex_angle.grid_forget()
            label_flow_coeff.grid_forget()
            entry_flow_coeff.grid_forget()
            label_stage_loading_coeff.grid_forget()
        else:
            label_statorin_angle.grid_forget()
            entry_statorin_angle.grid_forget()
            label_statorex_angle.grid_forget()
            entry_statorex_angle.grid_forget()
            label_rotorin_angle.grid_forget()
            entry_rotorin_angle.grid_forget()
            label_rotorex_angle.grid_forget()
            entry_rotorex_angle.grid_forget()
            label_stage_reaction.grid_forget()
            entry_stage_reaction.grid_forget()
            label_flow_coeff.grid_forget()
            entry_flow_coeff.grid_forget()
            label_stage_loading_coeff.grid_forget()
            entry_stage_loading_coeff.grid_forget()

    def update_designRadius_method(event):
        designRadius_method = entry_set_designRadius.get()
        if designRadius_method == "A. Input design radius directly":
            label_dirInput_designRadius.grid(row=5, column=0, pady=5)
            entry_dirInput_designRadius.grid(row=5, column=1, pady=5)
            label_stage_enthalpy_change.grid_forget()
            entry_stage_enthalpy_change.grid_forget()
        elif designRadius_method == "B. Input stage enthalpy change":
            label_stage_enthalpy_change.grid(row=5, column=0, pady=5)
            entry_stage_enthalpy_change.grid(row=5, column=1, pady=5)
            label_dirInput_designRadius.grid_forget()
            entry_dirInput_designRadius.grid_forget()
        else:
            label_dirInput_designRadius.grid_forget()
            entry_dirInput_designRadius.grid_forget()
            label_stage_enthalpy_change.grid_forget()
            entry_stage_enthalpy_change.grid_forget()

    
    def combined_handler1(event):
        update_intype_axi(event)
        update_values(event,0,0,intype_axi,entry_intype_axi.get(),i)
    
    label_intype = tk.Label(stage, text="Velocity triangle inputs chosen:") # Label for the inlet type
    entry_intype_axi = ttk.Combobox(stage, values=["A. Reaction, flow coefficient and stage loading coefficient","B. Flow coefficient, stator and rotor exit angles",
                                              "C. flow coefficient, rotor inlet and exit angles", "D. Stage reaction, first blade row inlet and exit angles"],
                                                state="readonly",width=30)
    
    label_intype.grid(row=0, column=0, pady=5)
    entry_intype_axi.grid(row=0, column=1, pady=5)
    entry_intype_axi.set(" Select the velocity triangle inputs chosen")
    entry_intype_axi.bind("<ButtonPress>", on_combo_configure)
    entry_intype_axi.bind("<<ComboboxSelected>>", combined_handler1)
    
    update_statorin_angle = tk.StringVar()
    label_statorin_angle= tk.Label(stage, text="Stator Inlet Angle (in deg):") # Label for the stator inlet angle
    entry_statorin_angle = tk.Entry(stage, textvariable=update_statorin_angle)
    update_statorin_angle.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,statorin_angle,update_statorin_angle.get(),i) )
    
    update_statorex_angle = tk.StringVar()
    label_statorex_angle= tk.Label(stage, text="Stator Exit Angle (in deg):") # Label for the stator exit angle
    entry_statorex_angle = tk.Entry(stage, textvariable=update_statorex_angle)
    update_statorex_angle.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,statorex_angle,update_statorex_angle.get(),i) )

    update_rotorin_angle = tk.StringVar()
    label_rotorin_angle= tk.Label(stage, text="Rotor Inlet Angle (in deg):") # Label for the rotor inlet angle
    entry_rotorin_angle = tk.Entry(stage, textvariable=update_rotorin_angle)
    update_rotorin_angle.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,rotorin_angle,update_rotorin_angle.get(),i) )

    update_rotorex_angle = tk.StringVar()
    label_rotorex_angle= tk.Label(stage, text="Rotor Exit Angle (in deg):") # Label for the rotor exit angle
    entry_rotorex_angle = tk.Entry(stage,textvariable=update_rotorex_angle)
    update_rotorex_angle.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,rotorex_angle,update_rotorex_angle.get(),i) )

    update_stage_reaction = tk.StringVar()
    label_stage_reaction= tk.Label(stage, text="Stage Reaction:") # Label for the stage reaction
    entry_stage_reaction = tk.Entry(stage, textvariable=update_stage_reaction)
    update_stage_reaction.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,stage_reaction,update_stage_reaction.get(),i) )

    update_flow_coeff = tk.StringVar()
    label_flow_coeff= tk.Label(stage, text="Flow Coefficient:") # Label for the flow coefficient
    entry_flow_coeff = tk.Entry(stage, textvariable=update_flow_coeff)
    update_flow_coeff.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,flow_coeff,update_flow_coeff.get(),i) )

    update_stage_loading_coeff = tk.StringVar()
    label_stage_loading_coeff= tk.Label(stage, text="Stage Loading Coefficient:") # Label for the stage loading coefficient
    entry_stage_loading_coeff = tk.Entry(stage,textvariable=update_stage_loading_coeff)
    update_stage_loading_coeff.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,stage_loading_coeff,update_stage_loading_coeff.get(),i) )


    def combined_handler2(event):
        update_designRadius_method(event)
        update_values(event,0,0,rad_typ,entry_set_designRadius.get(),i)
    
    label_set_designRadius = tk.Label(stage, text="Method to set the design radius:") # Label for the base radius
    label_set_designRadius.grid(row=4, column=0, pady=5)
    entry_set_designRadius = ttk.Combobox(stage, values=["A. Input design radius directly", "B. Input stage enthalpy change"], state="readonly",width=30)
    entry_set_designRadius.set(" Select the method to choose design point radius")
    entry_set_designRadius.grid(row=4, column=1, pady=5)
    entry_set_designRadius.bind("<ButtonPress>", on_combo_configure)
    entry_set_designRadius.bind("<<ComboboxSelected>>", combined_handler2)

    update_dirInput_designRadius = tk.StringVar()
    label_dirInput_designRadius = tk.Label(stage, text="Design Point Radius (in m):") # Label to input the design point radius directly
    entry_dirInput_designRadius = tk.Entry(stage, textvariable=update_dirInput_designRadius)
    update_dirInput_designRadius.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,dirInput_designRadius,update_dirInput_designRadius.get(),i) )

    update_stage_enthalpy_change = tk.StringVar()
    label_stage_enthalpy_change = tk.Label(stage, text="Stage Enthalpy Change (in J/kg):") # Label to input the stage enthalpy change
    entry_stage_enthalpy_change = tk.Entry(stage, textvariable=update_stage_enthalpy_change)
    update_stage_enthalpy_change.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,stage_enthalpy_change,update_stage_enthalpy_change.get(),i) )

    update_blade_axialChord1 = tk.StringVar()
    label_blade_axialChord1= tk.Label(stage, text="First Blade Axial Chord (in m):") # Label for the first blade axial chord
    label_blade_axialChord1.grid(row=6, column=0, pady=5)
    entry_blade_axialChord1 = tk.Entry(stage, textvariable=update_blade_axialChord1)
    entry_blade_axialChord1.grid(row=6, column=1, pady=5)
    update_blade_axialChord1.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,blade_axialChord1,update_blade_axialChord1.get(),i) )

    update_blade_axialChord2 = tk.StringVar()
    label_blade_axialChord2= tk.Label(stage, text="Second Blade Axial Chord (in m):") # Label for the second blade axial chord
    label_blade_axialChord2.grid(row=7, column=0, pady=5)
    entry_blade_axialChord2 = tk.Entry(stage, textvariable=update_blade_axialChord2)
    entry_blade_axialChord2.grid(row=7, column=1, pady=5)
    update_blade_axialChord2.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,blade_axialChord2,update_blade_axialChord2.get(),i) )


    update_rowGap = tk.StringVar()
    label_rowGap= tk.Label(stage, text="Row Gap (as fractions of first row axial chords):") # Label for the row gap
    label_rowGap.grid(row=8, column=0, pady=5)
    entry_rowGap = tk.Entry(stage, textvariable=update_rowGap)
    entry_rowGap.grid(row=8, column=1, pady=5)
    update_rowGap.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,rowGap,update_rowGap.get(),i) )

    update_stageGap = tk.StringVar()
    label_stageGap = tk.Label(stage, text="Stage Gap (as fractions of first row axial chords):") # Label for the stage gap
    label_stageGap.grid(row=9, column=0, pady=5)
    entry_stageGap = tk.Entry(stage, textvariable=update_stageGap)
    entry_stageGap.grid(row=9, column=1, pady=5)
    update_stageGap.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,stageGap,update_stageGap.get(),i) )

    bf_le= tk.StringVar()
    label_bloc_le = tk.Label(stage, text="Blockage factors at the Leading Edges of 1st blade row :") # Label for the blockage factor at the leading edges of the first blade row
    label_bloc_le.grid(row=10, column=0, pady=5)
    entry_bloc_le = tk.Entry(stage, textvariable=bf_le)
    entry_bloc_le.grid(row=10, column=1, pady=5)
    bf_le.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,fblock_le,bf_le.get(),i) )

    bf_te= tk.StringVar()
    label_bloc_te = tk.Label(stage, text="and at the Trailing Edges of 2nd blade row:") # Label for the blockage factor at the trailing edges of the second blade row
    label_bloc_te.grid(row=10, column=2, pady=5)
    entry_bloc_te = tk.Entry(stage, textvariable=bf_te)
    entry_bloc_te.grid(row=10, column=3, pady=5)
    bf_te.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,fblock_te,bf_te.get(),i) )

    update_guess_efficiency = tk.StringVar()
    label_guess_efficiency = tk.Label(stage, text="Guess of stage isentropic Efficiency:") # Label for the guess efficiency
    label_guess_efficiency.grid(row=11, column=0, pady=5)
    entry_guess_efficiency = tk.Entry(stage, textvariable=update_guess_efficiency)
    entry_guess_efficiency.grid(row=11, column=1, pady=5)
    def validate_entries(var,indx,mode,arr,val,entry):
        if is_decimal_string(val):
            if float(val) >= 0 and float(val) <= 1:
                update_values(var,indx,mode,arr,val,i)
            else:
                messagebox.showerror("Error", "Please enter a valid number between 0 and 1")
                entry.delete(0, tk.END) # Clear the entry field
        else:
            messagebox.showerror("Error", "Please enter a valid number")
            entry.delete(0, tk.END)

    update_guess_efficiency.trace_add('write', lambda var,indx,mode: validate_entries(var,indx,mode,isentropic_efficiency,update_guess_efficiency.get(),entry_guess_efficiency) )

    update_dev1 = tk.StringVar()   
    label_dev1 = tk.Label(stage, text="Deviation angle 1st row (in deg):") # Label for the deviation angle of the first row
    label_dev1.grid(row=12, column=0, pady=5)
    entry_dev1 = tk.Entry(stage, textvariable=update_dev1)
    entry_dev1.grid(row=12, column=1, pady=5)
    update_dev1.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,dev1,update_dev1.get(),i) )

    update_dev2 = tk.StringVar()
    label_dev2 = tk.Label(stage, text="Deviation angle 2nd row (in deg):") # Label for the deviation angle of the second row
    label_dev2.grid(row=13, column=0, pady=5)
    entry_dev2 = tk.Entry(stage, textvariable=update_dev2)
    entry_dev2.grid(row=13, column=1, pady=5)
    update_dev2.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,dev2,update_dev2.get(),i) )

    update_incid1 = tk.StringVar()
    label_incid1 = tk.Label(stage, text="Incidence angle 1st row (in deg):") # Label for the incidence angle of the first row
    label_incid1.grid(row=14, column=0, pady=5)
    entry_incid1 = tk.Entry(stage, textvariable=update_incid1)
    entry_incid1.grid(row=14, column=1, pady=5)
    update_incid1.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,incid1,update_incid1.get(),i) )

    update_incid2 = tk.StringVar()
    label_incid2 = tk.Label(stage, text="Incidence angle 2nd row (in deg):") # Label for the incidence angle of the second row
    label_incid2.grid(row=15, column=0, pady=5)
    entry_incid2 = tk.Entry(stage, textvariable=update_incid2)
    entry_incid2.grid(row=15, column=1, pady=5)
    update_incid2.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,incid2,update_incid2.get(),i) )

    textval_bt = tk.StringVar()
    label_blade_twist = tk.Label(stage, text="Blade twist option :") # Label for the blade twist angle
    label_blade_twist.grid(row=16, column=0, pady=5)
    entry_blade_twist = tk.Entry(stage, textvariable=textval_bt)
    entry_blade_twist.grid(row=16, column=1, pady=5)

    
    textval_bt.trace_add('write', lambda var,indx,mode: validate_entries(var,indx,mode,blade_twist,textval_bt.get(),entry_blade_twist) )

    
    blrot_value = tk.StringVar()
    label_blade_rotation = tk.Label(stage, text="Blade rotation option :") # Label for the blade rotation angle
    label_blade_rotation.grid(row=17, column=0, pady=5)
    entry_bldRot_yes = tk.Radiobutton(stage, text="Yes", variable=blrot_value, value="Y")
    entry_bldRot_yes.grid(row=17, column=1, pady=5)
    entry_bldRot_no = tk.Radiobutton(stage, text="No", variable=blrot_value, value="N")
    entry_bldRot_no.grid(row=18, column=1, pady=5)
    blrot_value.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,blade_rotation,blrot_value.get(),i) )

    update_q01_le = tk.StringVar()
    label_q01_le = tk.Label(stage, text="Q0 at LE of Row 1 (in deg):") # Label for the Q0 angle at the leading edge of the first row
    label_q01_le.grid(row=19, column=0, pady=5)
    entry_q01_le = tk.Entry(stage, textvariable=update_q01_le)
    entry_q01_le.grid(row=19, column=1, pady=5)
    update_q01_le.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,q01_le,update_q01_le.get(),i) )

    update_q01_te= tk.StringVar()
    label_q01_te = tk.Label(stage, text="Q0 at TE of Row 1 (in deg):") # Label for the Q0 angle at the trailing edge of the first row
    label_q01_te.grid(row=20, column=0, pady=5)
    entry_q01_te = tk.Entry(stage, textvariable=update_q01_te)
    entry_q01_te.grid(row=20, column=1, pady=5)
    update_q01_te.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,q01_te,update_q01_te.get(),i) )

    update_q02_le = tk.StringVar()
    label_q02_le = tk.Label(stage, text="Q0 at LE of Row 2 (in deg):") # Label for the Q0 angle at the leading edge of the second row
    label_q02_le.grid(row=1, column=2, pady=5)
    entry_q02_le = tk.Entry(stage, textvariable=update_q02_le)
    entry_q02_le.grid(row=1, column=3, pady=5)
    update_q02_le.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,q02_le,update_q02_le.get(),i) )

    update_q02_te = tk.StringVar()
    label_q02_te = tk.Label(stage, text="Q0 at TE of Row 2 (in deg):") # Label for the Q0 angle at the trailing edge of the second row
    label_q02_te.grid(row=2, column=2, pady=5)
    entry_q02_te = tk.Entry(stage, textvariable=update_q02_te)
    entry_q02_te.grid(row=2, column=3, pady=5)
    update_q02_te.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,q02_te,update_q02_te.get(),i) )

    entry_blade_axialChord1.insert(0, "0.05")
    entry_blade_axialChord2.insert(0, "0.04")
    entry_rowGap.insert(0, "0.25") 
    entry_stageGap.insert(0, "0.5") 
    entry_guess_efficiency.insert(0, "0.9")
    entry_dev1.insert(0, "5")
    entry_dev2.insert(0, "5")
    entry_incid1.insert(0, "-2")
    entry_incid2.insert(0, "-2")
    entry_bloc_le.insert(0, "0.0")
    entry_bloc_te.insert(0, "0.0")
    if (turbo_typ_var.get() == "T"):
        entry_q01_le.insert(0, "92")
        entry_q01_te.insert(0, "88")
        entry_q02_le.insert(0, "88")
        entry_q02_te.insert(0, "92")
    else:
        entry_q01_le.insert(0, "88")
        entry_q01_te.insert(0, "92")
        entry_q02_le.insert(0, "92")
        entry_q02_te.insert(0, "88")

    stage_windowButton = tk.Button(stage, text= f"Go to Stage {i+1}", command=lambda: stage_values_axi(i))
    bladerow_inputButton = tk.Button(stage, text="Go to Blade row inputs", command=blade_row_inputs)

    if i<int(nstg.get()):
        stage_windowButton.grid(row=15, column=2, columnspan=3, pady=20)
    else:
        bladerow_inputButton.grid(row=15, column=2, columnspan=3, pady=20)



#variables for the stage fields: mixed flow machines
intype_mix=[]
flow_coeff_mix=[]
stage_loading_coeff_mix=[]
stagein_angle_mix=[]
stageex_angle_mix=[]
fblock_le_mix=[]
fblock_te_mix=[]
num_points=[]
axial_coords=[]
rad_coords=[]
meridional_vel_ratios=[]
leading_trailing_edge_points=[]


def stage_values_mix(i):
    i=i+1
    stage = tk.Toplevel()
    stage.title(f"Stage {i}")
    stage.geometry("800x800")

    def copy_function(*args):
        if copyPrevious.get() == 1:
            isentropic_efficiency.pop()
            dev1.pop()
            dev2.pop()
            incid1.pop()
            incid2.pop()
            q01_le.pop()
            q01_te.pop()
            q02_le.pop()
            q02_te.pop()
            update_values(0,0,0,copy_stage,'Y',i)
            update_values(0,0,0,intype_mix,intype_mix[-1],i)
            entry_intype_mix.insert(0,intype_mix[-1])
            update_values(0,0,0,flow_coeff_mix,flow_coeff_mix[-1],i)
            entry_flow_coeff.insert(0,flow_coeff_mix[-1])
            update_values(0,0,0,stage_loading_coeff_mix,stage_loading_coeff_mix[-1],i)
            entry_stage_loading_coeff.insert(0,stage_loading_coeff_mix[-1])
            update_values(0,0,0,stagein_angle_mix,stagein_angle_mix[-1],i)
            entry_stagein_angle.insert(0,stagein_angle_mix[-1])
            update_values(0,0,0,stageex_angle_mix,stageex_angle_mix[-1],i)
            entry_stageex_angle.insert(0,stageex_angle_mix[-1])
            update_values(0,0,0,fblock_le_mix,fblock_le_mix[-1],i)
            entry_bloc_le.insert(0,fblock_le_mix[-1])
            update_values(0,0,0,fblock_te_mix,fblock_te_mix[-1],i)
            entry_bloc_te.insert(0,fblock_te_mix[-1])
            update_values(0,0,0,num_points,num_points[-1],i)
            entry_num_points.insert(0,num_points[-1])
            update_values(0,0,0,axial_coords,axial_coords[-1],i)
            temp=""
            for item in axial_coords[-1]:
                temp+=item+","
            entry_axial_coords.insert(0,temp)
            update_values(0,0,0,rad_coords,rad_coords[-1],i)
            temp=""
            for item in rad_coords[-1]:
                temp+=item+","
            entry_rad_coords.insert(0,temp)
            update_values(0,0,0,meridional_vel_ratios,meridional_vel_ratios[-1],i)
            temp=""
            for item in meridional_vel_ratios[-1]:
                temp+=item+","
            entry_meridional_vel_ratios.insert(0,temp)
            update_values(0,0,0,leading_trailing_edge_points,leading_trailing_edge_points[-1],i)
            temp=""
            for item in leading_trailing_edge_points[-1]:
                temp+=item+","
            entry_le_te_points.insert(0,temp)
            
            update_values(0,0,0,isentropic_efficiency,isentropic_efficiency[-1],i)
            entry_isefficiency.insert(0,isentropic_efficiency[-1])
            update_values(0,0,0,q01_le,q01_le[-1],i)
            entry_q01_le.insert(0, q01_le[-1])
            update_values(0,0,0,q01_te,q01_te[-1],i)
            entry_q01_te.insert(0, q01_te[-1])
            update_values(0,0,0,q02_le,q02_le[-1],i)
            entry_q02_le.insert(0, q02_le[-1])
            update_values(0,0,0,q02_te,q02_te[-1],i)
            entry_q02_te.insert(0, q02_te[-1])
            update_values(0,0,0,dev1,dev1[-1],i)
            entry_dev1.insert(0, dev1[-1])
            update_values(0,0,0,dev2,dev2[-1],i)
            entry_dev2.insert(0, dev2[-1])
            update_values(0,0,0,incid1,incid1[-1],i)
            entry_incid1.insert(0, incid1[-1])
            update_values(0,0,0,incid2,incid2[-1],i)
            entry_incid2.insert(0, incid2[-1])
            update_values(0,0,0,blade_twist,blade_twist[-1],i)
            entry_blade_twist.insert(0, blade_twist[-1])
            update_values(0,0,0,blade_rotation,blade_rotation[-1],i)
            if blade_rotation[-1] == "Y":
                entry_bldRot_yes.select()
            else:
                entry_bldRot_no.select()
        else:
            update_values(0,0,0,copy_stage,'N',i)
        
        return
            
        
            
        

    if i==1:
        intype_mix.clear()
        stagein_angle_mix.clear()
        stageex_angle_mix.clear()
        stage_reaction.clear()
        flow_coeff_mix.clear()
        statorin_angle.clear()
        statorex_angle.clear()
        rotorin_angle.clear()
        rotorex_angle.clear()
        stage_loading_coeff.clear()
        isentropic_efficiency.clear()
        dev1.clear()
        dev2.clear()
        incid1.clear()
        incid2.clear()
        blade_twist.clear()
        blade_rotation.clear()
        q01_le.clear()
        q01_te.clear()
        q02_le.clear()
        q02_te.clear()
        copy_stage.clear()
    else:
        copyPrevious= tk.IntVar()
        check_copyPrevious = tk.Checkbutton(stage, text="Do you want to repeat the last stage input type and velocity triangles?", variable=copyPrevious, onvalue=1, offvalue=0)
        check_copyPrevious.grid(row=0, column=4, pady=5)
        copyPrevious.set(0)
        copyPrevious.trace_add('write', copy_function )


    def update_intype_mix(event):
        intype = entry_intype_mix.get()
        if intype == "A. All four blade angles":
            label_statorin_angle.grid(row=1, column=0, pady=5)
            entry_statorin_angle.grid(row=1, column=1, pady=5)
            label_statorex_angle.grid(row=2, column=0, pady=5)
            entry_statorex_angle.grid(row=2, column=1, pady=5)
            label_rotorin_angle.grid(row=3, column=0, pady=5)
            entry_rotorin_angle.grid(row=3, column=1, pady=5)
            label_rotorex_angle.grid(row=4, column=0, pady=5)
            entry_rotorex_angle.grid(row=4, column=1, pady=5)
            label_stagein_angle.grid_forget()
            entry_stagein_angle.grid_forget()
            label_stageex_angle.grid_forget()
            entry_stageex_angle.grid_forget()
            label_stage_loading_coeff.grid_forget()
            entry_stage_loading_coeff.grid_forget()
        elif intype == "B. Absolute flow angles at stage inlet and outlet, and stage loading and flow coefficients":
            label_stagein_angle.grid(row=1, column=0, pady=5)
            entry_stagein_angle.grid(row=1, column=1, pady=5)
            label_stageex_angle.grid(row=2, column=0, pady=5)
            entry_stageex_angle.grid(row=2, column=1, pady=5)
            label_stage_loading_coeff.grid(row=3, column=0, pady=5)
            entry_stage_loading_coeff.grid(row=3, column=1, pady=5)
            label_flow_coeff.grid(row=4, column=0, pady=5)
            entry_flow_coeff.grid(row=4, column=1, pady=5)
            label_statorin_angle.grid_forget()
            entry_statorin_angle.grid_forget()
            label_statorex_angle.grid_forget()
            entry_statorex_angle.grid_forget()
            label_rotorin_angle.grid_forget()
            entry_rotorin_angle.grid_forget()
            label_rotorex_angle.grid_forget()
            entry_rotorex_angle.grid_forget()
        else:
            label_stagein_angle.grid_forget()
            entry_stagein_angle.grid_forget()
            label_stageex_angle.grid_forget()
            entry_stageex_angle.grid_forget()
            label_stage_loading_coeff.grid_forget()
            entry_stage_loading_coeff.grid_forget()
            label_flow_coeff.grid_forget()
            entry_flow_coeff.grid_forget()

    def combined_handler(event):
        update_intype_mix(event)
        update_values(event,0,0,intype_mix,entry_intype_mix.get(),i)

    label_intype = tk.Label(stage, text="Velocity triangle inputs chosen:") # Label for the inlet type
    entry_intype_mix = ttk.Combobox(stage, values=["A. All four blade angles","B. Absolute flow angles at stage inlet and outlet, and stage loading and flow coefficients"],
                                                state="readonly",width=30)
    label_intype.grid(row=0, column=0, pady=5)
    entry_intype_mix.grid(row=0, column=1, pady=5)
    entry_intype_mix.set(" Select the velocity triangle inputs chosen")
    entry_intype_mix.bind("<ButtonPress>", on_combo_configure)
    entry_intype_mix.bind("<<ComboboxSelected>>", combined_handler)

    update_statorin_angle = tk.StringVar()
    label_statorin_angle= tk.Label(stage, text="Stator Inlet Angle (in deg):") # Label for the stator inlet angle
    entry_statorin_angle = tk.Entry(stage, textvariable=update_statorin_angle)
    update_statorin_angle.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,statorin_angle,update_statorin_angle.get(),i) )

    update_statorex_angle = tk.StringVar()
    label_statorex_angle= tk.Label(stage, text="Stator Exit Angle (in deg):") # Label for the stator exit angle
    entry_statorex_angle = tk.Entry(stage, textvariable=update_statorex_angle)
    update_statorex_angle.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,statorex_angle,update_statorex_angle.get(),i) )

    update_rotorin_angle = tk.StringVar()
    label_rotorin_angle= tk.Label(stage, text="Rotor Inlet Angle (in deg):") # Label for the rotor inlet angle
    entry_rotorin_angle = tk.Entry(stage, textvariable=update_rotorin_angle)
    update_rotorin_angle.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,rotorin_angle,update_rotorin_angle.get(),i) )

    update_rotorex_angle = tk.StringVar()
    label_rotorex_angle= tk.Label(stage, text="Rotor Exit Angle (in deg):") # Label for the rotor exit angle
    entry_rotorex_angle = tk.Entry(stage,textvariable=update_rotorex_angle)
    update_rotorex_angle.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,rotorex_angle,update_rotorex_angle.get(),i) )

    update_stagein_angle = tk.StringVar()
    label_stagein_angle= tk.Label(stage, text="Stage Inlet Angle (in deg):") # Label for the stage inlet angle
    entry_stagein_angle = tk.Entry(stage, textvariable=update_stagein_angle)
    update_stagein_angle.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,stagein_angle_mix,update_stagein_angle.get(),i) )

    update_stageex_angle = tk.StringVar()
    label_stageex_angle= tk.Label(stage, text="Stage Exit Angle (in deg):") # Label for the stage exit angle
    entry_stageex_angle = tk.Entry(stage, textvariable=update_stageex_angle)
    update_stageex_angle.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,stageex_angle_mix,update_stageex_angle.get(),i) )

    update_stage_loading_coeff = tk.StringVar()
    label_stage_loading_coeff= tk.Label(stage, text="Stage Loading Coefficient:") # Label for the stage loading coefficient
    entry_stage_loading_coeff = tk.Entry(stage,textvariable=update_stage_loading_coeff)
    update_stage_loading_coeff.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,stage_loading_coeff_mix,update_stage_loading_coeff.get(),i) )

    update_flow_coeff = tk.StringVar()  
    label_flow_coeff= tk.Label(stage, text="Flow Coefficient:") # Label for the flow coefficient
    entry_flow_coeff = tk.Entry(stage, textvariable=update_flow_coeff)
    update_flow_coeff.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,flow_coeff_mix,update_flow_coeff.get(),i) )

    update_num_points = tk.StringVar()
    label_num_points = tk.Label(stage, text="Number of points taken on stream surface:") # Label for the number of points
    label_num_points.grid(row=6, column=0, pady=5)
    entry_num_points = tk.Entry(stage, textvariable=update_num_points)
    entry_num_points.grid(row=6, column=1, pady=5)

    def initialize_points(var,indx,mode,num_points,val,i):
        if val.isdigit():
            if int(val) > 0:
                update_values(var,indx,mode,num_points,val,i)
                label_axial_coords.grid(row=7, column=0, pady=5)
                entry_axial_coords.grid(row=7, column=1, pady=5)
                label_rad_coords.grid(row=8, column=0, pady=5)
                entry_rad_coords.grid(row=8, column=1, pady=5)
                label_meridional_vel_ratios.grid(row=9, column=0, pady=5)
                entry_meridional_vel_ratios.grid(row=9, column=1, pady=5)
            else:
                messagebox.showerror("Error", "Please enter a positive integer")
                entry_num_points.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter an integer")
            entry_num_points.delete(0, tk.END)

    update_num_points.trace_add('write', lambda var,indx,mode: initialize_points(var,indx,mode,num_points,update_num_points.get(),i) )
    
    def items_in_string(input_string):
        items = input_string.split(',')
        items = [item.strip() for item in items]
        return items
    
    def count_points(var,indx,mode,arr,val,n):
        if val:
            points = items_in_string(val)
            if len(points) == n:
                update_values(var,indx,mode,arr,points,i)
                messagebox.showinfo("Success", "Points entered successfully")
            else:
                messagebox.showerror("Error", "Please enter the correct number of points")
        
    update_axial_coords = tk.StringVar()
    label_axial_coords = tk.Label(stage, text="Enter the axial coordinates of the points on the mean stream surface\n (Each coordinate separated only by a single comma)and press enter:") # Label for the axial coordinates
    entry_axial_coords = tk.Entry(stage, textvariable=update_axial_coords)
    entry_axial_coords.bind("<Return>", lambda event: count_points(event,0,0,axial_coords,update_axial_coords.get(),int(update_num_points.get())))

    update_rad_coords = tk.StringVar()
    label_rad_coords = tk.Label(stage, text="Enter the radial coordinates of the points on the mean stream surface\n (Each coordinate separated only by a single comma) and press enter:") # Label for the radial coordinates
    entry_rad_coords = tk.Entry(stage, textvariable=update_rad_coords)
    entry_rad_coords.bind("<Return>", lambda event: count_points(event,0,0,rad_coords,update_rad_coords.get(),int(update_num_points.get())))

    update_meridional_vel_ratios = tk.StringVar()
    label_meridional_vel_ratios = tk.Label(stage, text="Enter the meridional velocity ratios at the points on the mean stream surface\n (Each ratio separated only by a single comma) and press enter:") # Label for the meridional velocity ratios
    entry_meridional_vel_ratios = tk.Entry(stage, textvariable=update_meridional_vel_ratios)
    entry_meridional_vel_ratios.bind("<Return>", lambda event: count_points(event,0,0,meridional_vel_ratios,update_meridional_vel_ratios.get(),int(update_num_points.get())))

    label_le_te_points = tk.Label(stage, text="Enter the leading and trailing edge points of the mean stream surface\n (Each point separated only by single comma and press enter when done):") # Label for the leading and trailing edge points
    label_le_te_points.grid(row=10, column=0, pady=5)
    le_te_points= tk.StringVar()
    entry_le_te_points = tk.Entry(stage, textvariable=le_te_points)
    entry_le_te_points.grid(row=10, column=1, pady=5)
    entry_le_te_points.bind("<Return>", lambda event: count_points(event,0,0,leading_trailing_edge_points,le_te_points.get(),4))

    bf_le= tk.StringVar()
    label_bloc_le = tk.Label(stage, text="Blockage factor at the Leading Edges of 1st blade row :") # Label for the blockage factor at the leading edges of the first blade row
    label_bloc_le.grid(row=11, column=0, pady=5)
    entry_bloc_le = tk.Entry(stage, textvariable=bf_le)
    entry_bloc_le.grid(row=11, column=1, pady=5)
    bf_le.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,fblock_le_mix,bf_le.get(),i) )

    bf_te= tk.StringVar()
    label_bloc_te = tk.Label(stage, text="Bloackage factor at the Trailing Edges of 2nd blade row:") # Label for the blockage factor at the trailing edges of the second blade row
    label_bloc_te.grid(row=12, column=0, pady=5)
    entry_bloc_te = tk.Entry(stage, textvariable=bf_te)
    entry_bloc_te.grid(row=12, column=1, pady=5)
    bf_te.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,fblock_te_mix,bf_te.get(),i) )

    update_isefficiency = tk.StringVar()
    label_isefficiency = tk.Label(stage, text="Guess of Isentropic Efficiency:") # Label for the isentropic efficiency
    label_isefficiency.grid(row=13, column=0, pady=5)
    entry_isefficiency = tk.Entry(stage, textvariable=update_isefficiency)
    entry_isefficiency.grid(row=13, column=1, pady=5)
    def validate_entries(var,indx,mode,arr,val,entry):
        if is_decimal_string(val):
            if float(val) >= 0 and float(val) <= 1:
                update_values(var,indx,mode,arr,val,i)
            else:
                messagebox.showerror("Error", "Please enter a valid number between 0 and 1")
                entry.delete(0, tk.END) # Clear the entry field
        else:
            messagebox.showerror("Error", "Please enter a valid number")
            entry.delete(0, tk.END)
    update_isefficiency.trace_add('write', lambda var,indx,mode: validate_entries(var,indx,mode,isentropic_efficiency,update_isefficiency.get(),entry_isefficiency) )

    update_dev1 = tk.StringVar()
    label_dev1 = tk.Label(stage, text="Deviation angle 1st row (in deg):") # Label for the deviation angle of the first row
    label_dev1.grid(row=14, column=0, pady=5)
    entry_dev1 = tk.Entry(stage, textvariable=update_dev1)
    entry_dev1.grid(row=14, column=1, pady=5)
    update_dev1.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,dev1,update_dev1.get(),i) )

    update_dev2 = tk.StringVar()
    label_dev2 = tk.Label(stage, text="Deviation angle 2nd row (in deg):") # Label for the deviation angle of the second row
    label_dev2.grid(row=15, column=0, pady=5)
    entry_dev2 = tk.Entry(stage, textvariable=update_dev2)
    entry_dev2.grid(row=15, column=1, pady=5)
    update_dev2.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,dev2,update_dev2.get(),i) )

    update_incid1 = tk.StringVar()
    label_incid1 = tk.Label(stage, text="Incidence angle 1st row (in deg):") # Label for the incidence angle of the first row
    label_incid1.grid(row=16, column=0, pady=5)
    entry_incid1 = tk.Entry(stage, textvariable=update_incid1)
    entry_incid1.grid(row=16, column=1, pady=5)
    update_incid1.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,incid1,update_incid1.get(),i) )

    update_incid2 = tk.StringVar()
    label_incid2 = tk.Label(stage, text="Incidence angle 2nd row (in deg):") # Label for the incidence angle of the second row
    label_incid2.grid(row=17, column=0, pady=5)
    entry_incid2 = tk.Entry(stage, textvariable=update_incid2)
    entry_incid2.grid(row=17, column=1, pady=5)
    update_incid2.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,incid2,update_incid2.get(),i) )

    textval_bt = tk.StringVar()
    label_blade_twist = tk.Label(stage, text="Blade twist option :") # Label for the blade twist angle
    label_blade_twist.grid(row=18, column=0, pady=5)
    entry_blade_twist = tk.Entry(stage, textvariable=textval_bt)
    entry_blade_twist.grid(row=18, column=1, pady=5)
    textval_bt.trace_add('write', lambda var,indx,mode: validate_entries(var,indx,mode,blade_twist,textval_bt.get(),entry_blade_twist) )

    blrot_value = tk.StringVar()
    label_blade_rotation = tk.Label(stage, text="Blade rotation option :") # Label for the blade rotation angle
    label_blade_rotation.grid(row=19, column=0, pady=5)
    entry_bldRot_yes = tk.Radiobutton(stage, text="Yes", variable=blrot_value, value="Y")
    entry_bldRot_yes.grid(row=19, column=1, pady=5)
    entry_bldRot_no = tk.Radiobutton(stage, text="No", variable=blrot_value, value="N")
    entry_bldRot_no.grid(row=20, column=1, pady=5)
    blrot_value.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,blade_rotation,blrot_value.get(),i) )
    
    update_q01_le = tk.StringVar()
    label_q01_le = tk.Label(stage, text="Q0 at LE of Row 1 (in deg):") # Label for the Q0 angle at the leading edge of the first row
    label_q01_le.grid(row=1, column=2, pady=5)
    entry_q01_le = tk.Entry(stage, textvariable=update_q01_le)
    entry_q01_le.grid(row=1, column=3, pady=5)
    update_q01_le.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,q01_le,update_q01_le.get(),i) )

    update_q01_te= tk.StringVar()
    label_q01_te = tk.Label(stage, text="Q0 at TE of Row 1 (in deg):") # Label for the Q0 angle at the trailing edge of the first row
    label_q01_te.grid(row=2, column=2, pady=5)
    entry_q01_te = tk.Entry(stage, textvariable=update_q01_te)
    entry_q01_te.grid(row=2, column=3, pady=5)
    update_q01_te.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,q01_te,update_q01_te.get(),i) )

    update_q02_le = tk.StringVar()
    label_q02_le = tk.Label(stage, text="Q0 at LE of Row 2 (in deg):") # Label for the Q0 angle at the leading edge of the second row
    label_q02_le.grid(row=3, column=2, pady=5)
    entry_q02_le = tk.Entry(stage, textvariable=update_q02_le)
    entry_q02_le.grid(row=3, column=3, pady=5)
    update_q02_le.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,q02_le,update_q02_le.get(),i) )

    update_q02_te = tk.StringVar()
    label_q02_te = tk.Label(stage, text="Q0 at TE of Row 2 (in deg):") # Label for the Q0 angle at the trailing edge of the second row
    label_q02_te.grid(row=4, column=2, pady=5)
    entry_q02_te = tk.Entry(stage, textvariable=update_q02_te)
    entry_q02_te.grid(row=4, column=3, pady=5)
    update_q02_te.trace_add('write', lambda var,indx,mode: update_values(var,indx,mode,q02_te,update_q02_te.get(),i) )

    if (turbo_typ_var.get() == "T"):
        entry_q01_le.insert(0, "92")
        entry_q01_te.insert(0, "88")
        entry_q02_le.insert(0, "88")
        entry_q02_te.insert(0, "92")
    else:
        entry_q01_le.insert(0, "88")
        entry_q01_te.insert(0, "92")
        entry_q02_le.insert(0, "92")
        entry_q02_te.insert(0, "88")

    if i<int(nstg.get()):
        stage_windowButton = tk.Button(stage, text= f"Go to Stage {i+1}", command=lambda: stage_values_mix(i))
        stage_windowButton.grid(row=15, column=2, columnspan=3, pady=20)
    else:
        bladerow_inputButton = tk.Button(stage, text="Blade Row inputs", command= blade_row_inputs)
        bladerow_inputButton.grid(row=15, column=2, columnspan=3, pady=20)

    

#Blade row inputs   
def blade_row_inputs():
    blade_row = tk.Toplevel()
    blade_row.title("Blade Row Inputs")
    blade_row.geometry("1200x768")

    canvas = tk.Canvas(blade_row)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(blade_row, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)
    frame = tk.Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')

    global blade_row_values
    global anstk
    blade_row_values = []
    anstk = []
    def update_blade_row(event):
        for i in range(2*int(nstg.get())):
            blade_row_values.append(tk.StringVar(value='N'))
        
        i=0
        j=0
        label_declare = tk.Label(frame, text="Please select the blade rows for which output is requested") # Label for the blade row inputs
        label_declare.grid(row=2, column=0, pady=5)
        
        while i<2*int(nstg.get()):
            i_now = i
            entry_rotor_row = tk.Checkbutton(frame, text=f"Rotor Row Stage {i_now+1}", variable=blade_row_values[i_now], onvalue='Y', offvalue='N')
            entry_rotor_row.grid(row=3+j, column=0, pady=5)
            entry_stator_row = tk.Checkbutton(frame, text=f"Stator Row Stage {i_now+1}", variable=blade_row_values[i_now+1], onvalue='Y', offvalue='N')
            entry_stator_row.grid(row=3+j, column=1, pady=5)
            j+=1
            i+=2


    global request_input
    request_input= tk.StringVar()
    label_request_input = tk.Label(frame, text="Is output requsted for all blade rows?") # Label for the blade row inputs
    label_request_input.grid(row=0, column=0, pady=5)
    entry_input_yes = tk.Radiobutton(frame, text="Yes", variable=request_input, value="Y")
    entry_input_yes.grid(row=0, column=1, pady=5)
    entry_input_no = tk.Radiobutton(frame, text="No", variable=request_input, value="N")
    entry_input_no.grid(row=1, column=1, pady=5)
    entry_input_no.bind("<Button-1>", update_blade_row) # Bind the function to the No option to show the blade row inputs
    
    
    for i in range(2*int(nstg.get())):
        anstk.append(tk.StringVar(value='Y'))
    
    def create_empty_string_matrix(n):
        matrix = [[tk.StringVar() for _ in range(3)] for _ in range(n)]
        return matrix

    global max_thickness_stator 
    max_thickness_stator = create_empty_string_matrix(int(nstg.get()))
    global max_thickness_rotor 
    max_thickness_rotor   = create_empty_string_matrix(int(nstg.get()))
    global thickness_loc_stator 
    thickness_loc_stator= create_empty_string_matrix(int(nstg.get()))
    global thickness_loc_rotor
    thickness_loc_rotor = create_empty_string_matrix(int(nstg.get()))

    def update_blade_thickness(i,j):
        label_max_thickness_rotor = tk.Label(frame, text=f"Maximum thickness of rotor blade row {j+1} (in m):") # Label for the maximum thickness of the stator blade row
        entry1_rotor= tk.Entry(frame, textvariable=max_thickness_rotor[j][0])
        entry2_rotor= tk.Entry(frame, textvariable=max_thickness_rotor[j][1])
        entry3_rotor= tk.Entry(frame, textvariable=max_thickness_rotor[j][2])
        label_thickness_loc_rotor = tk.Label(frame, text=f"Max thickness location of rotor blade row {j+1} (in m):") # Label for the thickness location of the stator blade row
        entry4_rotor= tk.Entry(frame, textvariable=thickness_loc_rotor[j][0])
        entry5_rotor= tk.Entry(frame, textvariable=thickness_loc_rotor[j][1])
        entry6_rotor= tk.Entry(frame, textvariable=thickness_loc_rotor[j][2])
        label_max_thickness_stator = tk.Label(frame, text=f"Maximum thickness of stator blade row {j+1} (in m):")
        entry1_stator= tk.Entry(frame, textvariable=max_thickness_stator[j][0])
        entry2_stator= tk.Entry(frame, textvariable=max_thickness_stator[j][1])
        entry3_stator= tk.Entry(frame, textvariable=max_thickness_stator[j][2])
        label_thickness_loc_stator = tk.Label(frame, text=f"Max thickness location of stator blade row {j+1} (in m):")
        entry4_stator= tk.Entry(frame, textvariable=thickness_loc_stator[j][0])
        entry5_stator= tk.Entry(frame, textvariable=thickness_loc_stator[j][1])
        entry6_stator= tk.Entry(frame, textvariable=thickness_loc_stator[j][2])


        if anstk[i].get() == 'N' and i%2 == 0:
            label_max_thickness_rotor.grid(row=3+2*int(nstg.get())+i, column=0, pady=5)
            entry1_rotor.grid(row=3+2*int(nstg.get())+i, column=1, pady=5)
            entry2_rotor.grid(row=3+2*int(nstg.get())+i, column=2, pady=5)
            entry3_rotor.grid(row=3+2*int(nstg.get())+i, column=3, pady=5)
            label_thickness_loc_rotor.grid(row=4+2*int(nstg.get())+i, column=0, pady=5)
            entry4_rotor.grid(row=4+2*int(nstg.get())+i, column=1, pady=5)
            entry5_rotor.grid(row=4+2*int(nstg.get())+i, column=2, pady=5)
            entry6_rotor.grid(row=4+2*int(nstg.get())+i, column=3, pady=5)
        elif anstk[i].get() == 'N' and i%2 != 0:
            label_max_thickness_stator.grid(row=4+2*int(nstg.get())+i, column=0, pady=5)
            entry1_stator.grid(row=4+2*int(nstg.get())+i, column=1, pady=5)
            entry2_stator.grid(row=4+2*int(nstg.get())+i, column=2, pady=5)
            entry3_stator.grid(row=4+2*int(nstg.get())+i, column=3, pady=5)
            label_thickness_loc_stator.grid(row=5+2*int(nstg.get())+i, column=0, pady=5)
            entry4_stator.grid(row=5+2*int(nstg.get())+i, column=1, pady=5)
            entry5_stator.grid(row=5+2*int(nstg.get())+i, column=2, pady=5)
            entry6_stator.grid(row=5+2*int(nstg.get())+i, column=3, pady=5)
        elif anstk[i].get() == 'Y' and i%2 == 0:
            label_max_thickness_rotor.grid_forget()
            entry1_rotor.grid_forget()
            entry2_rotor.grid_forget()
            entry3_rotor.grid_forget()
            label_thickness_loc_rotor.grid_forget()
            entry4_rotor.grid_forget()
            entry5_rotor.grid_forget()
            entry6_rotor.grid_forget()
        elif anstk[i].get() == 'Y' and i%2 != 0:
            label_max_thickness_stator.grid_forget()
            entry1_stator.grid_forget()
            entry2_stator.grid_forget()
            entry3_stator.grid_forget()
            label_thickness_loc_stator.grid_forget()
            entry4_stator.grid_forget()
            entry5_stator.grid_forget()
            entry6_stator.grid_forget()
        else:
            return
        
    i=0
    j=0

    while i<2*int(nstg.get()):
        i_now = i
        entry_anstk_rotor = tk.Checkbutton(frame, text=f"Use same blade sections as previous for rotor {j+1}", variable=anstk[i_now], onvalue='Y', offvalue='N', command= lambda i=i_now,j=j: update_blade_thickness(i,j))
        entry_anstk_rotor.grid(row=3+int(nstg.get())+j, column=0, pady=5)
        i+=1
        i_now = i
        entry_anstk_stator = tk.Checkbutton(frame, text=f"Use same blade sections as previous for stator {j+1}", variable=anstk[i_now], onvalue='Y', offvalue='N', command= lambda i=i_now,j=j: update_blade_thickness(i,j))
        entry_anstk_stator.grid(row=3+int(nstg.get())+j, column=1, pady=5)
        j+=1
        i+=1
    
    
    create_in_fileButton = tk.Button(frame, text="Create meangen.in file", command=create_in_file) 
    create_in_fileButton.grid(row=5+4*int(nstg.get()), column=2, columnspan=3, pady=20)

    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    blade_row.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
    
   
    

        
    

    

    

    
    

# Function to show or hide additional fields based on the FLO_TYP selection
def update_flo_typ():
    flo_typ = flo_typ_var.get()
    def update_windowButton(*args):
        if flo_typ == "AXI":
            stage_windowButton = tk.Button(root, text=" Specify Stage 1", command= lambda: stage_values_axi(0))
            stage_windowButton.grid(row=12, column=4, columnspan=3, pady=20)
        elif flo_typ == "MIX":
            stage_windowButton = tk.Button(root, text=" Specify Stage 1", command= lambda: stage_values_mix(0))
            stage_windowButton.grid(row=12, column=4, columnspan=3, pady=20)
        else:
            return
    nstg.trace_add('write', update_windowButton)
    return




# Function to create the .in file with user inputs
def create_in_file():
    turbo_typ = turbo_typ_var.get()
    flo_typ = flo_typ_var.get()
    rgas = entry_rgas.get()
    gamma = entry_gamma.get()
    poin = entry_poin.get()
    toin = entry_toin.get()
    num_stages = entry_num_stages.get()
    base_radius = entry_designPoint_choice.get()[0]
    rotation_speed = entry_rotation_speed.get()
    flowin = entry_flowin.get()



    file= open("meangen.in","w")
    if not turbo_typ:
        messagebox.showerror("Error", "Please select whether the turbomachinery is a compressor or a turbine")
        return
    else:   
        file.write(f"{turbo_typ:1s}{' '*(25-1)} TURBO_TYP,\"C\" FOR A COMPRESSOR,\"T\" FOR A TURBINE\n")

    if not flo_typ:
        messagebox.showerror("Error", "Please select whether the machine is axial or mixed flow")
        return
    else:
        file.write(f"{flo_typ:3s}{' '*(25-3)} FLO_TYP FOR AXIAL OR MIXED FLOW MACHINE \n")

    if not rgas or not is_decimal_string(rgas):
        rgas = "287.5"
    if not gamma or not is_decimal_string(gamma):
        gamma = "1.4"
    file.write(f"{float(rgas):10.3f}{float(gamma):10.3f}{' '*(25-20)} GAS PROPERTOES, RGAS, GAMMA \n")
    if not all([poin, toin]):
        messagebox.showerror("Error", "POIN and TOIN are required")
        return
    elif not is_decimal_string(poin) or not is_decimal_string(toin):
        messagebox.showerror("Error", "POIN and TOIN should be numbers")
        return
    else:
        file.write(f" {float(poin):10.3f}{float(toin):10.3f}{' '*(25-20)} POIN,  TOIN \n")

    if not num_stages:
        messagebox.showerror("Error", "Number of stages is required")
        return
    elif not is_decimal_string(num_stages):
        messagebox.showerror("Error", "Number of stages should be a number")
        return
    else:
        file.write(f"{int(num_stages):5d}{' '*(25-5)} NUMBER OF STAGES IN THE MACHINE \n")

    if not base_radius:
        messagebox.showerror("Error", "Design radius choice is required")
        return
    elif base_radius not in ["H", "M", "T"]:
        messagebox.showerror("Error", "Design radius choice should be Hub, Mid or Tip")
        return
    else:
        file.write(f"{base_radius:1s}{' '*(25-1)} CHOICE OF DESIGN POINT RADIUS, HUB, MID or TIP\n")

    if not rotation_speed:
        messagebox.showerror("Error", "Rotation speed is required")
        return
    elif not is_decimal_string(rotation_speed):
        messagebox.showerror("Error", "Rotation speed should be a number")
        return
    elif int(rotation_speed)<=0:
        messagebox.showerror("Error", "Rotation speed should be positive number")
        return
    else:
        file.write(f"{float(rotation_speed):12.3f}{' '*(25-12)} ROTATION SPEED, RPM \n")

    if not flowin:
        messagebox.showerror("Error", "Mass flow rate for inlet is required")
        return
    elif not is_decimal_string(flowin):
        messagebox.showerror("Error", "Mass flow rate for inlet should be a number")
        return
    else:
        file.write(f"{float(flowin):12.3f}{' '*(25-12)} MASS FLOW RATE, FLOWIN. \n")

    def is_decimal_array(arr):
        return all([is_decimal_string(val) for val in arr])

    if flo_typ == "AXI":
        for i in range(int(num_stages)):
            if i!=0:
                file.write(f"{copy_stage[i]:1s}{' '*(25-1)} IFSAME_ALL, SET = \"Y\" TO REPEAT THE LAST STAGE INPUT TYPE AND VELOCITY TRIANGLES, SET = \"C\" TO CHANGE INPUT TYPE.\n")
                if copy_stage[i] == "Y":
                    if not all ([fblock_le[i],fblock_te[i]]):
                        messagebox.showerror("Error", "Please enter all the values for blockage factors for stage : "+str(i+1))
                        return
                    elif not all([is_decimal_string(fblock_le[i]), is_decimal_string(fblock_te[i])]):
                        messagebox.showerror("Error", "Please enter valid numbers for blockage factors for stage : "+str(i+1))
                        return
                    else:
                        file.write(f"{float(fblock_le[i]):10.5f}{fblock_te[i]:10.5f}{' '*(25-20)} BLOCKAGE FACTORS, FBLOCK_LE,  FBLOCK_TE \n")
                    file.write("N  DO YOU WANT TO CHANGE THE ANGLES FOR THIS STAGE ? \"Y\" or \"N\"\n")
                    continue       
            if intype_axi[i] == "A. Reaction, flow coefficient and stage loading coefficient":
                file.write(f"{intype_axi[i][0]:1s}{' '*(25-1)} INTYPE, TO CHOOSE THE METHOD OF DEFINING THE VELOCITY TRIANGLES\n")
                if not all([stage_reaction[i], flow_coeff[i], stage_loading_coeff[i]]):
                    messagebox.showerror("Error", "Please enter all the values for stage : "+str(i+1))
                    return
                elif not all([is_decimal_string(stage_reaction[i]), is_decimal_string(flow_coeff[i]), is_decimal_string(stage_loading_coeff[i])]):
                    messagebox.showerror("Error", "Please enter valid numbers for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{float(stage_reaction[i]):7.3f}{float(flow_coeff[i]):7.3f}{float(stage_loading_coeff[i]):7.3f}{' '*(25-21)}  REACTION, FLOW COEFF., LOADING COEFF.\n") #INTYPE A
            elif intype_axi[i] == "B. Flow coefficient, stator and rotor exit angles":
                file.write(f"{intype_axi[i][0]:1s}{' '*(25-1)} INTYPE, TO CHOOSE THE METHOD OF DEFINING THE VELOCITY TRIANGLES\n")
                if not all([flow_coeff[i], statorex_angle[i], rotorex_angle[i]]):
                    messagebox.showerror("Error", "Please enter all the values for stage : "+str(i+1))
                    return
                elif not all([is_decimal_string(flow_coeff[i]), is_decimal_string(statorex_angle[i]), is_decimal_string(rotorex_angle[i])]):
                    messagebox.showerror("Error", "Please enter valid numbers for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{float(flow_coeff[i]):12.3f}{float(statorex_angle[i]):12.3f}{float(rotorex_angle[i]):12.3f}  FLOW COEFF, STATOR ANGLES \n") #INTYPE B
            elif intype_axi[i] == "C. flow coefficient, rotor inlet and exit angles":
                file.write(f"{intype_axi[i][0]:1s}{' '*(25-1)} INTYPE, TO CHOOSE THE METHOD OF DEFINING THE VELOCITY TRIANGLES\n")
                if not all([flow_coeff[i], rotorin_angle[i], rotorex_angle[i]]):
                    messagebox.showerror("Error", "Please enter all the values for stage : "+str(i+1))
                    return
                elif not all([is_decimal_string(flow_coeff[i]), is_decimal_string(rotorin_angle[i]), is_decimal_string(rotorex_angle[i])]):
                    messagebox.showerror("Error", "Please enter valid numbers for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{float(rotorin_angle[i]):12.3f}{float(rotorex_angle[i]):12.3f}{float(flow_coeff[i]):12.3f} ROTOR ANGLES, FLOW COEFF.\n") #INTYPE C
            elif intype_axi[i] == "D. Stage reaction, first blade row inlet and exit angles":
                file.write(f"{intype_axi[i][0]:1s}{' '*(25-1)} INTYPE, TO CHOOSE THE METHOD OF DEFINING THE VELOCITY TRIANGLES\n")
                if not all([stage_reaction[i], rotorin_angle[i], rotorex_angle[i]]):
                    messagebox.showerror("Error", "Please enter all the values for stage : "+str(i+1))
                    return
                elif not all([is_decimal_string(stage_reaction[i]), is_decimal_string(rotorin_angle[i]), is_decimal_string(rotorex_angle[i])]):
                    messagebox.showerror("Error", "Please enter valid numbers for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{float(rotorin_angle[i]):12.3f} {float(rotorex_angle[i]):12.3f} {float(stage_reaction[i]):12.3f}  FIRST ROW ANGLES, REACTION\n")
            else:
                messagebox.showerror("Error", "Please select an input type for stage : "+str(i+1))
                return
            
            if rad_typ[i] == "A. Input design radius directly":
                file.write(f"{rad_typ[i][0]:1s}{' '*(25-1)}  RADTYPE, TO CHOOSE THE DESIGN POINT RADIUS\n")
                if not dirInput_designRadius[i]:
                    messagebox.showerror("Error", "Please enter radius of stage : "+str(i+1))
                    return
                elif not is_decimal_string(dirInput_designRadius[i]):
                    messagebox.showerror("Error", "Please enter a valid number for radius of stage : "+str(i+1))
                    return
                else:
                    file.write(f"{float(dirInput_designRadius[i]):12.3f}{' '*(25-12)} THE DESIGN POINT RADIUS \n")
            elif rad_typ[i] == "B. Input stage enthalpy change":
                file.write(f"{rad_typ[i][0]:1s}{' '*(25-1)}  RADTYPE, TO CHOOSE THE DESIGN POINT RADIUS\n")
                if not stage_enthalpy_change[i]:
                    messagebox.showerror("Error", "Please enter enthalpy change for stage : "+str(i+1))
                    return
                elif not is_decimal_string(stage_enthalpy_change[i]):
                    messagebox.showerror("Error", "Please enter a valid number for enthalpy change of stage : "+str(i+1))
                    return
                else:
                    file.write(f"{float(stage_enthalpy_change[i]):12.3f}{' '*(25-12)}STAGE ENTHALPY CHANGE, KJ/Kg\n")
            else:
                messagebox.showerror("Error", "Please select method to input radius of stage : "+str(i+1))
                return
            
            if not all([blade_axialChord1[i],blade_axialChord2[i]]):
                messagebox.showerror("Error", "Please enter all the values for blade axial chords for stage : "+str(i+1))
                return
            elif not all([is_decimal_string(blade_axialChord1[i]), is_decimal_string(blade_axialChord2[i])]):
                messagebox.showerror("Error", "Please enter valid numbers blade axia chords for stage : "+str(i+1))
                return
            else:
                file.write(f"{blade_axialChord1[i]}, {blade_axialChord2[i]} BLADE AXIAL CHORDS IN METRES\n")
            
            if not all([rowGap[i],stageGap[i]]):
                messagebox.showerror("Error", "Please enter all the values for row and stage gaps for stage : "+str(i+1))
                return
            elif not all([is_decimal_string(rowGap[i]), is_decimal_string(stageGap[i])]):
                messagebox.showerror("Error", "Please enter valid numbers for row and stage gaps for stage : "+str(i+1))
                return
            else:
                file.write(f"{rowGap[i]}, {stageGap[i]} ROW GAP  AND STAGE GAP \n")
            
            if not all ([fblock_le[i],fblock_te[i]]):
                messagebox.showerror("Error", "Please enter all the values for blockage factors for stage : "+str(i+1))
                return
            elif not all([is_decimal_string(fblock_le[i]), is_decimal_string(fblock_te[i])]):
                messagebox.showerror("Error", "Please enter valid numbers for blockage factors for stage : "+str(i+1))
                return
            else:
                file.write(f"{fblock_le[i]}, {fblock_te[i]} BLOCKAGE FACTORS, FBLOCK_LE,  FBLOCK_TE \n")
            
            if not isentropic_efficiency[i]:
                messagebox.showerror("Error", "Please enter isentropic efficiency for stage : "+str(i+1))
                return
            elif not is_decimal_string(isentropic_efficiency[i]):
                messagebox.showerror("Error", "Please enter a valid number for isentropic efficiency for stage : "+str(i+1))
                return
            else:
                file.write(f"{isentropic_efficiency[i]} GUESS OF THE STAGE ISENTROPIC EFFICIENCY \n")
            
            if not all([dev1[i], dev2[i]]):
                messagebox.showerror("Error", "Please enter all the values for row deviation angles for stage : "+str(i+1))
                return  
            elif not all([is_decimal_string(dev1[i]), is_decimal_string(dev2[i])]):
                messagebox.showerror("Error", "Please enter valid numbers for row deviation angles for stage : "+str(i+1))
                return
            else:
                file.write(f"{dev1[i]}, {dev2[i]} ESTIMATE OF THE FIRST AND SECOND ROW DEVIATION ANGLES \n")
            
            if not all([incid1[i], incid2[i]]):
                messagebox.showerror("Error", "Please enter all the values for row incidence angles for stage : "+str(i+1))
                return
            elif not all([is_decimal_string(incid1[i]), is_decimal_string(incid2[i])]):
                messagebox.showerror("Error", "Please enter valid numbers for row incidence angles for stage : "+str(i+1))
                return
            else:
                file.write(f"{incid1[i]}, {incid2[i]} FIRST AND SECOND ROW INCIDENCE ANGLES \n")
            
            if not blade_twist[i]:
                messagebox.showerror("Error", "Please enter blade twist option for stage : "+str(i+1))
                return
            elif not is_decimal_string(blade_twist[i]):
                messagebox.showerror("Error", "Please enter a valid number for blade twist option for stage : "+str(i+1))
                return
            else:
                file.write(f"{blade_twist[i]} BLADE TWIST OPTION, FRAC_TWIST \n")
            
            if not blade_rotation[i]:
                messagebox.showerror("Error", "Please enter blade rotation option for stage : "+str(i+1))
                return
            elif not blade_rotation[i] in ["Y", "N"]:
                messagebox.showerror("Error", "Please enter a valid option for blade rotation for stage : "+str(i+1))
                return
            else:
                file.write(f"{blade_rotation[i]} BLADE ROTATION OPTION , Y or N \n")
            
            if not all([q01_le[i], q01_te[i]]):
                messagebox.showerror("Error", "Please enter all the values for Q0 angles for row 1 of stage : "+str(i+1))
                return
            elif not all([is_decimal_string(q01_le[i]), is_decimal_string(q01_te[i])]):
                messagebox.showerror("Error", "Please enter valid numbers for Q0 angles for row 1 of stage : "+str(i+1))
                return
            else:
                file.write(f"{q01_le[i]}, {q01_te[i]} Q0 ANGLES AT LE AND TE OF ROW 1 \n")
            
            if not all([q02_le[i], q02_te[i]]):
                messagebox.showerror("Error", "Please enter all the values for Q0 angles for row 2 of stage : "+str(i+1))
                return
            elif not all([is_decimal_string(q02_le[i]), is_decimal_string(q02_te[i])]):
                messagebox.showerror("Error", "Please enter valid numbers for Q0 angles for row 2 of stage : "+str(i+1))
                return
            else:
                file.write(f"{q02_le[i]}, {q02_te[i]} Q0 ANGLES AT LE AND TE OF ROW 2 \n")
            
            file.write("N  DO YOU WANT TO CHANGE THE ANGLES FOR THIS STAGE ? \"Y\" or \"N\"\n")
    elif flo_typ == "MIX":
        for i in range(int(num_stages)):
            if i!=0:
                file.write(f"{copy_stage[i]} IFSAME_ALL, SET = \"Y\" TO REPEAT THE LAST STAGE INPUT TYPE AND VELOCITY TRIANGLES, SET = \"C\" TO CHANGE INPUT TYPE.\n")
                if copy_stage[i] == "Y":
                    if not all ([fblock_le_mix[i],fblock_te_mix[i]]):
                        messagebox.showerror("Error", "Please enter all the values for blockage factors for stage : "+str(i+1))
                        return
                    elif not all([is_decimal_string(fblock_le_mix[i]), is_decimal_string(fblock_te_mix[i])]):
                        messagebox.showerror("Error", "Please enter valid numbers for blockage factors for stage : "+str(i+1))
                        return
                    else:
                        file.write(f"{fblock_le_mix[i]}, {fblock_te_mix[i]} BLOCKAGE FACTORS, FBLOCK_LE,  FBLOCK_TE \n")
                    file.write("N  DO YOU WANT TO CHANGE THE ANGLES FOR THIS STAGE ? \"Y\" or \"N\"\n")
                    continue       
            
            if not intype_mix[i]:
                messagebox.showerror("Error", "Please select an input type for stage : "+str(i+1))
                return
            elif not intype_mix[i][0] in ["A. All four blade angles" ,"B. Absolute flow angles at stage inlet and outlet, and stage loading and flow coefficients"]:
                messagebox.showerror("Error", "Please select a valid input type for stage : "+str(i+1))
                return
            else:
                file.write(f"{intype_mix[i][0]} MIXTYP = INPUT TYPE FOR FLO_TYP = \"MIX\" .\n")
                if intype_mix[i] == "A. All four blade angles":
                    if not all([statorex_angle[i],statorin_angle[i],rotorex_angle[i],rotorin_angle[i]]):
                        messagebox.showerror("Error", "Please enter all the values for blade angles for stage : "+str(i+1))
                        return
                    elif not all([is_decimal_string(statorex_angle[i]), is_decimal_string(statorin_angle[i]), is_decimal_string(rotorex_angle[i]), is_decimal_string(rotorin_angle[i])]):
                        messagebox.showerror("Error", "Please enter valid numbers for blade angles for stage : "+str(i+1))
                        return
                    else:
                        file.write(f"{statorex_angle[i]} {statorin_angle[i]} ANGLES, STATOR_IN, STATOR_OUT\n")
                        file.write(f"{rotorex_angle[i]} {rotorin_angle[i]} ANGLES, ROTOR_IN, ROTOR_OUT\n")
                elif intype_mix[i] == "B. Absolute flow angles at stage inlet and outlet, and stage loading and flow coefficients":
                    if not all([flow_coeff[i], stageex_angle_mix[i], stagein_angle_mix[i], stage_loading_coeff[i]]):
                        messagebox.showerror("Error", "Please enter all the values for blade angles for stage : "+str(i+1))
                        return
                    elif not all([is_decimal_string(flow_coeff[i]), is_decimal_string(stageex_angle[i]), is_decimal_string(stagein_angle[i]), is_decimal_string(stage_loading_coeff[i])]):
                        messagebox.showerror("Error", "Please enter valid numbers for blade angles for stage : "+str(i+1))
                        return
                    else:
                        file.write(f"{flow_coeff[i]}  FLOW COEFFICIENT AT THE FIRST ROTOR LEADING EDGE.\n")
                        file.write(f"{stagein_angle_mix[i]} {stageex_angle_mix[i]} STAGE INLET AND OUTLET ABSOLUTE FLOW ANGLES.\n")
                        file.write(f"{stage_loading_coeff[i]} STAGE LOADING COEFFICIENT AT ROTOR LEADING EDGE\n")
                else:
                    messagebox.showerror("Error", "Please select an input type for stage : "+str(i+1))
                    return

                if not num_points[i]:
                    messagebox.showerror("Error", "Please enter number of points on stream surface for stage : "+str(i+1))
                    return
                elif not is_decimal_string(num_points[i]):
                    messagebox.showerror("Error", "Please enter a valid number for number of points on stream surface for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{num_points[i]} NUMBER OF POINTS ON THE STREAM SURFACE\n")
                
                
                if not all(axial_coords[i]):
                    messagebox.showerror("Error", "Please enter all the values for the stream surface axial coordinates for stage : "+str(i+1))
                    return
                elif not is_decimal_array(axial_coords[i]):
                    messagebox.showerror("Error", "Please enter valid numbers for the stream surface axial coordinates for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{' '.join(axial_coords[i])}\n")

                if not all(rad_coords[i]):
                    messagebox.showerror("Error", "Please enter all the values for the stream surface radial coordinates for stage : "+str(i+1))
                    return
                elif not is_decimal_array(rad_coords[i]):
                    messagebox.showerror("Error", "Please enter valid numbers for the stream surface radial coordinates for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{' '.join(rad_coords[i])}\n")
                
                if not all(meridional_vel_ratios[i]):
                    messagebox.showerror("Error", "Please enter all the values for the meridional velocity ratios for stage : "+str(i+1))
                    return
                elif not is_decimal_array(meridional_vel_ratios[i]):
                    messagebox.showerror("Error", "Please enter valid numbers for the meridional velocity ratios for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{' '.join(meridional_vel_ratios[i])}\n")
                
                if not all(leading_trailing_edge_points[i]):
                    messagebox.showerror("Error", "Please enter all the values for the leading and trailing edge points for stage : "+str(i+1))
                    return
                elif not is_decimal_array(leading_trailing_edge_points[i]):
                    messagebox.showerror("Error", "Please enter valid numbers for the leading and trailing edge points for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{' '.join(leading_trailing_edge_points[i])} LEADING AND TRAILING EDGE POINTS ON THE MEAN STREAM SURFACE.\n")

                if not all(fblock_le_mix[i],fblock_te_mix[i]):
                    messagebox.showerror("Error", "Please enter all the values for blockage factors for stage : "+str(i+1))
                    return
                elif not all([is_decimal_string(fblock_le_mix[i]), is_decimal_string(fblock_te_mix[i])]):
                    messagebox.showerror("Error", "Please enter valid numbers for blockage factors for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{fblock_le_mix[i]}, {fblock_te_mix[i]} BLOCKAGE FACTORS, FBLOCK_LE,  FBLOCK_TE \n")
                
                if not isentropic_efficiency[i]:
                    messagebox.showerror("Error", "Please enter isentropic efficiency for stage : "+str(i+1))
                    return
                elif not is_decimal_string(isentropic_efficiency[i]):
                    messagebox.showerror("Error", "Please enter a valid number for isentropic efficiency for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{isentropic_efficiency[i]} GUESS OF THE STAGE ISENTROPIC EFFICIENCY \n")
                
                if not all([dev1[i], dev2[i]]):
                    messagebox.showerror("Error", "Please enter all the values for row deviation angles for stage : "+str(i+1))
                    return
                elif not all([is_decimal_string(dev1[i]), is_decimal_string(dev2[i])]):
                    messagebox.showerror("Error", "Please enter valid numbers for row deviation angles for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{dev1[i]}, {dev2[i]} ESTIMATE OF THE FIRST AND SECOND ROW DEVIATION ANGLES \n")
                
                if not all([incid1[i], incid2[i]]):
                    messagebox.showerror("Error", "Please enter all the values for row incidence angles for stage : "+str(i+1))
                    return
                elif not all([is_decimal_string(incid1[i]), is_decimal_string(incid2[i])]):
                    messagebox.showerror("Error", "Please enter valid numbers for row incidence angles for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{incid1[i]}, {incid2[i]} FIRST AND SECOND ROW INCIDENCE ANGLES \n")
                
                if not blade_twist[i]:
                    messagebox.showerror("Error", "Please enter blade twist option for stage : "+str(i+1))
                    return
                elif not is_decimal_string(blade_twist[i]):
                    messagebox.showerror("Error", "Please enter a valid number for blade twist option for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{blade_twist[i]} BLADE TWIST OPTION, FRAC_TWIST \n")
                
                if not blade_rotation[i]:
                    messagebox.showerror("Error", "Please enter blade rotation option for stage : "+str(i+1))
                    return
                elif not blade_rotation[i] in ["Y", "N"]:
                    messagebox.showerror("Error", "Please enter a valid option for blade rotation for stage : "+str(i+1))
                    return
                else:
                    file.write(f"{blade_rotation[i]} BLADE ROTATION OPTION , Y or N \n")
                
                if not all([q01_le[i], q01_te[i]]):
                    messagebox.showerror("Error", "Please enter all the values for Q0 angles for row 1 of stage : "+str(i+1))
                    return
                elif not all([is_decimal_string(q01_le[i]), is_decimal_string(q01_te[i])]):
                    messagebox.showerror("Error", "Please enter valid numbers for Q0 angles for row 1 of stage : "+str(i+1))
                    return
                else:
                    file.write(f"{q01_le[i]}, {q01_te[i]} Q0 ANGLES AT LE AND TE OF ROW 1 \n")
                
                if not all([q02_le[i], q02_te[i]]):
                    messagebox.showerror("Error", "Please enter all the values for Q0 angles for row 2 of stage : "+str(i+1))
                    return
                elif not all([is_decimal_string(q02_le[i]), is_decimal_string(q02_te[i])]):
                    messagebox.showerror("Error", "Please enter valid numbers for Q0 angles for row 2 of stage : "+str(i+1))
                    return
                else:
                    file.write(f"{q02_le[i]}, {q02_te[i]} Q0 ANGLES AT LE AND TE OF ROW 2 \n")
                
                file.write("n DO YOU WANT TO CHANGE THE ANGLES FOR THIS STAGE ? \"Y\" or \"N\"\n")

    # blade row specifications
    
    if turbo_typ == "C":
        output_check=""
        if not request_input.get():
            messagebox.showerror("Error", "Please select whether all blade rows must be output or not")
            return
        elif request_input.get() == "Y":
            output_check = "Y"
        elif request_input.get() == "N":
            output_check = "N"
        else:
            messagebox.showerror("Error", "Please select a valid option for output")
            return
        file.write(f"{output_check} IS OUTPUT REQUESTED FOR ALL BLADE ROWS?\n")
        if output_check == "N":
            for i in range(2*int(num_stages)):
                file.write(f"{blade_row_values[i].get()} IS OUTPUT REQUESTED FOR THIS BLADE ROW ?\n") # for which blade rows(rotor/stator) output is requested
        j=0
        for i in range(2*int(num_stages)):
            if i%2 ==0:
                file.write(f"{anstk[i].get()} ROTOR No.   1 SET ANSTK = \"Y\" TO USE THE SAME  BLADE SECTIONS AS THE LAST STAGE\n")
                if anstk[i].get() == "N":
                    file.write(f"{max_thickness_rotor[j][0].get()} {thickness_loc_rotor[j][0].get()} MAX THICKNESS AND ITS LOCATION FOR ROTOR  1 SECTION No.  1\n")
                    file.write(f"{max_thickness_rotor[j][1].get()} {thickness_loc_rotor[j][1].get()} MAX THICKNESS AND ITS LOCATION FOR ROTOR  1 SECTION No.  2\n")
                    file.write(f"{max_thickness_rotor[j][2].get()} {thickness_loc_rotor[j][2].get()} MAX THICKNESS AND ITS LOCATION FOR ROTOR  1 SECTION No.  3\n")
            elif i%2!=0:
                file.write(f"{anstk[i].get()} STATOR No.   1 SET ANSTK = \"Y\" TO USE THE SAME  BLADE SECTIONS AS THE LAST STAGE\n")
                if anstk[i].get() == "N":
                    file.write(f"{max_thickness_stator[j][0].get()} {thickness_loc_stator[j][0].get()} MAX THICKNESS AND ITS LOCATION FOR STATOR  1 SECTION No.  1\n")
                    file.write(f"{max_thickness_stator[j][1].get()} {thickness_loc_stator[j][1].get()} MAX THICKNESS AND ITS LOCATION FOR STATOR  1 SECTION No.  2\n")
                    file.write(f"{max_thickness_stator[j][2].get()} {thickness_loc_stator[j][2].get()} MAX THICKNESS AND ITS LOCATION FOR STATOR  1 SECTION No.  3\n")
                j+=1
    elif turbo_typ == "T":
        output_check=""
        if not request_input.get():
            messagebox.showerror("Error", "Please select whether all blade rows must be output or not")
            return
        elif request_input.get() == "Y":
            output_check = "Y"
        elif request_input.get() == "N":
            output_check = "N"
        else:
            messagebox.showerror("Error", "Please select a valid option for output")
            return
        file.write(f"{output_check} IS OUTPUT REQUESTED FOR ALL BLADE ROWS?\n")
        if output_check == "N":
            for i in range(0,2*int(num_stages),2):
                file.write(f"{blade_row_values[i+1].get()} IS OUTPUT REQUESTED FOR THIS BLADE ROW ?\n") # for which blade rows(stator) output is requested
                file.write(f"{blade_row_values[i].get()} IS OUTPUT REQUESTED FOR THIS BLADE ROW ?\n") # for which blade rows(stator) output is requested
        j=0
        for i in range(1,2*int(num_stages),2):
            file.write(f"{anstk[i].get()} STATOR No.   1 SET ANSTK = \"Y\" TO USE THE SAME  BLADE SECTIONS AS THE LAST STAGE\n")
            if anstk[i].get() == "N":
                file.write(f"{max_thickness_stator[j][0].get()} {thickness_loc_stator[j][0].get()} MAX THICKNESS AND ITS LOCATION FOR STATOR  1 SECTION No.  1\n")
                file.write(f"{max_thickness_stator[j][1].get()} {thickness_loc_stator[j][1].get()} MAX THICKNESS AND ITS LOCATION FOR STATOR  1 SECTION No.  2\n")
                file.write(f"{max_thickness_stator[j][2].get()} {thickness_loc_stator[j][2].get()} MAX THICKNESS AND ITS LOCATION FOR STATOR  1 SECTION No.  3\n")
            file.write(f"{anstk[i-1].get()} ROTOR No.   1 SET ANSTK = \"Y\" TO USE THE SAME  BLADE SECTIONS AS THE LAST STAGE\n")
            if anstk[i-1].get() == "N":
                file.write(f"{max_thickness_rotor[j][0].get()} {thickness_loc_rotor[j][0].get()} MAX THICKNESS AND ITS LOCATION FOR ROTOR  1 SECTION No.  1\n")
                file.write(f"{max_thickness_rotor[j][1].get()} {thickness_loc_rotor[j][1].get()} MAX THICKNESS AND ITS LOCATION FOR ROTOR  1 SECTION No.  2\n")
                file.write(f"{max_thickness_rotor[j][2].get()} {thickness_loc_rotor[j][2].get()} MAX THICKNESS AND ITS LOCATION FOR ROTOR  1 SECTION No.  3\n")
            j+=1
                    
    messagebox.showinfo("Success", "The .in file has been created successfully")
    file.close()
    run = messagebox.askyesno("Run", "Do you want to run the code?")
    
    if run:
        run_program()
    # Validate inputs

# Create the main window
root = tk.Tk()
root.title("Input for .in File")
root.geometry("1366x768") # Set the window size, here it is set to my screen resolution
# Create widgets

turbo_typ_var = tk.StringVar(value="")
label_turbo_typ = tk.Label(root, text="Type of Turbomachinery:") # Label for the TURBO_TYP
label_turbo_typ.grid(row=0, column=0)

radio_compressor = tk.Radiobutton(root, text="Compressor", variable=turbo_typ_var, value='C', command=update_turbo_typ) 
radio_compressor.grid(row=1, column=0, pady=5, sticky="w")
radio_turbine = tk.Radiobutton(root, text="Turbine", variable=turbo_typ_var, value='T', command=update_turbo_typ)
radio_turbine.grid(row=1, column=1, pady=5, sticky="w")

flo_typ_var= tk.StringVar(value="") 
label_flo_typ = tk.Label(root, text="Axial flow Machine or Mixed flow machine:") # Label for the FLO_TYP
label_flo_typ.grid(row=2, column=0, pady=5)

radio_axial = tk.Radiobutton(root, text="Axial", variable=flo_typ_var, value='AXI',command=update_flo_typ)
radio_axial.grid(row=3, column=0, pady=5, sticky="w")
radio_mixed = tk.Radiobutton(root, text="Mixed", variable=flo_typ_var, value='MIX',command=update_flo_typ)
radio_mixed.grid(row=3, column=1, pady=5, sticky="w")

label_rgas = tk.Label(root, text="RGAS:") # Label for the RGAS- the characteristic gas constant
label_rgas.grid(row=4, column=0, pady=5)
entry_rgas = tk.Entry(root)
entry_rgas.grid(row=4, column=1, pady=5)

label_gamma = tk.Label(root, text="GAMMA:") # Label for the GAMMA- the specific heat ratio
label_gamma.grid(row=5, column=0, pady=5)
entry_gamma = tk.Entry(root)
entry_gamma.grid(row=5, column=1, pady=5)

label_poin = tk.Label(root, text="Inlet Pressure (in bar):") # Label for the POIN- the inlet pressure
label_poin.grid(row=6, column=0, pady=5)
entry_poin = tk.Entry(root)
entry_poin.grid(row=6, column=1, pady=5)

label_toin = tk.Label(root, text="Inlet Temperature (in K):") # Label for the TOIN- the inlet temperature
label_toin.grid(row=7, column=0, pady=5)
entry_toin = tk.Entry(root)
entry_toin.grid(row=7, column=1, pady=5)

label_designPoint_choice = tk.Label(root, text="Radius of choice:") # Label for the radius of choice
label_designPoint_choice.grid(row=8, column=0, pady=5)
entry_designPoint_choice = ttk.Combobox(root, values=["Mid", "Tip", "Hub"], state="readonly")
entry_designPoint_choice.set("Mid")
entry_designPoint_choice.grid(row=8, column=1, pady=5)

label_rotation_speed = tk.Label(root, text="Rotation Speed:") # Label for the rotation speed
label_rotation_speed.grid(row=9, column=0, pady=5)
entry_rotation_speed = tk.Entry(root)
entry_rotation_speed.grid(row=9, column=1, pady=5)

label_flowin = tk.Label(root, text="Mass flow rate for inlet:") # Label for the inlet mass flow rate
label_flowin.grid(row=10, column=0, pady=5)
entry_flowin = tk.Entry(root)
entry_flowin.grid(row=10, column=1, pady=5)

nstg= tk.StringVar()
label_num_stages= tk.Label(root, text="Number of Stages:") # Label for the number of stages
label_num_stages.grid(row=11, column=0, pady=5)
entry_num_stages = tk.Entry(root, textvariable=nstg)
entry_num_stages.grid(row=11, column=1, pady=5)

# Run the application
root.mainloop()

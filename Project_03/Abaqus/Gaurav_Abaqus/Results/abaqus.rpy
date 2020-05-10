# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_15-19.28.56 126354
# Run by gborgaon on Mon Apr 20 14:56:18 2015
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=451.333312988281, 
    height=277.283325195313)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='Beam_Fine_1st_Order - Copy', 
    inputFileName='C:/Users/gborgaon/Project_03/Beam_Fine_1st_Order - Copy.inp')
#: The model "Beam_Fine_1st_Order - Copy" has been created.
#: The part "PART-1" has been imported from the input file.
#: The model "Beam_Fine_1st_Order - Copy" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Beam_Fine_1st_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.08332, 
    farPlane=10.4175, width=30.5164, height=14.9249, viewOffsetX=-3.27917, 
    viewOffsetY=-0.562428)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.29871, 
    farPlane=12.3723, width=47.0729, height=23.0223, cameraPosition=(6.25882, 
    0.195358, 8.58208), cameraUpVector=(0.066176, 0.717927, -0.692966), 
    cameraTarget=(3.29775, -2.14185, 2.39029), viewOffsetX=-5.05827, 
    viewOffsetY=-0.867571)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.models['Model-1']
a = mdb.models['Beam_Fine_1st_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Beam_Fine_1st_Order - Copy'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.34514, 
    farPlane=9.15571, width=6.94275, height=3.76741, viewOffsetX=0.164881, 
    viewOffsetY=-0.144095)
mdb.models['Beam_Fine_1st_Order - Copy'].Material(name='Al')
mdb.models['Beam_Fine_1st_Order - Copy'].materials['Al'].Elastic(table=((
    69000000000.0, 0.34), ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.81635, 
    farPlane=9.68451, width=16.0758, height=8.7234, viewOffsetX=1.89482, 
    viewOffsetY=-1.00782)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.74865, 
    farPlane=9.40388, width=15.8499, height=8.60078, cameraPosition=(5.01023, 
    1.4191, 5.98347), cameraUpVector=(-0.25738, 0.865345, -0.430039), 
    cameraTarget=(1.60216, 0.0876349, -0.276002), viewOffsetX=1.86819, 
    viewOffsetY=-0.993658)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.93386, 
    farPlane=9.21867, width=13.6781, height=7.42229, viewOffsetX=1.90549, 
    viewOffsetY=-0.764624)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.37857, 
    farPlane=7.87303, width=12.1387, height=6.58695, cameraPosition=(2.43885, 
    0.643833, 6.02278), cameraUpVector=(-0.246626, 0.870913, -0.425072), 
    cameraTarget=(1.30254, -0.363221, -1.06689), viewOffsetX=1.69103, 
    viewOffsetY=-0.678569)
a = mdb.models['Beam_Fine_1st_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Beam_Fine_1st_Order - Copy'].StaticStep(name='Loading', 
    previous='Initial', initialInc=0.001, maxInc=0.02, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
mdb.models['Beam_Fine_1st_Order - Copy'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'E', 'U', 'RF'))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.22093, 
    farPlane=12.45, width=28.4558, height=15.4413, viewOffsetX=-2.08841, 
    viewOffsetY=0.55384)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.73237, 
    farPlane=12.0409, width=26.221, height=14.2286, cameraPosition=(5.98044, 
    3.90802, 7.18108), cameraUpVector=(-0.101162, 0.435235, -0.894615), 
    cameraTarget=(3.49131, -0.942404, 2.40129), viewOffsetX=-1.9244, 
    viewOffsetY=0.510344)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.30961, 
    farPlane=11.4637, width=18.8695, height=10.2393, viewOffsetX=0.00450659, 
    viewOffsetY=1.82191)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.6431, 
    farPlane=12.4591, width=19.8668, height=10.7805, cameraPosition=(9.76649, 
    1.37909, 5.54598), cameraUpVector=(-0.398991, 0.674256, -0.621438), 
    cameraTarget=(4.57525, -1.76463, 1.57901), viewOffsetX=0.00474478, 
    viewOffsetY=1.91821)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.5319, 
    farPlane=12.2944, width=19.5343, height=10.6001, cameraPosition=(9.27945, 
    2.40057, 5.71735), cameraUpVector=(-0.485594, 0.612507, -0.623726), 
    cameraTarget=(4.7139, -1.4547, 1.61108), viewOffsetX=0.00466536, 
    viewOffsetY=1.8861)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.86681, 
    farPlane=11.9595, width=14.1671, height=7.68763, viewOffsetX=0.267587, 
    viewOffsetY=1.85086)
mdb.models['Beam_Fine_1st_Order - Copy'].ExpressionField(
    name='Traction_Variation', localCsys=None, description='', 
    expression=' Y ')
a = mdb.models['Beam_Fine_1st_Order - Copy'].rootAssembly
f1 = a.instances['PART-1-1'].elements
face3Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:2 #10:2 #0:2 #2000 #0 #2000000 #0:4', 
    ' #10 #800 #0:8 #4000000 #80 #0:8 #100000', ' #0 #4000000 ]', ), )
face4Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:2 #28011040 #10500 #0 #8000 #c0080080 #8200000', 
    ' #820 #2a #80200000 #0 #40000 #10800001 #c4', 
    ' #0:8 #48000000 #e0d #0:7 #4000 #4000000 #20000', 
    ' #0:33 #2000000 #0:3 #8000000 #0:10 #10010 #0:8', 
    ' #40000400 #0:3 #10010 #0 #10000000 #40000 ]', ), )
face5Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:2 #4 #1 #0:2 #30800 #0 #20000', 
    ' #0:4 #10000 #0:9 #2000000 #20 #0:7 #800000', 
    ' #0:35 #40000 #0:2 #20000000 #800 #62084 #0:9', 
    ' #706a40 #0:8 #352000 #14000020 #0:2 #706a40 #0', 
    ' #40000000 #aa #1c0000 ]', ), )
face6Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:72 #8000 #400000 #0:9 #40020 #0:8 #1000', 
    ' #2 #0:2 #40020 #0 #20000000 #0 #10000 ]', ), )
region = a.Surface(face3Elements=face3Elements1, face4Elements=face4Elements1, 
    face5Elements=face5Elements1, face6Elements=face6Elements1, 
    name='Traction_Area')
mdb.models['Beam_Fine_1st_Order - Copy'].Pressure(name='Traction', 
    createStepName='Loading', region=region, distributionType=FIELD, 
    field='Traction_Variation', magnitude=-200.0, amplitude=UNSET)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.10565, 
    farPlane=11.7206, width=13.0597, height=7.08669, viewOffsetX=0.444302, 
    viewOffsetY=1.99199)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.86897, 
    farPlane=11.5051, width=12.6247, height=6.85064, cameraPosition=(8.14201, 
    2.09321, 6.7016), cameraUpVector=(-0.334539, 0.634193, -0.697053), 
    cameraTarget=(4.13788, -1.52774, 1.86172), viewOffsetX=0.429503, 
    viewOffsetY=1.92564)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.661, 
    farPlane=11.713, width=16.6813, height=9.05193, viewOffsetX=0.972075, 
    viewOffsetY=2.08447)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.90304, 
    farPlane=9.96916, width=14.7831, height=8.02191, cameraPosition=(3.67562, 
    1.56074, 7.92899), cameraUpVector=(-0.0735097, 0.673669, -0.735368), 
    cameraTarget=(2.72325, -1.8575, 1.60623), viewOffsetX=0.861463, 
    viewOffsetY=1.84727)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.49061, 
    farPlane=9.38158, width=7.73589, height=4.1978, viewOffsetX=0.621121, 
    viewOffsetY=1.77149)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.39726, 
    farPlane=8.91292, width=7.62463, height=4.13743, cameraPosition=(2.47392, 
    1.43128, 7.92162), cameraUpVector=(-0.0366882, 0.678787, -0.733418), 
    cameraTarget=(2.64517, -1.93497, 1.50229), viewOffsetX=0.612187, 
    viewOffsetY=1.74601)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.51919, 
    farPlane=8.791, width=5.7024, height=3.09435, viewOffsetX=0.505247, 
    viewOffsetY=1.81839)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.71948, 
    farPlane=9.45672, width=5.8776, height=3.18942, cameraPosition=(4.38439, 
    0.51266, 7.99075), cameraUpVector=(-0.121253, 0.764625, -0.632966), 
    cameraTarget=(2.7651, -2.03909, 1.4002), viewOffsetX=0.52077, 
    viewOffsetY=1.87426)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.4274, 
    farPlane=9.7488, width=10.4381, height=5.66413, viewOffsetX=0.997579, 
    viewOffsetY=2.10146)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.80451, 
    farPlane=8.30616, width=6.17851, height=3.35271, cameraPosition=(-4.0759, 
    -1.22298, 2.93057), cameraUpVector=(0.528613, 0.84883, 0.00750552), 
    cameraTarget=(1.55769, -1.84413, -1.59112), viewOffsetX=0.590486, 
    viewOffsetY=1.2439)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.88302, 
    farPlane=8.22765, width=9.76411, height=5.2984, viewOffsetX=0.852899, 
    viewOffsetY=1.37132)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.39071, 
    farPlane=8.03056, width=8.52617, height=4.62664, cameraPosition=(-4.26333, 
    0.209014, 2.57621), cameraUpVector=(0.479122, 0.573254, -0.664697), 
    cameraTarget=(1.93374, -3.01198, 0.629321), viewOffsetX=0.744764, 
    viewOffsetY=1.19746)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.97194, 
    farPlane=7.96423, width=9.9877, height=5.41972, cameraPosition=(-2.74379, 
    1.48836, 4.78032), cameraUpVector=(0.346038, 0.515441, -0.78395), 
    cameraTarget=(1.00812, -2.94414, 0.439237), viewOffsetX=0.872429, 
    viewOffsetY=1.40273)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.30463, 
    farPlane=7.63154, width=3.78071, height=2.05156, viewOffsetX=0.120693, 
    viewOffsetY=1.59193)
a = mdb.models['Beam_Fine_1st_Order - Copy'].rootAssembly
region = a.sets['FIXED_SUPPORT']
mdb.models['Beam_Fine_1st_Order - Copy'].DisplacementBC(name='Fixed_Support', 
    createStepName='Loading', region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, 
    ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
a = mdb.models['Beam_Fine_1st_Order - Copy'].rootAssembly
region = a.sets['ROLLER_SUPPORT']
mdb.models['Beam_Fine_1st_Order - Copy'].DisplacementBC(name='Roller_Support', 
    createStepName='Loading', region=region, u1=0.0, u2=UNSET, u3=0.0, ur1=0.0, 
    ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.22562, 
    farPlane=7.71055, width=5.40173, height=2.93119, viewOffsetX=0.411601, 
    viewOffsetY=1.63988)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Linear_Fine', model='Beam_Fine_1st_Order - Copy', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Linear_Fine'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Linear_Fine.inp" has been submitted for analysis.
#: Error in job Linear_Fine: THERE IS NO MATERIAL BY THE NAME DEFAULTMATERIAL
#: Error in job Linear_Fine: 4160 elements have missing property definitions. The elements have been identified in element set ErrElemMissingSection.
#: Job Linear_Fine: Analysis Input File Processor aborted due to errors.
#: Error in job Linear_Fine: Analysis Input File Processor exited with an error.
#: Job Linear_Fine aborted due to errors.
p1 = mdb.models['Beam_Fine_1st_Order - Copy'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Beam_Fine_1st_Order - Copy'].parts['PART-1'].sectionAssignments[0]
del mdb.models['Beam_Fine_1st_Order - Copy'].sections['Section-1-SOLID_SECTION']
mdb.models['Beam_Fine_1st_Order - Copy'].HomogeneousSolidSection(
    name='Section-1', material='Al', thickness=None)
p = mdb.models['Beam_Fine_1st_Order - Copy'].parts['PART-1']
region = p.sets['SOLID_SECTION']
p = mdb.models['Beam_Fine_1st_Order - Copy'].parts['PART-1']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Beam_Fine_1st_Order - Copy'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Linear_Fine'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Linear_Fine.inp" has been submitted for analysis.
#: Job Linear_Fine: Analysis Input File Processor completed successfully.
#: Job Linear_Fine: Abaqus/Standard completed successfully.
#: Job Linear_Fine completed successfully. 
mdb.jobs['Linear_Fine'].submit(consistencyChecking=OFF)
#: The job input file "Linear_Fine.inp" has been submitted for analysis.
#: Job Linear_Fine: Analysis Input File Processor completed successfully.
mdb.jobs['Linear_Fine'].kill()
#: Error in job Linear_Fine: Process terminated by external request (SIGTERM or SIGINT received).
#: Job Linear_Fine: Abaqus/Standard was terminated prior to analysis completion.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
#: Error in job Linear_Fine: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
mdb.models['Beam_Fine_1st_Order - Copy'].steps['Loading'].setValues(maxInc=0.1)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Linear_Fine'].submit(consistencyChecking=OFF)
#: The job input file "Linear_Fine.inp" has been submitted for analysis.
#: Job Linear_Fine: Analysis Input File Processor completed successfully.
#: Job Linear_Fine: Abaqus/Standard completed successfully.
#: Job Linear_Fine completed successfully. 
o3 = session.openOdb(name='C:/Temp/Linear_Fine.odb')
#: Model: C:/Temp/Linear_Fine.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.15267, 
    farPlane=9.34818, width=9.11885, height=5.28594, viewOffsetX=0.0786052, 
    viewOffsetY=-0.442875)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    triadFont='-*-verdana-medium-r-normal-*-*-140-*-*-p-*-*-*', 
    legendFont='-*-verdana-medium-r-normal-*-*-140-*-*-p-*-*-*', 
    titleFont='-*-verdana-medium-r-normal-*-*-140-*-*-p-*-*-*', 
    stateFont='-*-verdana-medium-r-normal-*-*-140-*-*-p-*-*-*')
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxValue=125.477, minValue=5.62553, showMinLocation=ON, showMaxLocation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.15712, 
    farPlane=9.34374, width=9.12672, height=5.29051, viewOffsetX=0.506905, 
    viewOffsetY=-0.374072)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.20221, 
    farPlane=9.61494, width=9.20652, height=5.33677, cameraPosition=(6.58639, 
    2.90121, 4.5429), cameraUpVector=(-0.566389, 0.71627, -0.407627), 
    cameraTarget=(1.69662, -0.110111, 0.116762), viewOffsetX=0.511337, 
    viewOffsetY=-0.377343)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.49521, 
    farPlane=10.0663, width=9.72506, height=5.63735, cameraPosition=(8.29653, 
    0.951117, 3.6747), cameraUpVector=(-0.216301, 0.848267, -0.483381), 
    cameraTarget=(2.06157, 0.151461, 0.0615919), viewOffsetX=0.540137, 
    viewOffsetY=-0.398596)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.24056, 
    farPlane=9.42331, width=9.2744, height=5.37611, cameraPosition=(5.49674, 
    2.2379, 5.72506), cameraUpVector=(-0.342489, 0.79555, -0.499801), 
    cameraTarget=(1.51882, 0.0192687, 0.0839092), viewOffsetX=0.515107, 
    viewOffsetY=-0.380125)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.40801, 
    farPlane=9.25587, width=7.024, height=4.07162, viewOffsetX=0.345588, 
    viewOffsetY=-0.180434)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.46734, 
    farPlane=9.19654, width=6.2745, height=3.63715, viewOffsetX=0.505872, 
    viewOffsetY=-0.134425)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.54568, 
    farPlane=9.11819, width=5.28618, height=3.06425, viewOffsetX=0.250101, 
    viewOffsetY=-0.188938)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
a = mdb.models['Beam_Fine_1st_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.99027, 
    farPlane=7.9459, width=8.36801, height=4.85071, viewOffsetX=0.538941, 
    viewOffsetY=1.40555)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.96101, 
    farPlane=8.12417, width=8.30665, height=4.81514, cameraPosition=(4.59902, 
    -0.777385, 5.82052), cameraUpVector=(-0.170044, 0.80723, -0.565212), 
    cameraTarget=(-0.150234, -2.4391, 0.60016), viewOffsetX=0.534989, 
    viewOffsetY=1.39524)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.7128, 
    farPlane=8.1427, width=7.78614, height=4.51341, cameraPosition=(6.45726, 
    -0.202544, 4.2126), cameraUpVector=(-0.661021, 0.723836, -0.197769), 
    cameraTarget=(0.975396, -2.93065, 0.329898), viewOffsetX=0.501465, 
    viewOffsetY=1.30781)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.38823, 
    farPlane=8.46726, width=13.2461, height=7.67841, viewOffsetX=0.264951, 
    viewOffsetY=0.358797)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.44569, 
    farPlane=7.49738, width=13.4707, height=7.80861, cameraPosition=(3.78196, 
    1.16812, 5.50265), cameraUpVector=(-0.940518, 0.187957, -0.283015), 
    cameraTarget=(2.02973, -3.12931, -0.0678565), viewOffsetX=0.269444, 
    viewOffsetY=0.364881)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.10591, 
    farPlane=6.73891, width=8.23292, height=4.7724, cameraPosition=(5.44964, 
    2.82372, 1.04952), cameraUpVector=(-0.894679, 0.153083, -0.419661), 
    cameraTarget=(1.35414, -3.10416, 1.85943), viewOffsetX=0.164676, 
    viewOffsetY=0.223005)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.77115, 
    farPlane=7.23778, width=10.8336, height=6.27996, cameraPosition=(6.09042, 
    1.94437, 2.25103), cameraUpVector=(-0.849947, 0.46958, -0.238925), 
    cameraTarget=(0.914572, -2.95508, 0.918802), viewOffsetX=0.216696, 
    viewOffsetY=0.293451)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.71297, 
    farPlane=7.29595, width=10.6062, height=6.14812, viewOffsetX=3.55798, 
    viewOffsetY=0.937573)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.364241, 
    farPlane=4.13395, width=1.42398, height=0.825441, cameraPosition=(1.73833, 
    0.675971, 2.93945), cameraUpVector=(-0.786742, 0.259546, -0.560065), 
    cameraTarget=(-0.283468, -4.9609, -1.14796), viewOffsetX=0.477691, 
    viewOffsetY=0.125878)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.730929, 
    farPlane=3.76727, width=6.05344, height=3.50901, viewOffsetX=1.08767, 
    viewOffsetY=0.144587)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.721055, 
    farPlane=3.77714, width=5.97166, height=3.46161, cameraPosition=(5.18654, 
    3.2224, -2.27791), cameraUpVector=(0.606565, -0.774979, 0.177443), 
    cameraTarget=(3.16474, -2.41447, -6.36532), viewOffsetX=1.07298, 
    viewOffsetY=0.142634)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.13976, 
    farPlane=8.27952, width=8.10511, height=4.69831, cameraPosition=(-3.08245, 
    5.56223, 0.208316), cameraUpVector=(0.083671, -0.609022, 0.788728), 
    cameraTarget=(8.48435, 1.30851, 0.913722), viewOffsetX=1.45631, 
    viewOffsetY=0.193592)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.64355, 
    farPlane=8.75364, width=13.2443, height=7.67737, viewOffsetX=0.951473, 
    viewOffsetY=-0.268291)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.9063, 
    farPlane=6.75824, width=6.92941, height=4.01679, cameraPosition=(-1.40334, 
    -2.60514, -1.9487), cameraUpVector=(0.896679, -0.403432, 0.182235), 
    cameraTarget=(5.88273, 5.80434, 3.39699), viewOffsetX=0.497809, 
    viewOffsetY=-0.140369)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.86962, 
    farPlane=7.59901, width=14.0661, height=8.15373, cameraPosition=(-1.27417, 
    2.75329, -4.29812), cameraUpVector=(0.375066, -0.825652, -0.421455), 
    cameraTarget=(3.36933, -4.59503, 4.46674), viewOffsetX=1.01051, 
    viewOffsetY=-0.284937)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.81668, 
    farPlane=8.68221, width=13.8737, height=8.04219, cameraPosition=(5.51279, 
    0.385275, -4.93386), cameraUpVector=(-0.369647, -0.928525, 0.0346792), 
    cameraTarget=(-3.96927, 0.0234702, 2.96185), viewOffsetX=0.996686, 
    viewOffsetY=-0.281039)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.56013, 
    farPlane=8.80832, width=12.9411, height=7.50163, cameraPosition=(5.63528, 
    -2.47247, -4.05622), cameraUpVector=(-0.598164, -0.737464, 0.313604), 
    cameraTarget=(-3.94742, 2.32572, 2.07012), viewOffsetX=0.929691, 
    viewOffsetY=-0.262148)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.66469, 
    farPlane=8.87397, width=13.3212, height=7.72195, cameraPosition=(6.29744, 
    -1.74562, -3.81775), cameraUpVector=(-0.309037, -0.830541, 0.463354), 
    cameraTarget=(-4.28971, 0.542737, 2.10327), viewOffsetX=0.956996, 
    viewOffsetY=-0.269847)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.16611, 
    farPlane=8.37256, width=6.80257, height=3.94326, viewOffsetX=1.38111, 
    viewOffsetY=-0.203228)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.44963, 
    farPlane=8.29932, width=7.26551, height=4.21162, cameraPosition=(3.95375, 
    5.04217, -3.33188), cameraUpVector=(0.0307342, -0.846408, -0.531647), 
    cameraTarget=(-3.00607, -3.53442, 2.18045), viewOffsetX=1.4751, 
    viewOffsetY=-0.217059)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.30513, 
    farPlane=8.59818, width=8.66241, height=5.02136, cameraPosition=(2.38619, 
    6.7871, 1.99549), cameraUpVector=(0.231244, -0.125644, -0.964749), 
    cameraTarget=(-1.7681, -4.18758, -1.8361), viewOffsetX=1.75871, 
    viewOffsetY=-0.258792)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.89733, 
    farPlane=9.08001, width=9.62938, height=5.58189, cameraPosition=(1.23299, 
    3.93014, 6.61154), cameraUpVector=(0.236994, 0.603365, -0.761436), 
    cameraTarget=(-1.14386, -1.79097, -4.06564), viewOffsetX=1.95503, 
    viewOffsetY=-0.287681)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.35921, 
    farPlane=9.67689, width=10.3836, height=6.01906, cameraPosition=(1.65671, 
    -1.1621, 8.182), cameraUpVector=(0.102319, 0.970263, -0.219363), 
    cameraTarget=(-1.55805, 0.758422, -3.58064), viewOffsetX=2.10815, 
    viewOffsetY=-0.310212)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.66523, 
    farPlane=10.4653, width=9.25043, height=5.36222, cameraPosition=(7.04647, 
    2.62652, 5.64026), cameraUpVector=(-0.471411, 0.771744, -0.426829), 
    cameraTarget=(-3.04312, -1.43418, -0.19871), viewOffsetX=1.87809, 
    viewOffsetY=-0.276358)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.9652, 
    farPlane=10.1653, width=5.93735, height=3.44172, viewOffsetX=2.18244, 
    viewOffsetY=-0.238578)
odb = session.odbs['C:/Temp/Linear_Fine.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.21317, 
    farPlane=9.4507, width=10.484, height=6.0773, viewOffsetX=0.905765, 
    viewOffsetY=-0.653502)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.10112, 
    farPlane=7.99335, width=10.2587, height=5.94667, cameraPosition=(1.17869, 
    2.35762, 6.11434), cameraUpVector=(-0.348249, 0.674646, -0.650827), 
    cameraTarget=(1.15028, -0.502067, -0.548251), viewOffsetX=0.886297, 
    viewOffsetY=-0.639456)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.18623, 
    farPlane=7.90824, width=9.80407, height=5.68315, viewOffsetX=0.239196, 
    viewOffsetY=-0.470593)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.15256, 
    farPlane=7.94192, width=9.74041, height=5.64625, cameraPosition=(1.47469, 
    2.53484, 6.03701), cameraUpVector=(0.148999, 0.723591, -0.673955), 
    cameraTarget=(1.44628, -0.324848, -0.625578), viewOffsetX=0.237642, 
    viewOffsetY=-0.467537)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.03018, 
    farPlane=8.96471, width=9.50906, height=5.51214, cameraPosition=(4.39221, 
    -1.63628, 6.16877), cameraUpVector=(-0.146187, 0.988501, -0.0386614), 
    cameraTarget=(1.06575, 0.0737709, -0.0424364), viewOffsetX=0.231998, 
    viewOffsetY=-0.456432)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.78358, 
    farPlane=8.61117, width=9.04288, height=5.24191, cameraPosition=(-1.68505, 
    2.40159, 5.4119), cameraUpVector=(0.0127508, 0.722479, -0.691276), 
    cameraTarget=(1.19049, -0.175592, -0.724725), viewOffsetX=0.220624, 
    viewOffsetY=-0.434055)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.14879, 
    farPlane=8.4825, width=9.73327, height=5.64211, cameraPosition=(-1.05244, 
    0.669058, 6.30165), cameraUpVector=(0.124427, 0.915375, -0.382891), 
    cameraTarget=(1.22206, 0.129303, -0.561595), viewOffsetX=0.237468, 
    viewOffsetY=-0.467193)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.05734, 
    farPlane=8.70781, width=9.56039, height=5.54189, cameraPosition=(-1.81337, 
    -0.166097, 6.05193), cameraUpVector=(0.0362102, 0.951676, -0.304962), 
    cameraTarget=(1.2008, 0.148044, -0.53479), viewOffsetX=0.23325, 
    viewOffsetY=-0.458895)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.60293, 
    farPlane=8.16221, width=2.2551, height=1.30722, viewOffsetX=-0.364616, 
    viewOffsetY=0.261862)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=100000)
session.animationController.animationOptions.setValues(frameRate=49, 
    numScaleFactorFrames=30)
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    triadSize=9)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    triadSize=6)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    titleBox=ON)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    titleBox=OFF)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    triadSize=7)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendDecimalPlaces=5)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=1000000)
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.68378, 
    farPlane=8.08259, width=1.23216, height=0.714248, viewOffsetX=-0.513278, 
    viewOffsetY=0.262875)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.62823, 
    farPlane=8.13815, width=1.92816, height=1.1177, viewOffsetX=-0.446071, 
    viewOffsetY=0.0387702)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=1E+007)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=3E+007)
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.74338, 
    farPlane=8.05885, width=0.203487, height=0.117956, viewOffsetX=-0.753752, 
    viewOffsetY=0.266135)
session.animationController.setValues(animationType=NONE)
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.2507, 
    farPlane=8.55154, width=7.15757, height=4.14904, viewOffsetX=0.667923, 
    viewOffsetY=-0.462999)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.07353, 
    farPlane=9.3673, width=6.91606, height=4.00905, cameraPosition=(6.36526, 
    1.62351, 5.14318), cameraUpVector=(-0.290519, 0.854523, -0.430569), 
    cameraTarget=(1.03465, 0.260304, 0.421408), viewOffsetX=0.645386, 
    viewOffsetY=-0.447377)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.17073, 
    farPlane=9.27011, width=5.50315, height=3.19003, viewOffsetX=0.752261, 
    viewOffsetY=-0.393424)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.19304, 
    farPlane=9.24779, width=5.5269, height=3.20379, viewOffsetX=1.04802, 
    viewOffsetY=-0.202586)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=2E+007)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.19754, 
    farPlane=9.2508, width=6.2604, height=3.62898, viewOffsetX=1.03209, 
    viewOffsetY=-0.227918)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=AUTO)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.26297, 
    farPlane=9.2004, width=5.60133, height=3.24694, viewOffsetX=1.01922, 
    viewOffsetY=-0.179128)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.40369, 
    farPlane=8.71098, width=5.75109, height=3.33375, cameraPosition=(4.6832, 
    0.122297, 6.33617), cameraUpVector=(-0.207626, 0.938522, -0.275803), 
    cameraTarget=(0.806785, 0.0394178, 0.20955), viewOffsetX=1.04647, 
    viewOffsetY=-0.183918)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.28729, 
    farPlane=8.8958, width=5.6272, height=3.26194, cameraPosition=(5.18436, 
    1.22179, 5.97598), cameraUpVector=(-0.306337, 0.874715, -0.375542), 
    cameraTarget=(0.845017, 0.0248023, 0.292125), viewOffsetX=1.02393, 
    viewOffsetY=-0.179956)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.24182, 
    farPlane=8.94126, width=6.71674, height=3.89351, viewOffsetX=0.951579, 
    viewOffsetY=-0.297627)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.21657, 
    farPlane=8.9665, width=6.68439, height=3.87476, viewOffsetX=1.1937, 
    viewOffsetY=-0.012107)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.20191, 
    farPlane=9.05533, width=6.66561, height=3.86387, cameraPosition=(5.25711, 
    2.16586, 5.7015), cameraUpVector=(-0.359646, 0.805423, -0.471115), 
    cameraTarget=(0.86735, 0.0631037, 0.327744), viewOffsetX=1.19034, 
    viewOffsetY=-0.012073)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.30367, 
    farPlane=8.95356, width=5.64465, height=3.27205, viewOffsetX=1.05918, 
    viewOffsetY=0.0448601)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.30962, 
    farPlane=9.05307, width=5.65098, height=3.27572, cameraPosition=(6.17069, 
    0.389637, 5.48531), cameraUpVector=(-0.288291, 0.924782, -0.248328), 
    cameraTarget=(0.966023, 0.0285267, 0.450439), viewOffsetX=1.06037, 
    viewOffsetY=0.0449104)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.30745, 
    farPlane=9.05525, width=5.64867, height=3.27438, viewOffsetX=1.20155, 
    viewOffsetY=-0.553312)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.06389, 
    farPlane=8.65675, width=5.38945, height=3.12412, cameraPosition=(4.7392, 
    1.92847, 5.78049), cameraUpVector=(-0.412865, 0.805832, -0.424473), 
    cameraTarget=(0.676164, -0.126294, 0.137923), viewOffsetX=1.14641, 
    viewOffsetY=-0.52792)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.08183, 
    farPlane=8.63881, width=5.40855, height=3.13519, viewOffsetX=1.09021, 
    viewOffsetY=-0.311232)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.08194, 
    farPlane=8.6387, width=5.40867, height=3.13526, cameraPosition=(4.7461, 
    1.79789, 5.82308), cameraUpVector=(-0.479041, 0.794708, -0.372771), 
    cameraTarget=(0.683059, -0.256873, 0.180509), viewOffsetX=1.09023, 
    viewOffsetY=-0.311239)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.08195, 
    farPlane=8.6387, width=5.40868, height=3.13527, viewOffsetX=1.1166, 
    viewOffsetY=-0.145432)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    compass=OFF)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    compass=ON)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(state=OFF)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(state=ON)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendMinMax=ON)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendMinMax=OFF)
mdb.saveAs(pathName='C:/Temp/Linear_Elements')
#: The model database has been saved to "C:\Temp\Linear_Elements.cae".
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='Beam_Fine_2nd_Order - Copy', 
    inputFileName='C:/Users/gborgaon/Project_03/Beam_Fine_2nd_Order - Copy.inp')
#: The model "Beam_Fine_2nd_Order - Copy" has been created.
#: The part "PART-1" has been imported from the input file.
#: The model "Beam_Fine_2nd_Order - Copy" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.models['Model-1']
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.31638, 
    farPlane=9.18448, width=6.90498, height=4.00263, viewOffsetX=0.514787, 
    viewOffsetY=-0.145591)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Beam_Fine_2nd_Order - Copy'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Beam_Fine_2nd_Order - Copy'].sections['Section-1-BEAM_WITH_HOLE']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Beam_Fine_2nd_Order - Copy'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Beam_Fine_2nd_Order - Copy'].parts.changeKey(fromName='PART-1', 
    toName='Beam_Solid')
#: Warning: One or more instances of this part exists in the
#: assembly. They have been modified to refer to the renamed part.
#: Any assembly features and attributes that depend on the original
#: instance may become invalid due to this operation. You may need
#: to edit assembly attributes, sets, surfaces, and reference points.
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.50054, 
    farPlane=9.00032, width=4.31945, height=2.50387, viewOffsetX=0.102882, 
    viewOffsetY=-0.00725808)
mdb.models['Beam_Fine_2nd_Order - Copy'].Material(name='Al')
mdb.models['Beam_Fine_2nd_Order - Copy'].materials['Al'].Elastic(table=((
    69000000000.0, 0.34), ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.37087, 
    farPlane=9.12998, width=6.13867, height=3.55842, viewOffsetX=0.532557, 
    viewOffsetY=-0.00173331)
mdb.models['Beam_Fine_2nd_Order - Copy'].HomogeneousSolidSection(
    name='Section-1', material='Al', thickness=None)
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Warning: Instance 'PART-1-1' has been modified to refer to renamed part 'Beam_Solid'.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Beam_Fine_2nd_Order - Copy'].StaticStep(name='Loading', 
    previous='Initial', initialInc=0.001, maxInc=0.1, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
mdb.models['Beam_Fine_2nd_Order - Copy'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'E', 'U', 'RF'))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
mdb.models['Beam_Fine_2nd_Order - Copy'].ExpressionField(name='Traction_Load', 
    localCsys=None, description='', expression=' Y ')
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
f1 = a.instances['PART-1-1'].elements
face3Elements1 = f1.getSequenceFromMask(mask=('[#0:10 #1f00000 #0:5 #3e000 ]', 
    ), )
face4Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:5 #1f00000 #0 #f800 #0 #7c #0:2', 
    ' #7c000000 #e0000000 #3 #f801f #1f00 #0:60 #f800', ' #0:3 #f800000 ]', ), 
    )
face5Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:12 #f800 #0:3 #f800000 #0:53 #1f00000 #0', 
    ' #f800 #0 #7c #0:2 #7c000000 #e0000000 #3', ' #f801f #1f00 ]', ), )
face6Elements1 = f1.getSequenceFromMask(mask=('[#0:75 #1f00000 #0:5 #3e000 ]', 
    ), )
region = a.Surface(face3Elements=face3Elements1, face4Elements=face4Elements1, 
    face5Elements=face5Elements1, face6Elements=face6Elements1, 
    name='Traction_Surface')
mdb.models['Beam_Fine_2nd_Order - Copy'].Pressure(name='Normal_Traction', 
    createStepName='Loading', region=region, distributionType=FIELD, 
    field='Traction_Load', magnitude=-200.0, amplitude=UNSET)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.83449, 
    farPlane=9.66636, width=14.8209, height=8.59125, viewOffsetX=1.94244, 
    viewOffsetY=-0.0274949)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.53796, 
    farPlane=6.9575, width=10.8462, height=6.28722, cameraPosition=(0.978554, 
    0.967836, 5.17319), cameraUpVector=(-0.196755, 0.825736, -0.528628), 
    cameraTarget=(0.842903, -0.659955, -1.89085), viewOffsetX=1.42151, 
    viewOffsetY=-0.0201212)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.33568, 
    farPlane=6.56226, width=10.2261, height=5.92778, cameraPosition=(0.108562, 
    -0.429043, 4.78627), cameraUpVector=(-0.214341, 0.904381, -0.36899), 
    cameraTarget=(1.27013, -0.401374, -2.37045), viewOffsetX=1.34024, 
    viewOffsetY=-0.0189708)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.0571, 
    farPlane=6.50157, width=6.30639, height=3.65564, cameraPosition=(-1.94554, 
    0.383873, 2.65246), cameraUpVector=(0.123552, 0.850038, -0.512025), 
    cameraTarget=(2.80617, -0.697358, -2.71604), viewOffsetX=0.82652, 
    viewOffsetY=-0.0116992)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.66273, 
    farPlane=5.89595, width=2.36815, height=1.37275, viewOffsetX=0.165323, 
    viewOffsetY=-0.252001)
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
region = a.sets['FIXED_SUPPORT']
mdb.models['Beam_Fine_2nd_Order - Copy'].DisplacementBC(name='Fixed_Support', 
    createStepName='Loading', region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, 
    ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.73215, 
    farPlane=5.82653, width=1.68316, height=0.975684, viewOffsetX=0.0610051, 
    viewOffsetY=-0.192032)
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
region = a.sets['ROLLER_SUPPORT']
mdb.models['Beam_Fine_2nd_Order - Copy'].DisplacementBC(name='Roller_Support', 
    createStepName='Loading', region=region, u1=0.0, u2=UNSET, u3=0.0, ur1=0.0, 
    ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.62636, 
    farPlane=5.93231, width=3.16774, height=1.83625, viewOffsetX=0.339149, 
    viewOffsetY=-0.0792377)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Quadratic_Fine', model='Beam_Fine_2nd_Order - Copy', 
    description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, 
    queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Quadratic_Fine'].submit(consistencyChecking=OFF)
#: The job input file "Quadratic_Fine.inp" has been submitted for analysis.
#: Error in job Quadratic_Fine: 4160 elements have missing property definitions. The elements have been identified in element set ErrElemMissingSection.
#: Job Quadratic_Fine: Analysis Input File Processor aborted due to errors.
#: Error in job Quadratic_Fine: Analysis Input File Processor exited with an error.
#: Job Quadratic_Fine aborted due to errors.
p1 = mdb.models['Beam_Fine_2nd_Order - Copy'].parts['Beam_Solid']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Beam_Fine_2nd_Order - Copy'].parts['Beam_Solid'].sectionAssignments[0]
del mdb.models['Beam_Fine_2nd_Order - Copy'].sections['Section-1']
del mdb.models['Beam_Fine_2nd_Order - Copy'].parts['Beam_Solid'].sets['BEAM_WITH_HOLE']
mdb.models['Beam_Fine_2nd_Order - Copy'].HomogeneousSolidSection(
    name='Section-1', material='Al', thickness=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.04393, 
    farPlane=9.45692, width=10.7034, height=6.20444, viewOffsetX=1.74505, 
    viewOffsetY=0.046101)
p = mdb.models['Beam_Fine_2nd_Order - Copy'].parts['Beam_Solid']
e = p.elements
elements = e.getSequenceFromMask(mask=('[#ffffffff:130 ]', ), )
region = p.Set(elements=elements, name='Set-1')
p = mdb.models['Beam_Fine_2nd_Order - Copy'].parts['Beam_Solid']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Quadratic_Fine'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Quadratic_Fine.inp" has been submitted for analysis.
#: Job Quadratic_Fine: Analysis Input File Processor completed successfully.
#: Job Quadratic_Fine: Abaqus/Standard completed successfully.
#: Job Quadratic_Fine completed successfully. 
o3 = session.openOdb(name='C:/Temp/Quadratic_Fine.odb')
#: Model: C:/Temp/Quadratic_Fine.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Quadratic_Fine'].submit(consistencyChecking=OFF)
#: The job input file "Quadratic_Fine.inp" has been submitted for analysis.
#: Job Quadratic_Fine: Analysis Input File Processor completed successfully.
#: Job Quadratic_Fine: Abaqus/Standard completed successfully.
#: Job Quadratic_Fine completed successfully. 
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.38944, 
    farPlane=6.16923, width=6.46848, height=3.7496, viewOffsetX=0.389443, 
    viewOffsetY=-0.0881862)
o3 = session.openOdb(name='C:/Temp/Quadratic_Fine.odb')
#: Model: C:/Temp/Quadratic_Fine.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.48203, 
    farPlane=9.01882, width=4.5797, height=2.65473, viewOffsetX=0.254595, 
    viewOffsetY=-0.0883355)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.60878, 
    farPlane=8.73696, width=4.68559, height=2.7161, cameraPosition=(4.61983, 
    2.51907, 5.94914), cameraUpVector=(-0.194435, 0.75761, -0.623075), 
    cameraTarget=(1.60043, -0.0562049, -0.118796), viewOffsetX=0.260481, 
    viewOffsetY=-0.0903779)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.53171, 
    farPlane=8.81402, width=5.91893, height=3.43104, viewOffsetX=0.301776, 
    viewOffsetY=-0.00312829)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.42704, 
    farPlane=9.29619, width=5.80694, height=3.36612, cameraPosition=(6.80319, 
    1.15912, 4.97448), cameraUpVector=(-0.344024, 0.872104, -0.34797), 
    cameraTarget=(1.66031, -0.0770247, 0.0155111), viewOffsetX=0.296066, 
    viewOffsetY=-0.0030691)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.50381, 
    farPlane=9.21942, width=4.59789, height=2.66527, viewOffsetX=0.265187, 
    viewOffsetY=0.00228509)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.52379, 
    farPlane=9.17216, width=4.61459, height=2.67495, cameraPosition=(6.64759, 
    1.26217, 5.09176), cameraUpVector=(-0.386818, 0.862467, -0.326377), 
    cameraTarget=(1.6546, -0.0968405, 0.0131887), viewOffsetX=0.26615, 
    viewOffsetY=0.00229339)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.49693, 
    farPlane=9.19107, width=4.59215, height=2.66194, cameraPosition=(6.59355, 
    1.95345, 4.91883), cameraUpVector=(-0.419667, 0.81201, -0.405609), 
    cameraTarget=(1.6549, -0.0733375, 0.0126445), viewOffsetX=0.264856, 
    viewOffsetY=0.00228224)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.40353, 
    farPlane=9.28447, width=6.20126, height=3.5947, viewOffsetX=0.235133, 
    viewOffsetY=-0.199865)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.13592, 
    farPlane=8.23382, width=7.04178, height=4.08193, cameraPosition=(1.51162, 
    -1.47172, 7.03618), cameraUpVector=(-0.280197, 0.944627, -0.170793), 
    cameraTarget=(1.48603, -0.211795, -0.1039), viewOffsetX=0.267003, 
    viewOffsetY=-0.226955)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.84751, 
    farPlane=9.0898, width=6.71079, height=3.89006, cameraPosition=(3.48995, 
    -4.80963, 5.3664), cameraUpVector=(-0.632699, 0.688064, 0.35533), 
    cameraTarget=(1.4522, -0.3939, -0.0111148), viewOffsetX=0.254453, 
    viewOffsetY=-0.216287)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.23043, 
    farPlane=9.17252, width=7.15024, height=4.1448, cameraPosition=(3.46802, 
    -7.36644, 1.10214), cameraUpVector=(-0.341384, 0.396677, 0.852117), 
    cameraTarget=(1.4852, -0.489474, -0.0573778), viewOffsetX=0.271116, 
    viewOffsetY=-0.23045)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.2033, 
    farPlane=9.62954, width=7.1191, height=4.12675, cameraPosition=(4.22114, 
    -6.5871, -3.45415), cameraUpVector=(-0.333969, -0.212029, 0.918427), 
    cameraTarget=(1.54751, -0.57577, -0.407137), viewOffsetX=0.269935, 
    viewOffsetY=-0.229446)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.33005, 
    farPlane=9.79444, width=7.26457, height=4.21107, cameraPosition=(4.23207, 
    -4.19302, -6.32601), cameraUpVector=(-0.241259, -0.627756, 0.740078), 
    cameraTarget=(1.56857, -0.425603, -0.733062), viewOffsetX=0.275451, 
    viewOffsetY=-0.234134)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.52157, 
    farPlane=9.82992, width=7.48436, height=4.33848, cameraPosition=(4.30151, 
    -1.46514, -7.54539), cameraUpVector=(-0.22889, -0.865407, 0.445735), 
    cameraTarget=(1.58021, -0.1442, -0.956127), viewOffsetX=0.283785, 
    viewOffsetY=-0.241218)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.31953, 
    farPlane=10.087, width=7.2525, height=4.20407, cameraPosition=(5.8716, 
    -1.15491, -6.85096), cameraUpVector=(-0.272155, -0.88561, 0.376334), 
    cameraTarget=(1.79436, -0.121342, -0.945323), viewOffsetX=0.274993, 
    viewOffsetY=-0.233745)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.33409, 
    farPlane=10.0724, width=7.26921, height=4.21376, viewOffsetX=0.802087, 
    viewOffsetY=0.150627)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.31288, 
    farPlane=10.4063, width=7.24487, height=4.19965, cameraPosition=(7.11008, 
    -1.90407, -5.90582), cameraUpVector=(-0.392675, -0.839279, 0.376056), 
    cameraTarget=(2.06614, -0.216007, -0.978567), viewOffsetX=0.799401, 
    viewOffsetY=0.150123)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.31456, 
    farPlane=10.4046, width=7.2468, height=4.20077, viewOffsetX=0.708777, 
    viewOffsetY=-0.102287)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.37555, 
    farPlane=10.3436, width=6.07722, height=3.52279, viewOffsetX=0.535355, 
    viewOffsetY=-0.195649)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.40065, 
    farPlane=10.3185, width=6.10114, height=3.53666, viewOffsetX=0.482229, 
    viewOffsetY=0.0373748)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.37341, 
    farPlane=10.3912, width=6.07517, height=3.52161, cameraPosition=(7.43891, 
    -2.37403, -5.42691), cameraUpVector=(-0.447493, -0.806774, 0.38583), 
    cameraTarget=(2.13931, -0.285032, -0.941489), viewOffsetX=0.480176, 
    viewOffsetY=0.0372157)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.37523, 
    farPlane=10.3893, width=6.07691, height=3.52262, viewOffsetX=0.581877, 
    viewOffsetY=-0.216808)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.38908, 
    farPlane=10.4108, width=6.09012, height=3.53027, cameraPosition=(7.5806, 
    -2.0664, -5.4237), cameraUpVector=(-0.440661, -0.827844, 0.347119), 
    cameraTarget=(2.17045, -0.233597, -0.958297), viewOffsetX=0.583141, 
    viewOffsetY=-0.217279)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.34699, 
    farPlane=10.3763, width=6.05, height=3.50702, cameraPosition=(7.33096, 
    -2.97594, -5.21196), cameraUpVector=(-0.518121, -0.757175, 0.397791), 
    cameraTarget=(2.11688, -0.34323, -0.916506), viewOffsetX=0.579299, 
    viewOffsetY=-0.215848)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.34972, 
    farPlane=10.3736, width=6.05261, height=3.50853, viewOffsetX=0.655417, 
    viewOffsetY=-0.0936484)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.42384, 
    farPlane=10.2995, width=4.78073, height=2.77126, viewOffsetX=0.556656, 
    viewOffsetY=-0.202777)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.44423, 
    farPlane=10.2791, width=4.79591, height=2.78005, viewOffsetX=0.531705, 
    viewOffsetY=-0.190055)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.animationController.setValues(animationType=HARMONIC, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.animationOptions.setValues(numScaleFactorFrames=40)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.42384, 
    farPlane=10.2995, width=4.78073, height=2.77126, viewOffsetX=0.738798, 
    viewOffsetY=-0.139526)
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.42119, 
    farPlane=10.3021, width=5.40829, height=3.13504, viewOffsetX=0.723588, 
    viewOffsetY=-0.22061)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.71815, 
    farPlane=9.66276, width=5.6584, height=3.28002, cameraPosition=(4.46703, 
    1.49365, -7.5475), cameraUpVector=(-0.839921, -0.54211, -0.025506), 
    cameraTarget=(1.70084, 1.00684, -0.8632), viewOffsetX=0.757051, 
    viewOffsetY=-0.230812)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.58654, 
    farPlane=9.79436, width=7.55897, height=4.38173, viewOffsetX=1.02236, 
    viewOffsetY=-0.224889)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.50396, 
    farPlane=10.712, width=7.46419, height=4.32678, cameraPosition=(7.16254, 
    6.06889, -2.54218), cameraUpVector=(-0.73018, -0.128609, -0.671042), 
    cameraTarget=(2.11775, 1.63855, 0.194752), viewOffsetX=1.00954, 
    viewOffsetY=-0.222069)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.0076, 
    farPlane=11.0991, width=8.04218, height=4.66183, cameraPosition=(6.27407, 
    4.51317, 6.33816), cameraUpVector=(-0.308368, 0.62172, -0.719982), 
    cameraTarget=(1.75731, 1.00203, 1.88401), viewOffsetX=1.08771, 
    viewOffsetY=-0.239265)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.11426, 
    farPlane=11.1401, width=8.16459, height=4.73279, cameraPosition=(5.83637, 
    3.27149, 7.42938), cameraUpVector=(-0.217144, 0.739615, -0.637038), 
    cameraTarget=(1.64449, 0.713877, 2.09502), viewOffsetX=1.10427, 
    viewOffsetY=-0.242907)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.2261, 
    farPlane=11.5234, width=8.29295, height=4.80719, cameraPosition=(8.52389, 
    -0.297725, 6.33863), cameraUpVector=(-0.184686, 0.943252, -0.275983), 
    cameraTarget=(2.52307, -0.0996865, 2.27421), viewOffsetX=1.12163, 
    viewOffsetY=-0.246726)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.21625, 
    farPlane=11.5333, width=8.28165, height=4.80064, viewOffsetX=2.01401, 
    viewOffsetY=-0.29832)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.65065, 
    farPlane=12.2107, width=8.78018, height=5.08963, cameraPosition=(10.0779, 
    -3.33654, 4.04997), cameraUpVector=(-0.0917506, 0.990785, 0.0996331), 
    cameraTarget=(3.39732, -1.31825, 2.08417), viewOffsetX=2.13525, 
    viewOffsetY=-0.316278)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.58821, 
    farPlane=12.2157, width=8.70852, height=5.04809, cameraPosition=(9.52821, 
    -4.0597, 4.44857), cameraUpVector=(-0.0440014, 0.988859, 0.142206), 
    cameraTarget=(3.11847, -1.57027, 2.14946), viewOffsetX=2.11782, 
    viewOffsetY=-0.313697)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.59017, 
    farPlane=12.2137, width=8.71077, height=5.04939, viewOffsetX=2.452, 
    viewOffsetY=0.323465)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.75594, 
    farPlane=12.048, width=6.14054, height=3.5595, viewOffsetX=2.06501, 
    viewOffsetY=0.431908)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.78194, 
    farPlane=12.022, width=6.16112, height=3.57143, viewOffsetX=2.15774, 
    viewOffsetY=0.034145)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.77735, 
    farPlane=12.0265, width=5.8465, height=3.38906, viewOffsetX=2.10012, 
    viewOffsetY=0.0514151)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.68854, 
    farPlane=11.8566, width=5.77974, height=3.35036, cameraPosition=(9.43149, 
    -2.48253, 5.37508), cameraUpVector=(-0.112627, 0.992939, -0.0372569), 
    cameraTarget=(3.01773, -0.887924, 2.39366), viewOffsetX=2.07614, 
    viewOffsetY=0.050828)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.42558, 
    farPlane=11.3471, width=5.58207, height=3.23577, cameraPosition=(7.46788, 
    1.68893, 7.21961), cameraUpVector=(-0.282126, 0.865323, -0.414273), 
    cameraTarget=(2.05272, 0.481714, 2.55201), viewOffsetX=2.00513, 
    viewOffsetY=0.0490896)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.37718, 
    farPlane=11.2523, width=5.54568, height=3.21468, cameraPosition=(6.50568, 
    4.44943, 6.66476), cameraUpVector=(-0.34834, 0.676215, -0.649147), 
    cameraTarget=(1.69729, 1.30253, 2.24386), viewOffsetX=1.99206, 
    viewOffsetY=0.0487696)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.36408, 
    farPlane=11.141, width=5.53583, height=3.20897, cameraPosition=(6.4202, 
    3.03022, 7.42524), cameraUpVector=(-0.65783, 0.684965, -0.313183), 
    cameraTarget=(1.91978, 0.0290631, 2.59749), viewOffsetX=1.98852, 
    viewOffsetY=0.048683)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.6599, 
    farPlane=11.8019, width=5.75821, height=3.33788, cameraPosition=(10.2821, 
    1.98754, 4.1189), cameraUpVector=(-0.584278, 0.811195, -0.0241177), 
    cameraTarget=(3.53114, 0.0507922, 2.31866), viewOffsetX=2.0684, 
    viewOffsetY=0.0506387)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.55859, 
    farPlane=11.6749, width=5.68206, height=3.29374, cameraPosition=(9.57959, 
    0.529583, 5.51113), cameraUpVector=(-0.491197, 0.870853, -0.0184503), 
    cameraTarget=(3.03521, -0.449312, 2.54799), viewOffsetX=2.04104, 
    viewOffsetY=0.049969)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.56311, 
    farPlane=11.6704, width=5.68547, height=3.29571, cameraPosition=(9.47666, 
    1.14689, 5.53453), cameraUpVector=(-0.399886, 0.888295, -0.225882), 
    cameraTarget=(2.93228, 0.168, 2.57139), viewOffsetX=2.04226, 
    viewOffsetY=0.0499989)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.48375, 
    farPlane=11.617, width=5.62581, height=3.26113, cameraPosition=(8.87141, 
    2.64852, 5.73298), cameraUpVector=(-0.429705, 0.811547, -0.39591), 
    cameraTarget=(2.64498, 0.767117, 2.52998), viewOffsetX=2.02083, 
    viewOffsetY=0.0494742)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.48798, 
    farPlane=11.6127, width=5.629, height=3.26297, viewOffsetX=2.01805, 
    viewOffsetY=-0.299542)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.3581, 
    farPlane=11.4124, width=5.53136, height=3.20638, cameraPosition=(7.82092, 
    3.68407, 6.15763), cameraUpVector=(-0.593343, 0.718904, -0.362106), 
    cameraTarget=(2.25096, 0.670594, 2.62749), viewOffsetX=1.98305, 
    viewOffsetY=-0.294346)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.40089, 
    farPlane=11.4834, width=5.56353, height=3.22503, cameraPosition=(8.23023, 
    3.44116, 5.93745), cameraUpVector=(-0.543908, 0.750132, -0.37612), 
    cameraTarget=(2.39219, 0.749081, 2.58523), viewOffsetX=1.99458, 
    viewOffsetY=-0.296058)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.399, 
    farPlane=11.4853, width=5.56212, height=3.22421, viewOffsetX=2.07928, 
    viewOffsetY=-0.086719)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    triadFont='-*-verdana-bold-r-normal-*-*-140-*-*-p-*-*-*', 
    legendFont='-*-verdana-bold-r-normal-*-*-140-*-*-p-*-*-*', 
    titleFont='-*-verdana-bold-r-normal-*-*-140-*-*-p-*-*-*', 
    stateFont='-*-verdana-bold-r-normal-*-*-140-*-*-p-*-*-*')
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    triadFont='-*-verdana-medium-r-normal-*-*-140-*-*-p-*-*-*', 
    legendFont='-*-verdana-medium-r-normal-*-*-140-*-*-p-*-*-*', 
    titleFont='-*-verdana-medium-r-normal-*-*-140-*-*-p-*-*-*', 
    stateFont='-*-verdana-medium-r-normal-*-*-140-*-*-p-*-*-*')
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Beam_Fine_2nd_Order - Copy'].loads['Normal_Traction'].setValues(
    magnitude=-200000000.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.05932, 
    farPlane=6.49935, width=11.0109, height=6.38272, viewOffsetX=0.789531, 
    viewOffsetY=-0.198883)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.65593, 
    farPlane=7.41044, width=14.2009, height=8.23186, cameraPosition=(4.23067, 
    1.10886, 4.47216), cameraUpVector=(-0.614361, 0.763958, -0.197306), 
    cameraTarget=(-1.12935, -1.15526, 0.146354), viewOffsetX=1.01827, 
    viewOffsetY=-0.256501)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.51665, 
    farPlane=7.74481, width=13.4562, height=7.80019, cameraPosition=(5.87006, 
    1.83142, 2.59248), cameraUpVector=(-0.522947, 0.787372, -0.326454), 
    cameraTarget=(-0.937708, -0.213184, 1.16331), viewOffsetX=0.964872, 
    viewOffsetY=-0.24305)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.52173, 
    farPlane=7.7553, width=13.4834, height=7.81595, cameraPosition=(5.14985, 
    0.984305, 3.89029), cameraUpVector=(-0.409389, 0.86923, -0.277198), 
    cameraTarget=(-1.16416, -0.272604, 0.555329), viewOffsetX=0.966821, 
    viewOffsetY=-0.243541)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.79554, 
    farPlane=7.48149, width=9.11148, height=5.28167, viewOffsetX=1.04997, 
    viewOffsetY=-0.0188643)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Quadratic_Fine'].submit(consistencyChecking=OFF)
#: The job input file "Quadratic_Fine.inp" has been submitted for analysis.
#: Job Quadratic_Fine: Analysis Input File Processor completed successfully.
o7 = session.odbs['C:/Temp/Linear_Fine.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.odbs['C:/Temp/Linear_Fine.odb'].close()
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Beam_Fine_2nd_Order - Copy'].steps['Loading'].setValues(
    initialInc=0.01)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
#: Job Quadratic_Fine: Abaqus/Standard completed successfully.
#: Job Quadratic_Fine completed successfully. 
o3 = session.openOdb(name='C:/Temp/Quadratic_Fine.odb')
#: Model: C:/Temp/Quadratic_Fine.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.20136, 
    farPlane=9.30446, width=7.58336, height=4.39587, viewOffsetX=0.761302, 
    viewOffsetY=0.0250228)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.1874, 
    farPlane=9.31227, width=7.56301, height=4.38407, cameraPosition=(6.51265, 
    2.01717, 4.87802), cameraUpVector=(-0.744542, 0.654971, -0.12911), 
    cameraTarget=(1.83344, -0.576619, -0.0154422), viewOffsetX=0.759259, 
    viewOffsetY=0.0249557)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.42441, 
    farPlane=9.6707, width=7.90856, height=4.58437, cameraPosition=(7.0705, 
    4.32934, 2.69537), cameraUpVector=(-0.742152, 0.545135, -0.38992), 
    cameraTarget=(1.90115, -0.0822162, 0.168575), viewOffsetX=0.793949, 
    viewOffsetY=0.0260959)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.26099, 
    farPlane=9.58145, width=7.67029, height=4.44626, cameraPosition=(7.14917, 
    1.81441, 4.4653), cameraUpVector=(-0.454849, 0.812419, -0.364811), 
    cameraTarget=(1.71111, -0.207889, 0.117137), viewOffsetX=0.770029, 
    viewOffsetY=0.0253097)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.3936, 
    farPlane=9.44884, width=5.77116, height=3.34538, viewOffsetX=0.574571, 
    viewOffsetY=0.196567)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.0426, 
    farPlane=10.2184, width=6.46558, height=3.74792, cameraPosition=(8.85331, 
    -1.92585, -2.95868), cameraUpVector=(-0.300028, 0.855767, -0.421481), 
    cameraTarget=(2.56232, 0.145538, -0.00884587), viewOffsetX=0.643707, 
    viewOffsetY=0.22022)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.22574, 
    farPlane=10.0352, width=3.17036, height=1.83777, viewOffsetX=0.826591, 
    viewOffsetY=0.194891)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.65523, 
    farPlane=10.0573, width=3.38908, height=1.96455, cameraPosition=(7.31706, 
    -2.03155, -5.68462), cameraUpVector=(-0.345234, 0.916252, -0.203213), 
    cameraTarget=(2.6737, 0.00595882, -0.502291), viewOffsetX=0.883615, 
    viewOffsetY=0.208335)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.27982, 
    farPlane=10.4327, width=8.64159, height=5.00929, viewOffsetX=0.680569, 
    viewOffsetY=0.157349)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.83403, 
    farPlane=10.1879, width=8.02813, height=4.65369, cameraPosition=(6.95652, 
    1.42645, 5.76045), cameraUpVector=(-0.218893, 0.855313, -0.469601), 
    cameraTarget=(1.48595, 0.312178, 1.13443), viewOffsetX=0.632256, 
    viewOffsetY=0.146179)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.97821, 
    farPlane=10.1634, width=8.22653, height=4.7687, cameraPosition=(5.85125, 
    3.76445, 5.72769), cameraUpVector=(-0.358961, 0.675655, -0.643923), 
    cameraTarget=(1.33014, 0.513975, 1.08412), viewOffsetX=0.647881, 
    viewOffsetY=0.149791)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.96876, 
    farPlane=10.1729, width=8.21353, height=4.76116, viewOffsetX=1.43618, 
    viewOffsetY=0.075161)
session.viewports['Viewport: 1'].view.setValues(width=8.29634, height=4.80916, 
    viewOffsetX=1.44592, viewOffsetY=0.0789745)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.97268, 
    farPlane=10.24, width=8.30195, height=4.81241, cameraPosition=(6.28851, 
    2.85555, 5.95173), cameraUpVector=(-0.387286, 0.757346, -0.525773), 
    cameraTarget=(1.44866, 0.278466, 1.20797), viewOffsetX=1.44689, 
    viewOffsetY=0.0790279)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.97172, 
    farPlane=10.241, width=8.30061, height=4.81164, viewOffsetX=1.79926, 
    viewOffsetY=0.00961639)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.60848, 
    farPlane=11.1338, width=9.1857, height=5.3247, cameraPosition=(9.68917, 
    0.733503, 3.56301), cameraUpVector=(-0.460948, 0.88413, -0.0764266), 
    cameraTarget=(2.79763, -0.299007, 1.56068), viewOffsetX=1.99111, 
    viewOffsetY=0.0106418)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.04517, 
    farPlane=10.6033, width=8.40272, height=4.87082, cameraPosition=(7.30071, 
    2.70986, 5.47892), cameraUpVector=(-0.638131, 0.724863, -0.259544), 
    cameraTarget=(1.83439, -0.135905, 1.65927), viewOffsetX=1.82139, 
    viewOffsetY=0.00973469)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.37329, 
    farPlane=10.9725, width=8.85881, height=5.13521, cameraPosition=(8.73316, 
    3.27541, 3.70478), cameraUpVector=(-0.470393, 0.736284, -0.486432), 
    cameraTarget=(2.24661, 0.934488, 1.46569), viewOffsetX=1.92025, 
    viewOffsetY=0.0102631)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.19682, 
    farPlane=10.7753, width=8.61352, height=4.99302, cameraPosition=(8.16295, 
    1.63236, 5.15567), cameraUpVector=(-0.40613, 0.853745, -0.325849), 
    cameraTarget=(1.95154, 0.191213, 1.70454), viewOffsetX=1.86708, 
    viewOffsetY=0.00997893)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.27287, 
    farPlane=10.6993, width=8.26327, height=4.78999, viewOffsetX=1.55996, 
    viewOffsetY=-0.242986)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.13912, 
    farPlane=11.2826, width=9.40438, height=5.45146, cameraPosition=(8.27814, 
    2.43196, -5.93783), cameraUpVector=(-0.844293, 0.46726, -0.262368), 
    cameraTarget=(3.29872, 1.52168, -0.746904), viewOffsetX=1.77538, 
    viewOffsetY=-0.276541)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.85153, 
    farPlane=11.8249, width=10.3428, height=5.99546, cameraPosition=(7.16301, 
    -5.30002, -6.31993), cameraUpVector=(-0.491734, 0.697354, -0.521436), 
    cameraTarget=(4.04972, -0.611634, -1.74878), viewOffsetX=1.95254, 
    viewOffsetY=-0.304137)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.93927, 
    farPlane=11.1838, width=10.4584, height=6.06246, cameraPosition=(5.45517, 
    -0.338108, -8.91693), cameraUpVector=(-0.269002, 0.940252, 0.208721), 
    cameraTarget=(3.8795, 0.215284, -1.86144), viewOffsetX=1.97436, 
    viewOffsetY=-0.307536)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.70327, 
    farPlane=11.5098, width=8.83024, height=5.11865, cameraPosition=(10.1735, 
    3.22289, 1.54991), cameraUpVector=(-0.61863, 0.777155, -0.115443), 
    cameraTarget=(3.30987, 0.949022, 2.08767), viewOffsetX=1.66699, 
    viewOffsetY=-0.259658)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.79275, 
    farPlane=11.469, width=8.94811, height=5.18698, cameraPosition=(9.06958, 
    2.68126, 4.89283), cameraUpVector=(-0.533245, 0.810611, -0.241992), 
    cameraTarget=(2.46516, 0.659739, 2.68733), viewOffsetX=1.68924, 
    viewOffsetY=-0.263124)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.79555, 
    farPlane=11.4662, width=8.95182, height=5.18912, viewOffsetX=2.93671, 
    viewOffsetY=0.110983)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.40451, 
    farPlane=10.8953, width=8.43671, height=4.89053, cameraPosition=(7.25253, 
    0.906018, 6.8028), cameraUpVector=(-0.394044, 0.890894, -0.225914), 
    cameraTarget=(1.34865, -0.0328371, 2.70013), viewOffsetX=2.76772, 
    viewOffsetY=0.104597)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.51076, 
    farPlane=10.7891, width=7.12365, height=4.12938, viewOffsetX=2.63797, 
    viewOffsetY=0.074991)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.63925, 
    farPlane=10.9809, width=7.26423, height=4.21088, cameraPosition=(7.53969, 
    3.80379, 5.66111), cameraUpVector=(-0.606312, 0.708392, -0.361341), 
    cameraTarget=(1.69313, 0.701485, 2.70093), viewOffsetX=2.69003, 
    viewOffsetY=0.0764709)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.63191, 
    farPlane=10.9883, width=7.25621, height=4.20622, viewOffsetX=2.56578, 
    viewOffsetY=-0.408947)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.9543, 
    farPlane=11.3414, width=7.60895, height=4.4107, cameraPosition=(9.37411, 
    1.4365, 5.0518), cameraUpVector=(-0.47359, 0.869381, -0.141025), 
    cameraTarget=(2.57441, 0.160478, 2.88269), viewOffsetX=2.69051, 
    viewOffsetY=-0.428827)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.12132, 
    farPlane=11.1744, width=4.74957, height=2.7532, viewOffsetX=2.3308, 
    viewOffsetY=-0.127137)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.14183, 
    farPlane=11.1539, width=4.76325, height=2.76113, viewOffsetX=2.60951, 
    viewOffsetY=0.230912)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.14188, 
    farPlane=11.1538, width=4.76329, height=2.76115, viewOffsetX=2.47021, 
    viewOffsetY=-0.0179881)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.26578, 
    farPlane=11.1466, width=4.84593, height=2.80905, cameraPosition=(9.73928, 
    -0.133958, 4.77243), cameraUpVector=(-0.32417, 0.942124, -0.085537), 
    cameraTarget=(2.74737, -0.148696, 2.85354), viewOffsetX=2.51306, 
    viewOffsetY=-0.0183002)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.25987, 
    farPlane=11.1525, width=4.84199, height=2.80677, viewOffsetX=2.58183, 
    viewOffsetY=0.113282)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.24027, 
    farPlane=11.1375, width=4.82892, height=2.79919, cameraPosition=(9.62378, 
    -0.236061, 4.931), cameraUpVector=(-0.321151, 0.94389, -0.0770355), 
    cameraTarget=(2.6723, -0.208921, 2.8706), viewOffsetX=2.57486, 
    viewOffsetY=0.112976)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.18528, 
    farPlane=11.1822, width=4.79224, height=2.77793, cameraPosition=(9.52275, 
    1.06265, 4.9756), cameraUpVector=(-0.432396, 0.891561, -0.134731), 
    cameraTarget=(2.64542, 0.121525, 2.88138), viewOffsetX=2.5553, 
    viewOffsetY=0.112118)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.18795, 
    farPlane=11.1796, width=4.79402, height=2.77896, viewOffsetX=2.3526, 
    viewOffsetY=0.0987992)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.2012, 
    farPlane=11.2346, width=4.80286, height=2.78408, cameraPosition=(9.53058, 
    2.65853, 4.39328), cameraUpVector=(-0.561424, 0.806249, -0.186454), 
    cameraTarget=(2.77125, 0.579456, 2.7939), viewOffsetX=2.35694, 
    viewOffsetY=0.0989813)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.20057, 
    farPlane=11.2353, width=4.80244, height=2.78384, viewOffsetX=2.46709, 
    viewOffsetY=-0.182088)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.14387, 
    farPlane=11.087, width=4.76463, height=2.76192, cameraPosition=(8.38367, 
    4.92666, 4.14743), cameraUpVector=(-0.72737, 0.625394, -0.282515), 
    cameraTarget=(2.37551, 1.14167, 2.68288), viewOffsetX=2.44766, 
    viewOffsetY=-0.180654)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.14657, 
    farPlane=11.0843, width=4.76643, height=2.76297, viewOffsetX=2.13326, 
    viewOffsetY=-0.373333)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.14626, 
    farPlane=11.1561, width=4.76622, height=2.76285, cameraPosition=(8.03881, 
    3.84556, 5.62194), cameraUpVector=(-0.534164, 0.731854, -0.423153), 
    cameraTarget=(1.97878, 1.07321, 2.76551), viewOffsetX=2.13317, 
    viewOffsetY=-0.373317)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.16133, 
    farPlane=11.1855, width=4.77627, height=2.76867, cameraPosition=(8.28249, 
    3.71747, 5.4484), cameraUpVector=(-0.512523, 0.74334, -0.429844), 
    cameraTarget=(2.08142, 1.12222, 2.73169), viewOffsetX=2.13767, 
    viewOffsetY=-0.374104)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.20847, 
    farPlane=11.2437, width=4.80771, height=2.7869, cameraPosition=(8.7219, 
    2.97522, 5.43503), cameraUpVector=(-0.470408, 0.797299, -0.378194), 
    cameraTarget=(2.27898, 0.952957, 2.79526), viewOffsetX=2.15174, 
    viewOffsetY=-0.376566)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.20619, 
    farPlane=11.2459, width=4.80619, height=2.78602, viewOffsetX=2.28159, 
    viewOffsetY=-0.202321)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.36666, 
    farPlane=11.2476, width=4.91322, height=2.84806, cameraPosition=(8.96208, 
    -0.0142448, 6.04672), cameraUpVector=(-0.269262, 0.944544, -0.187976), 
    cameraTarget=(2.37975, 0.0632005, 3.00762), viewOffsetX=2.3324, 
    viewOffsetY=-0.206826)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.28915, 
    farPlane=11.2492, width=4.86153, height=2.81809, cameraPosition=(9.00654, 
    4.75488, 3.53358), cameraUpVector=(-0.715193, 0.65398, -0.246596), 
    cameraTarget=(2.74369, 1.23398, 2.55931), viewOffsetX=2.30786, 
    viewOffsetY=-0.20465)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.26163, 
    farPlane=11.3094, width=4.84318, height=2.80746, cameraPosition=(9.37781, 
    3.16367, 4.44262), cameraUpVector=(-0.586078, 0.778646, -0.224106), 
    cameraTarget=(2.74056, 0.785113, 2.75185), viewOffsetX=2.29915, 
    viewOffsetY=-0.203877)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.26311, 
    farPlane=11.308, width=4.84417, height=2.80803, viewOffsetX=1.93529, 
    viewOffsetY=-0.419921)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.28499, 
    farPlane=11.2861, width=4.2932, height=2.48865, viewOffsetX=1.95415, 
    viewOffsetY=-0.360086)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.53859, 
    farPlane=11.3585, width=4.44265, height=2.57528, cameraPosition=(9.91518, 
    0.307741, 4.88789), cameraUpVector=(-0.297593, 0.934417, -0.19571), 
    cameraTarget=(2.95603, 0.251848, 2.85408), viewOffsetX=2.02218, 
    viewOffsetY=-0.372621)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.61933, 
    farPlane=11.558, width=4.49023, height=2.60286, cameraPosition=(8.30272, 
    -3.00739, 6.50396), cameraUpVector=(0.0256592, 0.997939, -0.0588209), 
    cameraTarget=(2.32238, -0.628611, 3.16536), viewOffsetX=2.04384, 
    viewOffsetY=-0.376612)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.32866, 
    farPlane=11.3101, width=4.31893, height=2.50357, cameraPosition=(9.32869, 
    3.66744, 4.18479), cameraUpVector=(-0.610215, 0.754746, -0.240823), 
    cameraTarget=(2.74139, 1.0546, 2.6519), viewOffsetX=1.96587, 
    viewOffsetY=-0.362245)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.34081, 
    farPlane=11.298, width=4.3261, height=2.50772, viewOffsetX=2.08662, 
    viewOffsetY=-0.320648)
session.viewports['Viewport: 1'].view.setValues(width=4.60225, height=2.6678, 
    viewOffsetX=2.0824, viewOffsetY=-0.335655)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.33844, 
    farPlane=11.3436, width=4.60075, height=2.66693, cameraPosition=(9.33083, 
    2.3665, 5.07616), cameraUpVector=(-0.494831, 0.839502, -0.224454), 
    cameraTarget=(2.64147, 0.70159, 2.82901), viewOffsetX=2.08172, 
    viewOffsetY=-0.335546)
session.viewports['Viewport: 1'].view.setValues(width=4.32419, height=2.50662, 
    viewOffsetX=2.13087, viewOffsetY=-0.290122)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
o3 = session.openOdb(name='C:/Temp/Quadratic_Fine.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['Beam_Fine_2nd_Order - Copy'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].setValues(displayedObject=None)
o3 = session.openOdb(name='C:/Temp/Quadratic_Fine.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.12959, 
    farPlane=11.5524, width=7.8008, height=4.52191, viewOffsetX=2.15318, 
    viewOffsetY=-0.567768)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.52476, 
    farPlane=11.5016, width=8.23317, height=4.77254, cameraPosition=(8.36113, 
    4.78051, -5.17755), cameraUpVector=(-0.697568, 0.654861, 0.290784), 
    cameraTarget=(4.3263, 1.8388, 0.0794071), viewOffsetX=2.27253, 
    viewOffsetY=-0.599237)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.25234, 
    farPlane=11.5187, width=9.02924, height=5.234, cameraPosition=(7.37305, 
    0.303066, -8.39762), cameraUpVector=(-0.357876, 0.917786, 0.172027), 
    cameraTarget=(4.85474, 0.681969, -1.60912), viewOffsetX=2.49226, 
    viewOffsetY=-0.657178)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.74681, 
    farPlane=11.5894, width=8.47612, height=4.91337, cameraPosition=(8.61762, 
    2.19712, -6.82076), cameraUpVector=(-0.287443, 0.848678, 0.443985), 
    cameraTarget=(5.18567, 0.641807, -0.626247), viewOffsetX=2.33959, 
    viewOffsetY=-0.61692)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.72471, 
    farPlane=11.3658, width=8.45194, height=4.89936, cameraPosition=(7.79285, 
    3.59297, -6.87596), cameraUpVector=(-0.285456, 0.753771, 0.591899), 
    cameraTarget=(5.04883, 0.924607, -0.718087), viewOffsetX=2.33292, 
    viewOffsetY=-0.61516)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.72913, 
    farPlane=11.3614, width=8.45678, height=4.90216, viewOffsetX=3.67698, 
    viewOffsetY=0.126883)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.03561, 
    farPlane=11.3701, width=8.79212, height=5.09655, cameraPosition=(6.91795, 
    3.71072, -7.76862), cameraUpVector=(-0.411382, 0.786505, 0.460624), 
    cameraTarget=(4.81252, 1.77955, -1.10477), viewOffsetX=3.82278, 
    viewOffsetY=0.131914)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.82687, 
    farPlane=11.4172, width=8.56373, height=4.96416, cameraPosition=(6.90754, 
    6.24172, -5.81641), cameraUpVector=(-0.516945, 0.581744, 0.627967), 
    cameraTarget=(4.63602, 2.29059, -0.177447), viewOffsetX=3.72348, 
    viewOffsetY=0.128487)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.84074, 
    farPlane=11.4034, width=8.57891, height=4.97296, viewOffsetX=3.64047, 
    viewOffsetY=-0.95912)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.97565, 
    farPlane=11.2685, width=6.40443, height=3.71247, viewOffsetX=3.52977, 
    viewOffsetY=-0.68824)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.00272, 
    farPlane=11.2414, width=6.42617, height=3.72507, viewOffsetX=3.34932, 
    viewOffsetY=-0.466714)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendBox=OFF)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    titleBox=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.03183, 
    farPlane=11.2123, width=5.69882, height=3.30345, viewOffsetX=3.25462, 
    viewOffsetY=-0.463451)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.01838, 
    farPlane=11.2425, width=5.68927, height=3.29792, cameraPosition=(7.33007, 
    5.53332, -6.13149), cameraUpVector=(-0.519831, 0.652551, 0.55132), 
    cameraTarget=(4.71013, 2.1869, -0.257274), viewOffsetX=3.24917, 
    viewOffsetY=-0.462675)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.02035, 
    farPlane=11.2405, width=5.69068, height=3.29873, viewOffsetX=3.17071, 
    viewOffsetY=-0.645171)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.93538, 
    farPlane=11.2543, width=5.63039, height=3.26378, cameraPosition=(7.68214, 
    5.47931, -5.77283), cameraUpVector=(-0.510856, 0.652943, 0.559188), 
    cameraTarget=(4.79392, 2.04416, -0.0783609), viewOffsetX=3.13712, 
    viewOffsetY=-0.638336)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.93967, 
    farPlane=11.25, width=5.63344, height=3.26555, viewOffsetX=3.05251, 
    viewOffsetY=-0.626906)
session.viewports['Viewport: 1'].view.setValues(width=5.29544, height=3.06962, 
    viewOffsetX=3.05699, viewOffsetY=-0.596528)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.68446, 
    farPlane=11.5052, width=9.55448, height=5.53847, viewOffsetX=3.80694, 
    viewOffsetY=-0.546493)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.24383, 
    farPlane=10.9498, width=7.76327, height=4.50015, cameraPosition=(10.4401, 
    2.3115, 0.535724), cameraUpVector=(-0.489526, 0.87149, -0.0294761), 
    cameraTarget=(3.59513, 1.31323, 2.70795), viewOffsetX=3.09324, 
    viewOffsetY=-0.44404)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.76218, 
    farPlane=10.2502, width=7.16441, height=4.15301, cameraPosition=(6.99704, 
    2.28568, 6.47029), cameraUpVector=(-0.48563, 0.844185, -0.22697), 
    cameraTarget=(0.570947, 0.661691, 3.53147), viewOffsetX=2.85463, 
    viewOffsetY=-0.409787)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.81414, 
    farPlane=10.1982, width=7.22901, height=4.19046, viewOffsetX=3.51467, 
    viewOffsetY=-0.499104)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.95966, 
    farPlane=10.3694, width=7.40995, height=4.29534, cameraPosition=(7.80151, 
    3.07679, 5.54599), cameraUpVector=(-0.542856, 0.807016, -0.23245), 
    cameraTarget=(1.12795, 1.02059, 3.59554), viewOffsetX=3.60264, 
    viewOffsetY=-0.511596)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.94736, 
    farPlane=10.3816, width=7.39466, height=4.28648, viewOffsetX=3.50252, 
    viewOffsetY=-1.03605)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.95058, 
    farPlane=10.3784, width=6.95474, height=4.03147, viewOffsetX=3.43141, 
    viewOffsetY=-0.991843)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.97773, 
    farPlane=10.3513, width=6.98647, height=4.04987, viewOffsetX=3.56869, 
    viewOffsetY=-0.689708)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.03668, 
    farPlane=10.2923, width=5.86009, height=3.39693, viewOffsetX=3.47736, 
    viewOffsetY=-0.590746)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.06081, 
    farPlane=10.2682, width=5.88351, height=3.41051, viewOffsetX=3.42161, 
    viewOffsetY=-0.740677)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxValue=0.0136592, minValue=0, showMinLocation=OFF, showMaxLocation=OFF)
session.viewports['Viewport: 1'].view.setValues(width=5.53063, height=3.20595, 
    viewOffsetX=3.34819, viewOffsetY=-0.703309)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=10)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.9219, 
    farPlane=9.98664, width=5.40375, height=3.1324, cameraPosition=(5.9523, 
    1.65901, 7.37414), cameraUpVector=(-0.421393, 0.874182, -0.241317), 
    cameraTarget=(0.0017485, 0.460591, 3.40887), viewOffsetX=3.27137, 
    viewOffsetY=-0.687174)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.93017, 
    farPlane=9.97837, width=5.4113, height=3.13678, viewOffsetX=3.5661, 
    viewOffsetY=-0.37144)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.95464, 
    farPlane=9.9539, width=4.80116, height=2.7831, viewOffsetX=3.55219, 
    viewOffsetY=-0.350499)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.04443, 
    farPlane=10.0209, width=4.87355, height=2.82506, cameraPosition=(6.65687, 
    1.32736, 7.06917), cameraUpVector=(-0.383806, 0.900887, -0.202721), 
    cameraTarget=(0.362251, 0.538359, 3.55864), viewOffsetX=3.60575, 
    viewOffsetY=-0.355784)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.04053, 
    farPlane=10.0248, width=4.87041, height=2.82324, viewOffsetX=3.34227, 
    viewOffsetY=-0.56594)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.09038, 
    farPlane=10.1128, width=4.9106, height=2.84654, cameraPosition=(7.32229, 
    1.46312, 6.58955), cameraUpVector=(-0.383238, 0.902071, -0.198484), 
    cameraTarget=(0.740065, 0.698409, 3.64707), viewOffsetX=3.36985, 
    viewOffsetY=-0.57061)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=25)
session.viewports['Viewport: 1'].view.setValues(width=5.16996, height=2.99688, 
    viewOffsetX=3.3382, viewOffsetY=-0.589988)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=AUTO)
mdb.saveAs(pathName='C:/Temp/Quadratic_Fine')
#: The model database has been saved to "C:\Temp\Quadratic_Fine.cae".
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='Linear_Fine', 
    inputFileName='C:/Temp/Linear_Fine.inp')
#: The model "Linear_Fine" has been created.
#: The part "PART-1" has been imported from the input file.
#: 
#: WARNING: The following keywords/parameters are not yet supported by the input file reader:
#: ---------------------------------------------------------------------------------
#: *PREPRINT
#: The model "Linear_Fine" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
a = mdb.models['Linear_Fine'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
del mdb.models['Model-1']
a = mdb.models['Linear_Fine'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.46112, 
    farPlane=9.03974, width=4.87329, height=2.82491, viewOffsetX=-0.0987673, 
    viewOffsetY=-0.120067)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='Linear_Fine', 
    inputFileName='C:/Temp/Linear_Fine.inp')
#: The model "Linear_Fine" has been created.
#: The part "PART-1" has been imported from the input file.
#: The model "Linear_Fine" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
a = mdb.models['Linear_Fine'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.models['Model-1']
a = mdb.models['Linear_Fine'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Linear_Fine'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Linear_Fine'].sections['Section-1-SOLID_SECTION']
mdb.models['Linear_Fine'].Material(name='Al')
mdb.models['Linear_Fine'].materials['Al'].Elastic(table=((69000000000.0, 0.34), 
    ))
mdb.models['Linear_Fine'].HomogeneousSolidSection(name='Section-1', 
    material='Al', thickness=None)
del mdb.models['Linear_Fine'].parts['PART-1'].sectionAssignments[0]
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.50054, 
    farPlane=9.00032, width=4.31945, height=2.50387, viewOffsetX=0.395701, 
    viewOffsetY=-0.0923253)
p = mdb.models['Linear_Fine'].parts['PART-1']
region = p.sets['SOLID_SECTION']
p = mdb.models['Linear_Fine'].parts['PART-1']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Linear_Fine'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Linear_Fine'].StaticStep(name='Loading', previous='Initial', 
    initialInc=0.01, maxInc=0.1, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
mdb.models['Linear_Fine'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'E', 'U', 'RF'))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
mdb.models['Linear_Fine'].ExpressionField(name='Traction_Variation', 
    localCsys=None, description='', expression=' Y ')
a = mdb.models['Linear_Fine'].rootAssembly
f1 = a.instances['PART-1-1'].elements
face3Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:2 #10:2 #0:2 #2000 #0 #2000000 #0:4', 
    ' #10 #800 #0:8 #4000000 #80 #0:8 #100000', ' #0 #4000000 ]', ), )
face4Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:2 #28011040 #10500 #0 #8000 #c0080080 #8200000', 
    ' #820 #2a #80200000 #0 #40000 #10800001 #c4', 
    ' #0:8 #48000000 #e0d #0:7 #4000 #4000000 #20000', 
    ' #0:33 #2000000 #0:3 #8000000 #0:10 #10010 #0:8', 
    ' #40000400 #0:3 #10010 #0 #10000000 #40000 ]', ), )
face5Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:2 #4 #1 #0:2 #30800 #0 #20000', 
    ' #0:4 #10000 #0:9 #2000000 #20 #0:7 #800000', 
    ' #0:35 #40000 #0:2 #20000000 #800 #62084 #0:9', 
    ' #706a40 #0:8 #352000 #14000020 #0:2 #706a40 #0', 
    ' #40000000 #aa #1c0000 ]', ), )
face6Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:72 #8000 #400000 #0:9 #40020 #0:8 #1000', 
    ' #2 #0:2 #40020 #0 #20000000 #0 #10000 ]', ), )
region = a.Surface(face3Elements=face3Elements1, face4Elements=face4Elements1, 
    face5Elements=face5Elements1, face6Elements=face6Elements1, 
    name='Traction_Surface')
mdb.models['Linear_Fine'].Pressure(name='Traction', createStepName='Loading', 
    region=region, distributionType=FIELD, field='Traction_Variation', 
    magnitude=-200000000.0, amplitude=UNSET)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.12272, 
    farPlane=9.37813, width=9.60522, height=5.56788, viewOffsetX=0.768423, 
    viewOffsetY=0.388859)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.80236, 
    farPlane=8.68978, width=9.00454, height=5.21968, cameraPosition=(4.96664, 
    1.01513, 5.75019), cameraUpVector=(0.398306, 0.635676, -0.661262), 
    cameraTarget=(1.1851, 0.756981, -0.430592), viewOffsetX=0.720368, 
    viewOffsetY=0.364541)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.91215, 
    farPlane=8.01316, width=7.33537, height=4.25211, cameraPosition=(-2.09139, 
    2.92065, 3.98548), cameraUpVector=(0.900892, 0.431977, 0.0422975), 
    cameraTarget=(1.90791, 0.726637, -1.65017), viewOffsetX=0.586834, 
    viewOffsetY=0.296966)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.39773, 
    farPlane=7.7184, width=6.37082, height=3.69299, cameraPosition=(-3.65728, 
    -0.113947, 2.34835), cameraUpVector=(0.456577, 0.829365, 0.32201), 
    cameraTarget=(2.36273, 0.994682, -1.5374), viewOffsetX=0.509669, 
    viewOffsetY=0.257917)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.59381, 
    farPlane=7.16412, width=6.73848, height=3.90611, cameraPosition=(-1.75381, 
    -2.20477, 3.78753), cameraUpVector=(0.0874326, 0.972354, 0.216524), 
    cameraTarget=(1.52762, 1.20843, -1.70346), viewOffsetX=0.539082, 
    viewOffsetY=0.272801)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.77638, 
    farPlane=7.77018, width=7.0808, height=4.10454, cameraPosition=(-2.9662, 
    1.44235, 3.44096), cameraUpVector=(0.40791, 0.836595, -0.365674), 
    cameraTarget=(2.01164, -0.274481, -1.54324), viewOffsetX=0.566468, 
    viewOffsetY=0.286659)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.90351, 
    farPlane=7.64305, width=4.74632, height=2.75131, viewOffsetX=0.32445, 
    viewOffsetY=-0.113023)
a = mdb.models['Linear_Fine'].rootAssembly
region = a.sets['FIXED_SUPPORT']
mdb.models['Linear_Fine'].DisplacementBC(name='Fixed_Support', 
    createStepName='Loading', region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, 
    ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.9625, 
    farPlane=7.58406, width=4.00179, height=2.31973, viewOffsetX=0.432853, 
    viewOffsetY=-0.223922)
a = mdb.models['Linear_Fine'].rootAssembly
region = a.sets['ROLLER_SUPPORT']
mdb.models['Linear_Fine'].DisplacementBC(name='Roller_Support', 
    createStepName='Loading', region=region, u1=0.0, u2=UNSET, u3=0.0, ur1=0.0, 
    ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Linear_Fine', model='Linear_Fine', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Linear_Fine'].submit(consistencyChecking=OFF)
#: The job input file "Linear_Fine.inp" has been submitted for analysis.
#: Job Linear_Fine: Analysis Input File Processor completed successfully.
#: Job Linear_Fine: Abaqus/Standard completed successfully.
#: Job Linear_Fine completed successfully. 
o3 = session.openOdb(name='C:/Temp/Linear_Fine.odb')
#: Model: C:/Temp/Linear_Fine.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.34446, 
    farPlane=9.16135, width=6.4719, height=3.75159, viewOffsetX=0.470177, 
    viewOffsetY=-0.025747)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.34542, 
    farPlane=9.41966, width=6.47306, height=3.75226, cameraPosition=(6.80604, 
    3.89364, 3.35441), cameraUpVector=(-0.741942, 0.585681, -0.326343), 
    cameraTarget=(1.77141, -0.176544, 0.0902545), viewOffsetX=0.470262, 
    viewOffsetY=-0.0257516)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.25046, 
    farPlane=9.51462, width=8.14356, height=4.7206, viewOffsetX=0.691084, 
    viewOffsetY=-0.0140983)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.23427, 
    farPlane=9.7074, width=8.11845, height=4.70604, cameraPosition=(7.6521, 
    2.28149, 3.57257), cameraUpVector=(-0.458068, 0.7844, -0.418199), 
    cameraTarget=(1.72842, 0.0264297, 0.0521555), viewOffsetX=0.688953, 
    viewOffsetY=-0.0140548)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.15297, 
    farPlane=9.4392, width=7.99235, height=4.63294, cameraPosition=(6.87957, 
    1.50589, 4.69543), cameraUpVector=(-0.401426, 0.844275, -0.355044), 
    cameraTarget=(1.59057, -0.117005, 0.0091435), viewOffsetX=0.678252, 
    viewOffsetY=-0.0138365)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.11051, 
    farPlane=9.30565, width=7.9265, height=4.59477, cameraPosition=(6.26251, 
    2.48937, 4.80312), cameraUpVector=(-0.397669, 0.764393, -0.507506), 
    cameraTarget=(1.52044, -0.0452095, -0.0607481), viewOffsetX=0.672664, 
    viewOffsetY=-0.0137225)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.11584, 
    farPlane=9.30031, width=7.93477, height=4.59957, viewOffsetX=1.09331, 
    viewOffsetY=-0.190643)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.26432, 
    farPlane=9.15184, width=5.93245, height=3.43888, viewOffsetX=0.652658, 
    viewOffsetY=-0.22543)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.2664, 
    farPlane=9.14976, width=5.93479, height=3.44024, viewOffsetX=1.0662, 
    viewOffsetY=-0.366106)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.34858, 
    farPlane=9.32097, width=6.02741, height=3.49392, cameraPosition=(6.7492, 
    2.12075, 4.66469), cameraUpVector=(-0.438583, 0.794809, -0.419432), 
    cameraTarget=(1.59658, -0.104058, 0.0745563), viewOffsetX=1.08284, 
    viewOffsetY=-0.371819)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.34221, 
    farPlane=9.32735, width=6.02023, height=3.48976, viewOffsetX=0.930625, 
    viewOffsetY=-0.178433)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.39285, 
    farPlane=9.27671, width=5.04771, height=2.92602, viewOffsetX=0.754465, 
    viewOffsetY=-0.217426)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.41375, 
    farPlane=9.25581, width=5.06727, height=2.93736, viewOffsetX=0.736216, 
    viewOffsetY=-0.126476)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.19152, 
    farPlane=9.47803, width=8.48048, height=4.9159, viewOffsetX=1.51132, 
    viewOffsetY=-0.108485)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.61661, 
    farPlane=11.1403, width=10.8084, height=6.26533, cameraPosition=(10.3405, 
    1.38041, -0.26119), cameraUpVector=(-0.534886, 0.827392, 0.171231), 
    cameraTarget=(3.35939, -0.386244, 0.582145), viewOffsetX=1.92617, 
    viewOffsetY=-0.138264)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.99191, 
    farPlane=12.1332, width=13.055, height=7.56762, cameraPosition=(7.58714, 
    3.19379, -7.53495), cameraUpVector=(-0.471052, 0.739393, 0.481049), 
    cameraTarget=(4.26425, 0.528368, -1.66792), viewOffsetX=2.32654, 
    viewOffsetY=-0.167003)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.27036, 
    farPlane=11.8548, width=6.42962, height=3.72707, viewOffsetX=1.67139, 
    viewOffsetY=0.32175)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.29764, 
    farPlane=11.8275, width=6.45082, height=3.73937, viewOffsetX=2.17554, 
    viewOffsetY=0.448655)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.32686, 
    farPlane=11.7983, width=5.72003, height=3.31574, viewOffsetX=2.07511, 
    viewOffsetY=0.535809)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxValue=1.25587E+008, minValue=5.62419E+006, showMinLocation=ON, 
    showMaxLocation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.9947, 
    farPlane=11.7572, width=5.49185, height=3.18348, cameraPosition=(8.79842, 
    3.16101, -6.08948), cameraUpVector=(-0.519972, 0.739663, 0.427232), 
    cameraTarget=(4.42207, 0.414077, -1.00322), viewOffsetX=1.99233, 
    viewOffsetY=0.514436)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.01225, 
    farPlane=11.7397, width=5.50392, height=3.19047, viewOffsetX=1.69774, 
    viewOffsetY=0.465714)
session.viewports['Viewport: 1'].view.setValues(width=5.17372, height=2.99906, 
    viewOffsetX=1.69039, viewOffsetY=0.458124)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.03594, 
    farPlane=11.716, width=5.18898, height=3.00791, viewOffsetX=1.69538, 
    viewOffsetY=0.524551)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendPosition=(1, 98))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
o7 = session.odbs['C:/Temp/Quadratic_Fine.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
o7 = session.odbs['C:/Temp/Linear_Fine.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
o7 = session.odbs['C:/Temp/Quadratic_Fine.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
o7 = session.odbs['C:/Temp/Linear_Fine.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
o7 = session.odbs['C:/Temp/Quadratic_Fine.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.39686, 
    farPlane=9.104, width=5.77464, height=3.3474, viewOffsetX=0.844663, 
    viewOffsetY=-0.29721)
mdb.saveAs(pathName='C:/Temp/Linear_Fine.cae')
#: The model database has been saved to "C:\Temp\Linear_Fine.cae".
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='Beam_2nd_Order_Coarse', 
    inputFileName='C:/Temp/Beam_2nd_Order_Coarse.inp')
#: The model "Beam_2nd_Order_Coarse" has been created.
#: The part "PART-1" has been imported from the input file.
#: The model "Beam_2nd_Order_Coarse" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
a = mdb.models['Beam_2nd_Order_Coarse'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.models['Model-1']
a = mdb.models['Beam_2nd_Order_Coarse'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Beam_2nd_Order_Coarse'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Beam_2nd_Order_Coarse'].materials['AL'].density
del mdb.models['Beam_2nd_Order_Coarse'].sections['Section-1-BEAM_SURFACE']
del mdb.models['Beam_2nd_Order_Coarse'].parts['PART-1'].sets['BEAM_SURFACE']
del mdb.models['Beam_2nd_Order_Coarse'].parts['PART-1'].sectionAssignments[0]
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='Beam_2nd_Order_Coarse', 
    inputFileName='C:/Temp/Beam_2nd_Order_Coarse.inp')
#: The model "Beam_2nd_Order_Coarse" has been created.
#: The part "PART-1" has been imported from the input file.
#: The model "Beam_2nd_Order_Coarse" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
a = mdb.models['Beam_2nd_Order_Coarse'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.models['Model-1']
a = mdb.models['Beam_2nd_Order_Coarse'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.48203, 
    farPlane=9.01882, width=4.5797, height=2.65473, viewOffsetX=0.190094, 
    viewOffsetY=0.032264)
mdb.models['Beam_2nd_Order_Coarse'].StaticStep(name='Loading', 
    previous='Initial', initialInc=0.01, maxInc=0.15, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
mdb.models['Beam_2nd_Order_Coarse'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'E', 'U', 'RF'))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
mdb.models['Beam_2nd_Order_Coarse'].ExpressionField(name='Traction_Variation', 
    localCsys=None, description='', expression=' Y ')
a = mdb.models['Beam_2nd_Order_Coarse'].rootAssembly
f1 = a.instances['PART-1-1'].elements
face3Elements1 = f1.getSequenceFromMask(mask=('[#0:36 #f0000 #f00 ]', ), )
face4Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:11 #f000000 #f000 #0:20 #f000000 #f000 #f000f000 ]', ), )
face5Elements1 = f1.getSequenceFromMask(mask=(
    '[#0:8 #f000000 #f000 #f000f000 #0:25 #f000000 #f000 ]', ), )
face6Elements1 = f1.getSequenceFromMask(mask=('[#0:11 #f0000 #f00 ]', ), )
region = a.Surface(face3Elements=face3Elements1, face4Elements=face4Elements1, 
    face5Elements=face5Elements1, face6Elements=face6Elements1, 
    name='Traction')
mdb.models['Beam_2nd_Order_Coarse'].Pressure(name='Traction', 
    createStepName='Loading', region=region, distributionType=FIELD, 
    field='Traction_Variation', magnitude=-200000000.0, amplitude=UNSET)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.12526, 
    farPlane=9.37559, width=9.57083, height=5.54795, viewOffsetX=1.33334, 
    viewOffsetY=0.26287)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.34434, 
    farPlane=7.31588, width=6.24517, height=3.62015, cameraPosition=(-2.58591, 
    1.20825, 3.60436), cameraUpVector=(0.378304, 0.870847, -0.313864), 
    cameraTarget=(1.16737, 0.150033, -2.50806), viewOffsetX=0.870035, 
    viewOffsetY=0.171528)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.25193, 
    farPlane=7.40828, width=11.2745, height=6.53551, viewOffsetX=1.58262, 
    viewOffsetY=-0.233394)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.47149, 
    farPlane=7.3918, width=15.5027, height=8.9865, cameraPosition=(-0.377778, 
    -1.83616, 5.64617), cameraUpVector=(-0.125492, 0.990426, -0.0575251), 
    cameraTarget=(-0.389002, 0.19839, -1.31293), viewOffsetX=2.17614, 
    viewOffsetY=-0.320922)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.53356, 
    farPlane=7.60486, width=12.2509, height=7.1015, cameraPosition=(-1.78356, 
    0.675006, 4.86759), cameraUpVector=(-0.109017, 0.819976, -0.561921), 
    cameraTarget=(0.0464163, -0.830116, -1.98474), viewOffsetX=1.71968, 
    viewOffsetY=-0.253606)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.94491, 
    farPlane=7.85757, width=13.6771, height=7.92822, cameraPosition=(1.00055, 
    2.92215, 5.47839), cameraUpVector=(0.0244063, 0.716507, -0.697153), 
    cameraTarget=(-0.702125, 0.0787578, -0.970222), viewOffsetX=1.91987, 
    viewOffsetY=-0.283129)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.82561, 
    farPlane=7.65604, width=13.2635, height=7.68848, cameraPosition=(0.374061, 
    4.3454, 4.10326), cameraUpVector=(0.0691931, 0.476191, -0.876615), 
    cameraTarget=(-0.613321, -0.385518, -1.30156), viewOffsetX=1.86181, 
    viewOffsetY=-0.274567)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.26713, 
    farPlane=7.53618, width=11.3272, height=6.56609, cameraPosition=(-1.4357, 
    4.31272, 2.60909), cameraUpVector=(0.619873, 0.511374, -0.595192), 
    cameraTarget=(0.812, 0.0287184, -2.79126), viewOffsetX=1.59002, 
    viewOffsetY=-0.234485)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.30833, 
    farPlane=7.40337, width=11.4701, height=6.64889, cameraPosition=(-2.28802, 
    2.13617, 3.78772), cameraUpVector=(0.395646, 0.82759, -0.398195), 
    cameraTarget=(0.625669, 0.560351, -2.66176), viewOffsetX=1.61007, 
    viewOffsetY=-0.237442)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.03502, 
    farPlane=7.45322, width=10.5225, height=6.09961, cameraPosition=(-3.0414, 
    1.59083, 2.97667), cameraUpVector=(0.356836, 0.870654, -0.33857), 
    cameraTarget=(1.08629, 0.403452, -2.86464), viewOffsetX=1.47706, 
    viewOffsetY=-0.217826)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.61571, 
    farPlane=6.87253, width=3.6367, height=2.1081, viewOffsetX=1.04793, 
    viewOffsetY=-0.646262)
a = mdb.models['Beam_2nd_Order_Coarse'].rootAssembly
region = a.sets['FIXED_SUPPORT']
mdb.models['Beam_2nd_Order_Coarse'].DisplacementBC(name='Fixed_Support', 
    createStepName='Loading', region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, 
    ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
a = mdb.models['Beam_2nd_Order_Coarse'].rootAssembly
region = a.sets['ROLLER_SUPPORT']
mdb.models['Beam_2nd_Order_Coarse'].DisplacementBC(name='Roller_Support', 
    createStepName='Loading', region=region, u1=0.0, u2=UNSET, u3=0.0, ur1=0.0, 
    ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Qudratic_Coarse', model='Beam_2nd_Order_Coarse', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Qudratic_Coarse'].submit(consistencyChecking=OFF)
#: The job input file "Qudratic_Coarse.inp" has been submitted for analysis.
#: Job Qudratic_Coarse: Analysis Input File Processor completed successfully.
#: Job Qudratic_Coarse: Abaqus/Standard completed successfully.
#: Job Qudratic_Coarse completed successfully. 
o3 = session.openOdb(name='C:/Temp/Qudratic_Coarse.odb')
#: Model: C:/Temp/Qudratic_Coarse.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.39443, 
    farPlane=9.11135, width=5.10018, height=2.95643, viewOffsetX=0.346064, 
    viewOffsetY=-0.236853)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    showMinLocation=OFF, showMaxLocation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.44194, 
    farPlane=9.06384, width=4.54621, height=2.63531, viewOffsetX=0.141557, 
    viewOffsetY=-0.185315)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.46107, 
    farPlane=9.04471, width=4.56219, height=2.64457, viewOffsetX=0.354914, 
    viewOffsetY=-0.182788)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.46114, 
    farPlane=9.04463, width=4.56225, height=2.64461, cameraPosition=(5.82217, 
    4.01699, 4.21895), cameraUpVector=(-0.680495, 0.567134, -0.463989), 
    cameraTarget=(1.63613, -0.169045, 0.0329143), viewOffsetX=0.354919, 
    viewOffsetY=-0.18279)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.28898, 
    farPlane=9.21679, width=8.01593, height=4.64661, viewOffsetX=1.22032, 
    viewOffsetY=-0.274415)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.15186, 
    farPlane=9.21922, width=7.80811, height=4.52615, cameraPosition=(5.65678, 
    3.91962, 4.38127), cameraUpVector=(-0.362685, 0.641221, -0.676236), 
    cameraTarget=(1.48477, 0.341826, -0.347622), viewOffsetX=1.18868, 
    viewOffsetY=-0.2673)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.31357, 
    farPlane=9.54256, width=8.05321, height=4.66822, cameraPosition=(6.86697, 
    1.73684, 4.83502), cameraUpVector=(-0.498308, 0.819786, -0.282204), 
    cameraTarget=(1.69486, -0.0909814, 0.09402), viewOffsetX=1.22599, 
    viewOffsetY=-0.27569)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.3135, 
    farPlane=9.60079, width=8.05311, height=4.66817, cameraPosition=(6.95256, 
    1.89609, 4.72171), cameraUpVector=(-0.494857, 0.814563, -0.30266), 
    cameraTarget=(1.71221, -0.0379969, 0.0992905), viewOffsetX=1.22597, 
    viewOffsetY=-0.275687)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.53429, 
    farPlane=9.37999, width=4.80614, height=2.78599, viewOffsetX=0.6213, 
    viewOffsetY=-0.102484)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxValue=1.38629E+008, minValue=123727, showMinLocation=ON, 
    showMaxLocation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.40297, 
    farPlane=9.51131, width=7.23555, height=4.19425, viewOffsetX=1.15762, 
    viewOffsetY=0.0302055)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.493, 
    farPlane=10.8555, width=8.6953, height=5.04043, cameraPosition=(9.86962, 
    2.25366, -0.743688), cameraUpVector=(-0.589437, 0.792926, 0.154377), 
    cameraTarget=(3.0451, 0.0292926, 0.279445), viewOffsetX=1.39116, 
    viewOffsetY=0.0362993)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.64604, 
    farPlane=11.5605, width=10.2394, height=5.93552, cameraPosition=(7.15314, 
    3.05054, -7.2165), cameraUpVector=(-0.48252, 0.753102, 0.447226), 
    cameraTarget=(3.58498, 0.535752, -1.42748), viewOffsetX=1.6382, 
    viewOffsetY=0.0427454)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.53132, 
    farPlane=11.6752, width=10.0858, height=5.84647, viewOffsetX=1.95778, 
    viewOffsetY=0.210752)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.83795, 
    farPlane=11.3686, width=5.65354, height=3.2772, viewOffsetX=1.35574, 
    viewOffsetY=0.117628)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.646, 
    farPlane=11.5605, width=9.04753, height=5.2446, viewOffsetX=2.0433, 
    viewOffsetY=0.0532195)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.73741, 
    farPlane=10.325, width=6.78909, height=3.93545, cameraPosition=(7.53476, 
    0.471827, 5.76915), cameraUpVector=(-0.439433, 0.883134, -0.164237), 
    cameraTarget=(1.21554, -0.568035, 2.36991), viewOffsetX=1.53325, 
    viewOffsetY=0.0399349)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.75447, 
    farPlane=10.3079, width=9.27817, height=5.3783, viewOffsetX=1.81118, 
    viewOffsetY=-0.207644)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.72127, 
    farPlane=10.3411, width=9.22463, height=5.34726, viewOffsetX=3.61225, 
    viewOffsetY=0.153466)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.36964, 
    farPlane=9.94003, width=8.65769, height=5.01862, cameraPosition=(5.8658, 
    3.04507, 5.95636), cameraUpVector=(-0.471815, 0.754078, -0.456899), 
    cameraTarget=(0.389362, 0.422713, 1.99397), viewOffsetX=3.39024, 
    viewOffsetY=0.144034)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.40707, 
    farPlane=9.90261, width=8.71804, height=5.05361, viewOffsetX=2.75213, 
    viewOffsetY=-0.413774)
session.viewports['Viewport: 1'].view.setValues(width=8.80712, height=5.10525, 
    viewOffsetX=2.76122, viewOffsetY=-0.421737)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.71951, 
    farPlane=10.3349, width=9.31495, height=5.39962, cameraPosition=(7.50378, 
    2.30452, 5.33437), cameraUpVector=(-0.416753, 0.829883, -0.37096), 
    cameraTarget=(1.11691, 0.662419, 2.32106), viewOffsetX=2.92043, 
    viewOffsetY=-0.446055)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.90967, 
    farPlane=10.1447, width=6.63976, height=3.84888, viewOffsetX=2.59749, 
    viewOffsetY=-0.292114)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.9528, 
    farPlane=10.2313, width=6.68821, height=3.87697, cameraPosition=(7.85474, 
    1.78795, 5.22881), cameraUpVector=(-0.402488, 0.861506, -0.309533), 
    cameraTarget=(1.2951, 0.517216, 2.41368), viewOffsetX=2.61645, 
    viewOffsetY=-0.294246)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.42666, 
    farPlane=10.5981, width=7.22061, height=4.18559, cameraPosition=(9.64175, 
    0.129637, 3.44791), cameraUpVector=(-0.251799, 0.94242, -0.220096), 
    cameraTarget=(2.47126, 0.547291, 2.45889), viewOffsetX=2.82473, 
    viewOffsetY=-0.317669)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.91404, 
    farPlane=10.3145, width=6.64466, height=3.85173, cameraPosition=(8.01776, 
    2.59725, 4.7528), cameraUpVector=(-0.490421, 0.815193, -0.308136), 
    cameraTarget=(1.39129, 0.719217, 2.48754), viewOffsetX=2.59941, 
    viewOffsetY=-0.29233)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.05577, 
    farPlane=10.1727, width=4.99342, height=2.89455, viewOffsetX=2.48229, 
    viewOffsetY=-0.234274)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.03744, 
    farPlane=10.1085, width=4.9783, height=2.88578, cameraPosition=(7.74428, 
    2.55441, 5.0638), cameraUpVector=(-0.489805, 0.815123, -0.309299), 
    cameraTarget=(1.24415, 0.635958, 2.48768), viewOffsetX=2.47478, 
    viewOffsetY=-0.233565)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.67014, 
    farPlane=10.4758, width=10.4511, height=6.05819, viewOffsetX=2.16401, 
    viewOffsetY=-0.425856)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.84088, 
    farPlane=10.5965, width=12.6089, height=7.30905, cameraPosition=(7.76928, 
    -0.739857, -6.80701), cameraUpVector=(-0.138057, 0.975892, 0.169043), 
    cameraTarget=(4.99787, 0.195422, -0.172777), viewOffsetX=2.61082, 
    viewOffsetY=-0.513785)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.69411, 
    farPlane=10.3811, width=12.3384, height=7.15224, cameraPosition=(3.18158, 
    3.25725, -8.37059), cameraUpVector=(0.259354, 0.715795, 0.648362), 
    cameraTarget=(4.45049, 0.292089, -1.87704), viewOffsetX=2.55481, 
    viewOffsetY=-0.502762)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.68869, 
    farPlane=10.7351, width=12.3284, height=7.14645, cameraPosition=(0.68351, 
    1.10926, -9.1686), cameraUpVector=(-0.007526, 0.915097, 0.403164), 
    cameraTarget=(3.69426, 0.871091, -2.57715), viewOffsetX=2.55274, 
    viewOffsetY=-0.502355)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.72394, 
    farPlane=10.1876, width=12.3934, height=7.18412, cameraPosition=(4.06255, 
    5.42709, -6.765), cameraUpVector=(-0.0515733, 0.576878, 0.8152), 
    cameraTarget=(4.57296, 1.28452, -0.836501), viewOffsetX=2.56619, 
    viewOffsetY=-0.505003)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.55623, 
    farPlane=10.3811, width=12.0843, height=7.00494, cameraPosition=(5.62172, 
    5.73579, -5.59618), cameraUpVector=(-0.528119, 0.565283, 0.633676), 
    cameraTarget=(4.16932, 1.93043, 0.402), viewOffsetX=2.50219, 
    viewOffsetY=-0.492407)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.47034, 
    farPlane=10.593, width=11.926, height=6.91317, cameraPosition=(6.96076, 
    4.04857, -6.00237), cameraUpVector=(-0.543687, 0.730785, 0.412745), 
    cameraTarget=(4.29341, 1.7846, 0.348067), viewOffsetX=2.46941, 
    viewOffsetY=-0.485956)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.42413, 
    farPlane=10.8984, width=11.8408, height=6.8638, cameraPosition=(8.92154, 
    -0.857255, -5.39054), cameraUpVector=(-0.18514, 0.980907, 0.0595423), 
    cameraTarget=(4.86951, 0.486096, 0.469903), viewOffsetX=2.45177, 
    viewOffsetY=-0.482486)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.70254, 
    farPlane=10.4893, width=12.354, height=7.16126, cameraPosition=(6.99467, 
    1.72213, -7.1399), cameraUpVector=(-0.0121885, 0.836028, 0.548552), 
    cameraTarget=(4.95167, 0.138523, -0.36593), viewOffsetX=2.55802, 
    viewOffsetY=-0.503396)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.65362, 
    farPlane=10.3936, width=12.2638, height=7.10901, cameraPosition=(6.14071, 
    4.29222, -6.54385), cameraUpVector=(-0.0717386, 0.648816, 0.757556), 
    cameraTarget=(4.84184, 0.687036, -0.388859), viewOffsetX=2.53935, 
    viewOffsetY=-0.499722)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.65499, 
    farPlane=10.3922, width=12.2664, height=7.11048, cameraPosition=(5.97375, 
    4.78893, -6.28814), cameraUpVector=(-0.234036, 0.649325, 0.723605), 
    cameraTarget=(4.67488, 1.18375, -0.133151), viewOffsetX=2.53987, 
    viewOffsetY=-0.499825)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.69553, 
    farPlane=10.4523, width=12.3411, height=7.15381, cameraPosition=(6.01705, 
    3.97836, -6.84199), cameraUpVector=(-0.421235, 0.745986, 0.515817), 
    cameraTarget=(4.4058, 1.68477, -0.155314), viewOffsetX=2.55534, 
    viewOffsetY=-0.502869)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.5758, 
    farPlane=10.6605, width=12.1204, height=7.02588, cameraPosition=(7.6275, 
    1.80521, -6.55665), cameraUpVector=(-0.418282, 0.879381, 0.22744), 
    cameraTarget=(4.56925, 1.40184, 0.00480199), viewOffsetX=2.50964, 
    viewOffsetY=-0.493876)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.59553, 
    farPlane=10.8011, width=12.1568, height=7.04696, cameraPosition=(7.92757, 
    -1.34191, -6.50619), cameraUpVector=(-0.15882, 0.98696, 0.0262136), 
    cameraTarget=(4.90787, 0.452466, -0.163484), viewOffsetX=2.51717, 
    viewOffsetY=-0.495358)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.30753, 
    farPlane=10.7424, width=11.626, height=6.73925, cameraPosition=(7.90613, 
    4.10091, -4.96254), cameraUpVector=(-0.490077, 0.739779, 0.461032), 
    cameraTarget=(4.43767, 1.45975, 0.830761), viewOffsetX=2.40726, 
    viewOffsetY=-0.473728)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.66176, 
    farPlane=10.3882, width=7.03576, height=4.07844, viewOffsetX=2.35616, 
    viewOffsetY=-0.761879)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.69033, 
    farPlane=10.3596, width=7.06593, height=4.09592, viewOffsetX=2.8288, 
    viewOffsetY=-0.745454)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.80981, 
    farPlane=10.3617, width=7.19212, height=4.16907, cameraPosition=(8.00833, 
    3.17718, -5.60769), cameraUpVector=(-0.348192, 0.799547, 0.489374), 
    cameraTarget=(4.76129, 1.03993, 0.512538), viewOffsetX=2.87932, 
    viewOffsetY=-0.758767)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.80109, 
    farPlane=10.3705, width=7.18291, height=4.16373, viewOffsetX=3.17575, 
    viewOffsetY=-0.537598)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.96113, 
    farPlane=10.2104, width=4.76756, height=2.76363, viewOffsetX=3.0119, 
    viewOffsetY=-0.433565)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].setValues(displayedObject=None)

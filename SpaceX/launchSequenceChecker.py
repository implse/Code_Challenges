# https://app.codesignal.com/company-challenges/spacex/

def launchSequenceChecker(systemNames, stepNumbers):
    sequence = dict()
    for i in range(len(systemNames)):
        systemId = systemNames[i]
        stepNumber = stepNumbers[i]
        if systemId not in sequence:
            sequence[systemId] = [stepNumber]
        elif stepNumber <= sequence[systemId][-1]:
            return False
        else:
            sequence[systemId].append(stepNumber)
    return True

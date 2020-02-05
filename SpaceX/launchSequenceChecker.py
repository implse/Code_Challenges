# https://app.codesignal.com/company-challenges/spacex/

def launchSequenceChecker(systemNames, stepNumbers):
    sequence = dict()
    for systemId, stepNumber in zip(systemNames, stepNumbers):
        if systemId not in sequence:
            sequence[systemId] = [stepNumber]
        elif stepNumber <= sequence[systemId][-1]:
            return False
        else:
            sequence[systemId].append(stepNumber)
    return True

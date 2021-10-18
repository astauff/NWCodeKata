# function to calculate the total amount to be charged
# takes in the strings sT (start time), eT (end time) and bT (bedtime) as input
# prints the total dollar (USD) to the screen for the user

def calc_charge(sT, eT, bT):
    correct_in = check_input(sT, eT, bT)
    # if input passes initial tests calculate charge
    if correct_in:
        print("============================================")
        sb_rate = 12    # hourly rate from start to bedtime $12/hr
        bm_rate = 8     # hourly rate from bedtime to midnight $8/hr
        me_rate = 16    # hourly rate from midnight to end $16/hr

        # breaking the time into the number value and am/pm

        # the number portion of the start time sT_num
        if (len(sT) == 3):
            sT_num = int(sT[0])

        if (len(sT) == 4):
            sT_num = int(sT[0:2])
            # checking that the time is a valid time (ex. start time not 25pm)
            if (sT_num > 12):
                raise ValueError("Error: Invalid Time")

        # the number portion of the end time eT_num and am/pm eT_ap
        eT_ap = eT[-2:]
        if (len(eT) == 3):
            eT_num = int(eT[0])

        if (len(eT) == 4):
            eT_num = int(eT[0:2])
            # checking that the time is a valid time (ex. end time not 25pm)
            if (eT_num > 12):
                raise ValueError("Error: Invalid Time")

        # the number portion of bedtime bT_num
        if (len(bT) == 3):
            bT_num = int(bT[0])

        if (len(bT) == 4):
            bT_num = int(bT[0:2])

        # checking that bedtime is a valid time (ex. bedtime not 88pm)
        if (12 < bT_num or bT_num < 5):
            raise ValueError("Error: Invalid Time")

        # checking for negative input
        if (sT_num < 0):
            raise ValueError("Error: Invalid Time")
        if (eT_num < 0):
            raise ValueError("Error: Invalid Time")
        if (bT_num < 0):
            raise ValueError("Error: Invalid Time")

        # calculating hours for each to be applied to each hourly rate

        # calculating hours from start to bedtime pre_bedT
        pre_bedT = bT_num - sT_num

        # calculating hours past midnight post_midT
        if(eT_ap == 'am' and eT_num != 12):
            post_midT = eT_num
        else:
            post_midT = 0

        # calculating total charge

        # calculating charge from start to bedtime
        pre_bed_hours = pre_bedT * sb_rate

        # calculating charge for midnight to end
        if(post_midT > 0):
            post_mid_hours = post_midT * me_rate
        else:
            post_mid_hours = 0

        # calculating pre-midnight hours (can be bedtime to end if end time is before midnight)
        if(eT_ap == 'pm'):
            b2mid_hours = (eT_num - bT_num) * bm_rate

        # if end time is midnight
        if(eT == '12am'):
            b2mid_hours = (12 - bT_num) * bm_rate

        if (post_midT > 0):
            b2mid_hours = (12 - bT_num) * bm_rate

        total = pre_bed_hours + b2mid_hours + post_mid_hours

        print("Charge before bedtime: $" + str(pre_bed_hours))
        print("Charge from bedtime to midnight: $" + str(b2mid_hours))
        print("Charge for after midnight: " + str(post_mid_hours))
        print("Total charge: $" + str(total))

        return total


# the check_input function checks that the input is entered in a way that makes sense (bedtime falls between start and end
# and that the end time does not occur before the start) while also conforming to the rules given
# takes in the strings startT (start time), endT (end time) and bedT (bedtime) as input

def check_input(startT, endT, bedT):
    # checking that input is a string
    if (type(startT) != str):
        raise TypeError("Start time must be a string")

    if (type(endT) != str):
        raise TypeError("End time must be a string")

    if (type(bedT) != str):
        raise TypeError("Bed time must be a string")

    # checking that input is no longer than 4 characters or less than 3
    if (3 < len(startT) > 4):
        raise ValueError("Invalid time format")

    if (3 < len(endT) > 4):
        raise ValueError("Invalid time format")

    if (3 < len(bedT) > 4):
        raise ValueError("Invalid time format")

    # checking for a start time
    if (startT == ''):
        raise ValueError("Error: no start time given")

    # checking for an end time
    if (endT == ''):
        raise ValueError("Error: no end time given")

    # checking for a bedtime
    if (bedT == ''):
        raise ValueError("Error: no bedtime given")

    # checking that start time is 5pm or later
    if (len(startT) == 3):
        if (int(startT[0]) < 5 and startT[-2:] == 'pm'):
            raise ValueError("Error: cannot start before 5pm")

    # checking that end time is 4am or earlier
    if (int(endT[0]) > 4 and endT[-2:] == 'am'):
        raise ValueError("Error: cannot end before 4am")

    # checking that bedtime occurs at a reasonable time
    # this will take multiple tests

    # checking that bedtime occurs after start time
    # if bedtime is single digit (ex. 8pm)
    if (len(bedT) == 3 and len(startT) == 3):
        if (int(bedT[0]) < int(startT[0]) and bedT[-2:] == startT[-2:]):
            raise ValueError("Error: bedtime cannot occur before start time")

    # if bedtime is double digit (ex. 10pm)
    if (len(bedT) == 4 and len(startT) == 4):
        if (int(bedT[0:2]) < int(startT[0:2]) and bedT[-2:] == startT[-2:]):
            raise ValueError("Error: bedtime cannot occur before start time")

    # checking that bedtime is not noon
    if (bedT[0:2] == '12' and bedT[-2:] == 'pm'):
        raise ValueError("Error: bedtime cannot occur before start time")

    # checking that bedtime occurs before end time
    # if bedtime is single digit (ex. 8pm)
    if (len(bedT) == 3 and len(endT) == 3):
        if (int(bedT[0]) > int(endT[0]) and bedT[-2:] == endT[-2:]):
            raise ValueError("Error: bedtime cannot occur after end time")

    # if bedtime is double digit (ex. 10pm)
    if (len(bedT) == 4 and len(endT) == 4):
        if (int(bedT[0:2]) > int(endT[0:2]) and bedT[-2:] == endT[-2:]):
            raise ValueError("Error: bedtime cannot occur after end time")

    # checking that bedtime occurs before midnight
    if (len(bedT) == 3):
        if(int(bedT[0]) < 4 and bedT[-2:] == 'am'):
            raise ValueError("Error: bedtime must occur before midnight")

    if (len(bedT) == 4):
        if(int(bedT[0:2]) == 12 and bedT[-2:] == 'am'):
            raise ValueError("Error: bedtime must occur before midnight")

    # if no errors appear in the input, return true to allow the calc function to operate
    return True

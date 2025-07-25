    # try:
    #     mobileNumber = int(mobileNumber)
    # except ValueError:
    #     return jsonify({'error': 'Invalid mobile number'}), 400

    # if(mobileNumber == 9999999999):
    #     result = {
    #     'creditLimit': 1500000,
    #     'interestRate': 12,
    #     'tenure': 4,
    #     'status': 'partial'
    # }
    # elif(mobileNumber == 1111111111):
    #     result = {
    #     'creditLimit': 2500000,
    #     'interestRate': 8,
    #     'tenure': 6,
    #     'status': 'partial'
    # }
    # else:
    #     result = {
    #     'creditLimit': 0,
    #     'interestRate': None,
    #     'tenure': 0,
    #     'status': 'rejected'
    #     }


    # if annual_income < 150000:
    #     result = {'status': 'rejected', 'creditLimit': 0, 'interestRate': None, 'tenure': 0}
    # elif annual_income <= 300000:
    #     result = {'status': 'partial', 'creditLimit': 500000, 'interestRate': 18, 'tenure': 2}
    # elif annual_income <= 600000:
    #     result = {'status': 'partial', 'creditLimit': 1000000, 'interestRate': 15, 'tenure': 3}
    # elif annual_income <= 1000000:
    #     result = {'status': 'partial', 'creditLimit': 1500000, 'interestRate': 12, 'tenure': 4}
    # elif annual_income <= 1500000:
    #     result = {'status': 'partial', 'creditLimit': 2000000, 'interestRate': 10, 'tenure': 5}
    # else:
    #     result = {'status': 'partial', 'creditLimit': 2500000, 'interestRate': 8, 'tenure': 6}
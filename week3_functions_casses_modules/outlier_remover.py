def no_outlier_mean(num_lst):
    new_list = num_lst.copy()

    try:
        for instance in range(len(num_lst)):
            new_list[instance] = float(new_list[instance])
            
        q1 = (len(new_list)+1)/4

        q3 = (3*(len(new_list)+1))/4

        iqr = q3-q1

        iqr_lower = q1-(1.5*iqr)

        iqr_upper = q3+(1.5*iqr)

        outlier_free_lst = [num for num in new_list if num >= iqr_lower and num <= iqr_upper]

        return sum(outlier_free_lst)/len(outlier_free_lst)

    except:

        return "Your list needs to contain only numbers!"

lst = [1, 50]

print(no_outlier_mean(lst))

print(lst)



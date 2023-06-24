def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    # Input the number of males
    num_males = int(input("Enter the number of males: "))

    # Input the number of females
    num_females = int(input("Enter the number of females: "))

    # Calculate the total number of students
    total_students = num_males + num_females

    # Calculate the percentage of males
    m_perc = (num_males / total_students) * 100

    # Calculate the percentage of females
    f_perc = (num_females / total_students) * 100

    # Display the percentages of males and females
    print("m_perc: {:.2f}%".format(m_perc))
    print("f_perc: {:.2f}%".format(f_perc))

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()

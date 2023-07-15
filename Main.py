from Program import Program


#Creates parseTree and parses, pretty prints, and then executes the Core program
def main():
    parseTree = Program()
    parseTree.parse()

    print("\n===== Start of Pretty Printing =====")
    parseTree.pprint()
    print("===== End of Pretty Printing =====\n")
    print("===== Start of Execution =====")
    parseTree.execute()
    print("===== End of Execution =====\n")

if __name__ == "__main__":
    main()
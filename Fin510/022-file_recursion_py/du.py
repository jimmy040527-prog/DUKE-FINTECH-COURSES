import sys
import os


def du(file):
    """
    From the given file (this may be a directory or a file),
    produce output similar to the linux command: du -ac
    However rather than the number of blocks, the size in bytes of the files and directories
    should be printed.  For directories, the size should include the directory file itself 
    plus the size of the files of all of the files contained within it.

    returns: size of the given file.
             for a regular file, this is just the file itself
             for a directory, this includes the directory file size and all of the children sizes
    """
    if not os.path.isdir(file):
        file_size = os.path.getsize(file)
    else:
        file_size = os.path.getsize(file)
        all_file = os.listdir(file)
        for child in all_file:
            real_child = os.path.join(file, child)
            file_size += du(real_child)
    print('{}\t{}'.format(file_size, file))
    return file_size


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python du.py directory")
        sys.exit(2)
    total_size = du(sys.argv[1])
    # print the total line
    print('{}\t{}'.format(total_size, 'total'))

# Retviews final interview
Hello and congratulations for making it this far!

For this stage of the process, you will have to build a functional spider (a script that will take the data from a certain website)

**Requirements:**
- conda (https://conda.io/projects/conda/en/latest/user-guide/install/index.html) - used to install scrapy
- git (https://git-scm.com/downloads) - used to clone the project
- pycharm (https://www.jetbrains.com/pycharm/) - the IDE you will write code (you can use any other editor you want, but we recommand pycharm)

Be aware to include git/conda to ENV PATH

After all requirements are done, you will have to install scrapy:

Write this command into shell (cmd/git/powershell etc) `conda install scrapy`

Clone the project into your desired directory:

Write this command into shell (cmd/git/powershell etc)

`git clone https://github.com/vladciobotearv/retviews-final-interview.git`

If you want to see if everything is set up properly, use this command:

`scrapy crawl marisfrolg_cn`

If everything is running properly, you will get a bunch of logs that tell you that links are being crawled and scraped.

You will receive the file to work on during the interview, it will need to be pasted into `interview(-main)/interview/spiders`.

## All set! Lets go!

Open the project on pycharm (the `interview(-main)/interview` folder) and start coding.

## Helpful tools

Run the script:  `scrapy crawl myspider`

Additional settings:

- `-s CLOSESPIDER_ITEMCOUNT=x` will stop when x items are taken;
- `-o output_file` will print the data scraped to output_file (extension must be `json`);
- in `spiders/` you will find an example already made, called `marisfrolg.py`. You can look into it a bit, but it's not mandatory as all you need to know will be communicated to you during the interview.


### Good luck!

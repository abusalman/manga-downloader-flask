import json
import subprocess
from jinja2 import Environment, FileSystemLoader


def run_crawler(crawler_name, **kwargs):
    """
    runs the crawler of crawler_name with the given kwargs
    returns a list of dicts of data
    """
    outfile = "results.json"
    #truncate the output file
    open(outfile, 'w').close()

    #handle arguments if any are given
    args = []
    if kwargs:
        args = ["-a"]
        for k, v in kwargs.iteritems():
            args.append("%s=%s" % (k, v))

    cmd = ["scrapy", "crawl", crawler_name, "--nolog"] + args + \
          ["-o", outfile, "-t", "jsonlines"]

    # block until completion
    subprocess.call(cmd)

    return [json.loads(x) for x in open(outfile)]


def extract_link(link_node):
    """returns (text, href) of the given link node"""
    return (link_node.xpath('text()').extract()[0],
            link_node.xpath('@href').extract()[0])


def jinja_template(template_path, **kwargs):
    """
    inits jinja and returns a template object from the given path
    kwargs is a dict of globals to add to the templates
    """
    jinja2 = Environment(loader=FileSystemLoader("templates"))
    #add the globals to jinja
    jinja2.globals.update(**kwargs)
    return jinja2.get_template(template_path)

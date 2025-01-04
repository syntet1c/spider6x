import argparse

def arguments_f():
    args = argparse.ArgumentParser()
    args.add_argument("-u", "--url", dest="url")
    args.add_argument("-e", "--element", dest="element")
    args.add_argument("-a", "--attribute", dest="attribute")
    arguments = args.parse_args()

    url = arguments.url
    element = arguments.element
    attribute = arguments.attribute

    if attribute:
        return {"url": url, "element": element, "attribute": attribute}

    return {"url": url, "element": element}
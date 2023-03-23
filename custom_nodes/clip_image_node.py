class LatentCombine:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "latent1": ("LATENT",),
                "latent2": ("LATENT",),
            },
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "combine"

    # OUTPUT_NODE = False

    CATEGORY = "latent"

    def combine(self, latent1, latent2):
        latent1 = latent1['samples']
        latent2 = latent2['samples']
        print('latent shapes:', latent1.shape, latent2.shape)
        result = (latent1 + latent2) / 2

        return ({"samples": result},)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "LatentCombine": LatentCombine
}

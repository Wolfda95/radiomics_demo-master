import SimpleITK as sitk
import radiomics
from radiomics import glcm, glrlm, glszm, shape


def calc_radiomics(path_img, path_mask):

    img = sitk.ReadImage(path_img)
    mask = sitk.ReadImage(path_mask)
    settings = {'binWidth': 25,
                'interpolator': sitk.sitkBSpline,
                'resampledPixelSpacing': None}

    firstOrderFeatures = radiomics.firstorder.RadiomicsFirstOrder(img, mask, **settings)

    firstOrderFeatures.enableAllFeatures()

    results_First_order = firstOrderFeatures.execute()

    shapeFeatures = shape.RadiomicsShape(img, mask, **settings)
    shapeFeatures.enableAllFeatures()

    results_shape = shapeFeatures.execute()
    glcmFeatures = glcm.RadiomicsGLCM(img, mask, **settings)
    glcmFeatures.enableAllFeatures()

    results_glcm = glcmFeatures.execute()

    glrlmFeatures = glrlm.RadiomicsGLRLM(img, mask, **settings)
    glrlmFeatures.enableAllFeatures()

    results_glrlm = glrlmFeatures.execute()

    glszmFeatures = glszm.RadiomicsGLSZM(img, mask, **settings)
    glszmFeatures.enableAllFeatures()

    results_glszm = glszmFeatures.execute()

    return results_First_order, results_shape, results_glcm, results_glrlm, results_glszm

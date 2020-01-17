%global packname  RJafroc
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Analyzing Diagnostic Observer Performance Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-bbmle 
Requires:         R-CRAN-binom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-utils 

%description
Implements software for assessing medical imaging systems, radiologists or
computer aided detection algorithms. Models of observer performance are
implemented, including the binormal model (BM), the contaminated binormal
model (CBM), the correlated contaminated binormal model (CORCBM), and the
radiological search model (RSM). The software and applications are
described in a book - Chakraborty DP: Observer Performance Methods for
Diagnostic Imaging - Foundations, Modeling, and Applications with R-Based
Examples. Taylor-Francis LLC; 2017 - and its vignettes
<https://dpc10ster.github.io/RJafroc/>. Observer performance data
collection paradigms are the receiver operating characteristic (ROC) and
its location specific extensions, primarily free-response ROC (FROC) and
the location ROC (LROC). ROC data consists of single ratings per images. A
rating is the perceived confidence level that the image is that of a
diseased patient. FROC data consists of a variable number (including zero)
of mark-rating pairs per image, where a mark is the location of a
clinically reportable suspicious region and the rating is the
corresponding confidence level that it is a real lesion. LROC data
consists of a rating and a forced localization of the most suspicious
region on every image. RJafroc supersedes the Windows version of JAFROC
software V4.2.1, <http://www.devchakraborty.com>:. Package functions are
organized as follows. Data file related function names are preceded by Df,
curve fitting functions by Fit, included data sets by dataset, plotting
functions by Plot, significance testing functions by St, sample size
related functions by Ss, data simulation functions by Simulate and utility
functions by Util. Implemented are figures of merit (FOMs) for quantifying
performance, functions for visualizing empirical operating
characteristics: e.g., ROC, FROC, alternative FROC (AFROC) and weighted
AFROC (wAFROC) curves. Four maximum likelihood curve-fitting algorithms
are implemented: the binormal model (BM), the contaminated binormal model
(CBM), the correlated contaminated binormal model (CORCBM) and the
radiological search model (RSM). Unlike the binormal model, CBM, CORCBM
and RSM predict "proper" ROC curves that do not cross the chance diagonal.
RSM fitting additionally yields measures of search and
lesion-classification performances. Search performance is the ability to
find lesions while avoiding finding non-lesions. Lesion-classification
performance is the ability to correctly classify found lesions from found
non-lesions. For fully crossed study designs significance testing of
reader-averaged FOM differences between modalities is implemented via both
Dorfman-Berbaum-Metz and the Obuchowski-Rockette methods, including
Hillis' extensions. Also implemented are single treatment analyses, which
allow comparison of performance of a group of radiologists to a specified
value, or comparison to CAD to a group of radiologists interpreting the
same cases. Crossed-modality analysis is implemented wherein there are two
crossed treatment factors and the desire is to determined performance in
each treatment factor averaged over all levels of the other factor. Sample
size estimation tools are provided for ROC and FROC studies; these use
estimates of the relevant variances from a pilot study to predict required
numbers of readers and cases in a pivotal study to achieve a desired
power. Utility and data file manipulation functions allow data to be read
in any of the currently used input formats, including Excel, and the
results of the analysis can be viewed in text or Excel output files. The
methods are illustrated with several included datasets from the author's
international collaborations. This version corrects a few bugs noticed by
users and extends the Excel file input format for greater flexibility in
handling non-crossed datasets and the sample size routines have been
rewritten for ease of use.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ANALYZED
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/MRMCRuns
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

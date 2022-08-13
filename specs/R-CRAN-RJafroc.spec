%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RJafroc
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Artificial Intelligence Systems and Observer Performance

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
BuildRequires:    R-CRAN-readxl 
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
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-utils 

%description
Analyzing the performance of artificial intelligence (AI)
systems/algorithms characterized by a 'search-and-report' strategy.
Historically observer performance has dealt with measuring radiologists'
performances in search tasks, e.g., searching for lesions in medical
images and reporting them, but the implicit location information has been
ignored. The implemented methods apply to analyzing the absolute and
relative performances of AI systems, comparing AI performance to a group
of human readers or optimizing the reporting threshold of an AI system. In
addition to performing historical receiver operating receiver operating
characteristic (ROC) analysis (localization information ignored), the
software also performs free-response receiver operating characteristic
(FROC) analysis, where lesion localization information is used. A book
using the software has been published: Chakraborty DP: Observer
Performance Methods for Diagnostic Imaging - Foundations, Modeling, and
Applications with R-Based Examples, Taylor-Francis LLC; 2017:
<https://www.routledge.com/Observer-Performance-Methods-for-Diagnostic-Imaging-Foundations-Modeling/Chakraborty/p/book/9781482214840>.
Online updates to this book, which use the software, are at
<https://dpc10ster.github.io/RJafrocQuickStart/>,
<https://dpc10ster.github.io/RJafrocRocBook/> and at
<https://dpc10ster.github.io/RJafrocFrocBook/>. Supported data collection
paradigms are the ROC, FROC and the location ROC (LROC). ROC data consists
of single ratings per images, where a rating is the perceived confidence
level that the image is that of a diseased patient. An ROC curve is a plot
of true positive fraction vs. false positive fraction. FROC data consists
of a variable number (zero or more) of mark-rating pairs per image, where
a mark is the location of a reported suspicious region and the rating is
the confidence level that it is a real lesion. LROC data consists of a
rating and a location of the most suspicious region, for every image. Four
models of observer performance, and curve-fitting software, are
implemented: the binormal model (BM), the contaminated binormal model
(CBM), the correlated contaminated binormal model (CORCBM), and the
radiological search model (RSM). Unlike the binormal model, CBM, CORCBM
and RSM predict 'proper' ROC curves that do not inappropriately cross the
chance diagonal. Additionally, RSM parameters are related to search
performance (not measured in conventional ROC analysis) and classification
performance. Search performance refers to finding lesions, i.e., true
positives, while simultaneously not finding false positive locations.
Classification performance measures the ability to distinguish between
true and false positive locations. Knowing these separate performances
allows principled optimization of reader or AI system performance. This
package supersedes Windows JAFROC (jackknife alternative FROC) software
V4.2.1, <https://github.com/dpc10ster/WindowsJafroc>. Package functions
are organized as follows. Data file related function names are preceded by
'Df', curve fitting functions by 'Fit', included data sets by 'dataset',
plotting functions by 'Plot', significance testing functions by 'St',
sample size related functions by 'Ss', data simulation functions by
'Simulate' and utility functions by 'Util'. Implemented are figures of
merit (FOMs) for quantifying performance and functions for visualizing
empirical or fitted operating characteristics: e.g., ROC, FROC,
alternative FROC (AFROC) and weighted AFROC (wAFROC) curves. For fully
crossed study designs significance testing of reader-averaged FOM
differences between modalities is implemented via either
Dorfman-Berbaum-Metz or the Obuchowski-Rockette methods. Also implemented
is single treatment analysis, which allows comparison of performance of a
group of radiologists to a specified value, or comparison of AI to a group
of radiologists interpreting the same cases. Crossed-modality analysis is
implemented wherein there are two crossed treatment factors and the aim is
to determined performance in each treatment factor averaged over all
levels of the second factor. Sample size estimation tools are provided for
ROC and FROC studies; these use estimates of the relevant variances from a
pilot study to predict required numbers of readers and cases in a pivotal
study to achieve the desired power. Utility and data file manipulation
functions allow data to be read in any of the currently used input
formats, including Excel, and the results of the analysis can be viewed in
text or Excel output files. The methods are illustrated with several
included datasets from the author's collaborations. This update includes
improvements to the code, some as a result of user-reported bugs and new
feature requests, and others discovered during ongoing testing and code
simplification.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

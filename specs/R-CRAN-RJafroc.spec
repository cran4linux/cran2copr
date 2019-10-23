%global packname  RJafroc
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
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
Tools for quantitative assessment of medical imaging systems, radiologists
or computer aided detection ('CAD') algorithms. Implements methods
described in the book: 'Chakraborty' (2017) <ISBN:978-1482214840>. Data
collection paradigms include receiver operating characteristic ('ROC') and
a location specific extension, namely free-response 'ROC' ('FROC'). 'ROC'
data consists of a single rating per image, where the rating is the
perceived confidence level the image is of a diseased patient. 'FROC' data
consists of a variable number (including zero) of mark-rating pairs per
image, where a mark is the location of a clinically relevant suspicious
region and the rating is the corresponding confidence level that it is a
true lesion. The name 'RJafroc' is derived from it being an enhanced R
version of original Windows 'JAFROC' <http://www.devchakraborty.com>.
Implemented are a number of figures of merit quantifying performance,
functions for visualizing operating characteristics and three ROC ratings
data curve-fitting algorithms: the 'binormal' model ('BM'), the
contaminated 'binormal' model ('CBM') and the 'radiological' search model
('RSM') 'Chakraborty' (2006) <{doi:10.1088/0031-9155/51/14/012}> . Also
implemented is maximum likelihood fitting of paired ROC data, utilizing
the correlated 'CBM' model ('CORCBM') model. Unlike the 'BM', which
predicts 'improper' ROC curves, 'CBM', 'CORCBM' and the 'RSM' predict
proper ROC curves that do not cross the chance diagonal. 'RSM' fitting
yields measures of search and lesion-classification performances, in
addition to the usual case-classification performance measured by the area
under the 'ROC' curve. Search performance is the ability to find lesions
while avoiding finding non-lesions. Lesion-classification performance is
the ability to discriminate between found lesions and non-lesions. A
number of significance testing algorithms are implement. For fully-crossed
factorial study designs, termed multiple-reader multiple-case,
significance testing of reader-averaged figure-of-merit differences
between 'modalities' is implemented using either 'pseudovalue'-based or
figure of merit-based methods. Single treatment analysis allows comparison
of performance of a group of radiologists to a specified value, or
comparison of 'CAD' performance to a group of radiologists interpreting
the same cases. Sample size estimation tools are provided for 'ROC' and
'FROC' studies that allow estimation of relevant variances from a pilot
study, in order to predict required numbers of readers and cases in a
pivotal study. Utility and data file manipulation functions allow data to
be read in any of the currently used input formats, including Excel, and
the results of the analysis can be viewed in text or Excel output files.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/MRMCRuns
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

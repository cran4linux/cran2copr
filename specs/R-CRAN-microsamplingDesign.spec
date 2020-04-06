%global packname  microsamplingDesign
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Finding Optimal Microsampling Designs for Non-CompartmentalPharmacokinetic Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-matrixcalc 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Find optimal microsampling designs for non-compartmental pharacokinetic
analysis using a general simulation methodology: Algorithm III of Barnett,
Helen, Helena Geys, Tom Jacobs, and Thomas Jaki. (2017) "Optimal Designs
for Non-Compartmental Analysis of Pharmacokinetic Studies. (currently
unpublished)" This methodology consist of (1) specifying a pharmacokinetic
model including variability among animals; (2) generating possible
sampling times; (3) evaluating performance of each time point choice on
simulated data; (4) generating possible schemes given a time point choice
and additional constraints and finally (5) evaluating scheme performance
on simulated data. The default settings differ from the article of Barnett
and others, in the default pharmacokinetic model used and the
parameterization of variability among animals. Details can be found in the
package vignette. A 'shiny' web application is included, which guides
users from model parametrization to optimal microsampling scheme.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/apps
%{rlibdir}/%{packname}/dataForTesting
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/extData
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

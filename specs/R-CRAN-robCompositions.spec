%global packname  robCompositions
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          3%{?dist}
Summary:          Compositional Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-sROC 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-VIM 
BuildRequires:    R-CRAN-zCompositions 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-car 
Requires:         R-CRAN-cvTools 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-rrcov 
Requires:         R-cluster 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-kernlab 
Requires:         R-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-sROC 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-VIM 
Requires:         R-CRAN-zCompositions 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-Rcpp 

%description
Methods for analysis of compositional data including robust methods
(<doi:10.1007/978-3-319-96422-5>), imputation of missing values
(<doi:10.1016/j.csda.2009.11.023>), methods to replace rounded zeros
(<doi:10.1080/02664763.2017.1410524>,
<doi:10.1016/j.chemolab.2016.04.011>, <doi:10.1016/j.csda.2012.02.012>),
count zeros (<doi:10.1177/1471082X14535524>), methods to deal with
essential zeros (<doi:10.1080/02664763.2016.1182135>), (robust) outlier
detection for compositional data, (robust) principal component analysis
for compositional data, (robust) factor analysis for compositional data,
(robust) discriminant analysis for compositional data (Fisher rule),
robust regression with compositional predictors, functional data analysis
and p-splines (<doi:10.1016/j.csda.2015.07.007>), contingency
(<doi:10.1080/03610926.2013.824980>) and compositional tables
(<doi:10.1111/sjos.12326>, <doi:10.1111/sjos.12223>,
<doi:10.1080/02664763.2013.856871>) and (robust) Anderson-Darling
normality tests for compositional data as well as popular log-ratio
transformations (addLR, cenLR, isomLR, and their inverse transformations).
In addition, visualisation and diagnostic tools are implemented as well as
high and low-level plot functions for the ternary diagram.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

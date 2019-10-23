%global packname  robCompositions
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Compositional Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-sROC 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-VIM 
BuildRequires:    R-CRAN-zCompositions 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-car 
Requires:         R-CRAN-cvTools 
Requires:         R-CRAN-rrcov 
Requires:         R-cluster 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-kernlab 
Requires:         R-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-sROC 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-VIM 
Requires:         R-CRAN-zCompositions 

%description
Methods for analysis of compositional data including robust methods,
imputation, methods to replace rounded zeros, (robust) outlier detection
for compositional data, (robust) principal component analysis for
compositional data, (robust) factor analysis for compositional data,
(robust) discriminant analysis for compositional data (Fisher rule),
robust regression with compositional predictors and (robust)
Anderson-Darling normality tests for compositional data as well as popular
log-ratio transformations (addLR, cenLR, isomLR, and their inverse
transformations). In addition, visualisation and diagnostic tools are
implemented as well as high and low-level plot functions for the ternary
diagram.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

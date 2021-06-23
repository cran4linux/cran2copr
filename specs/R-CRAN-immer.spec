%global __brp_check_rpaths %{nil}
%global packname  immer
%global packver   1.1-35
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.35
Release:          3%{?dist}%{?buildtag}
Summary:          Item Response Models for Multiple Ratings

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-CDM >= 6.0.101
BuildRequires:    R-CRAN-sirt >= 2.4.9
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-psychotools 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TAM 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CDM >= 6.0.101
Requires:         R-CRAN-sirt >= 2.4.9
Requires:         R-CRAN-coda 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-psychotools 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-TAM 

%description
Implements some item response models for multiple ratings, including the
hierarchical rater model, conditional maximum likelihood estimation of
linear logistic partial credit model and a wrapper function to the
commercial FACETS program. See Robitzsch and Steinfeld (2018) for a
description of the functionality of the package. See Wang, Su & Qiu (2014;
<doi:10.1111/jedm.12045>) for an overview of modeling alternatives.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

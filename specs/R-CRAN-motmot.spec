%global __brp_check_rpaths %{nil}
%global packname  motmot
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Models of Trait Macroevolution on Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-ape >= 3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-caper 
BuildRequires:    R-methods 
Requires:         R-CRAN-ape >= 3.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-caper 
Requires:         R-methods 

%description
Functions for fitting models of trait evolution on phylogenies for
continuous traits. The majority of functions described in Thomas and
Freckleton (2012) <doi:10.1111/j.2041-210X.2011.00132.x> and include
functions that allow for tests of variation in the rates of trait
evolution.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

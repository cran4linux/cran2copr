%global packname  vines
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}
Summary:          Multivariate Dependence Modeling with Vines

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-ADGofTest 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-TSP 
Requires:         R-methods 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-ADGofTest 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-TSP 

%description
Implementation of the vine graphical model for building high-dimensional
probability distributions as a factorization of bivariate copulas and
marginal density functions. This package provides S4 classes for vines
(C-vines and D-vines) and methods for inference, goodness-of-fit tests,
density/distribution function evaluation, and simulation.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

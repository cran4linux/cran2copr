%global packname  ref.ICAR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Objective Bayes Intrinsic Conditional Autoregressive Model forAreal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-MCMCglmm 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-graphics 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-MCMCglmm 
Requires:         R-CRAN-Rdpack 
Requires:         R-graphics 

%description
Implements an objective Bayes intrinsic conditional autoregressive prior.
This model provides an objective Bayesian approach for modeling spatially
correlated areal data using an intrinsic conditional autoregressive prior
on a vector of spatial random effects.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX

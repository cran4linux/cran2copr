%global packname  bbmle
%global packver   1.0.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.22
Release:          1%{?dist}
Summary:          Tools for General Maximum Likelihood Estimation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats4 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bdsmatrix 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats4 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-bdsmatrix 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 

%description
Methods and functions for fitting maximum likelihood models in R.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/vignetteData
%{rlibdir}/%{packname}/INDEX

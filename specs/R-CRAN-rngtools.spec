%global packname  rngtools
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}
Summary:          Utility Functions for Working with Random Number Generators

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-digest 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-parallel 

%description
Provides a set of functions for working with Random Number Generators
(RNGs). In particular, a generic S4 framework is defined for
getting/setting the current RNG, or RNG data that are embedded into
objects for reproducibility. Notably, convenient default methods greatly
facilitate the way current RNG settings can be changed.

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
%{rlibdir}/%{packname}/INDEX

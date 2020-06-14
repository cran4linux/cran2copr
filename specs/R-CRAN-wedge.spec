%global packname  wedge
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          The Exterior Calculus

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-spray >= 1.0.7
BuildRequires:    R-CRAN-permutations >= 1.0.4
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
Requires:         R-CRAN-spray >= 1.0.7
Requires:         R-CRAN-permutations >= 1.0.4
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 

%description
Provides functionality for working with differentials, k-forms, wedge
products, Stokes's theorem, and related concepts from the exterior
calculus.  The canonical reference would be: M. Spivak (1965,
ISBN:0-8053-9021-9). "Calculus on Manifolds", Benjamin Cummings.

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
%doc %{rlibdir}/%{packname}/examples.R
%doc %{rlibdir}/%{packname}/try.R
%{rlibdir}/%{packname}/INDEX

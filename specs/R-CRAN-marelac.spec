%global packname  marelac
%global packver   2.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.10
Release:          3%{?dist}
Summary:          Tools for Aquatic Sciences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-seacarb 
Requires:         R-CRAN-shape 
Requires:         R-stats 
Requires:         R-CRAN-seacarb 

%description
Datasets, constants, conversion factors, and utilities for 'MArine',
'Riverine', 'Estuarine', 'LAcustrine' and 'Coastal' science. The package
contains among others: (1) chemical and physical constants and datasets,
e.g. atomic weights, gas constants, the earths bathymetry; (2) conversion
factors (e.g. gram to mol to liter, barometric units, temperature,
salinity); (3) physical functions, e.g. to estimate concentrations of
conservative substances, gas transfer and diffusion coefficients, the
Coriolis force and gravity; (4) thermophysical properties of the seawater,
as from the UNESCO polynomial or from the more recent derivation based on
a Gibbs function.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

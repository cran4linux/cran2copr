%global packname  celestial
%global packver   1.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.6
Release:          3%{?dist}
Summary:          Collection of Common Astronomical Conversion Routines andFunctions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-NISTunits 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-NISTunits 
Requires:         R-CRAN-pracma 

%description
Contains a number of common astronomy conversion routines, particularly
the HMS and degrees schemes, which can be fiddly to convert between on
mass due to the textural nature of the former. It allows users to
coordinate match datasets quickly. It also contains functions for various
cosmological calculations.

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
%{rlibdir}/%{packname}/INDEX

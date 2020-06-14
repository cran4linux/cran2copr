%global packname  angstroms
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Tools for 'ROMS' the Regional Ocean Modeling System

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-proj4 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spbabel 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-proj4 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spbabel 

%description
Helper functions for working with Regional Ocean Modeling System 'ROMS'
output. See <https://www.myroms.org/> for more information about 'ROMS'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/roms-mapping.rmd
%{rlibdir}/%{packname}/INDEX

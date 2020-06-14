%global packname  geotech
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Geotechnical Engineering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
A compilation of functions for performing calculations and creating plots
that commonly arise in geotechnical engineering and soil mechanics. The
types of calculations that are currently included are: (1) phase diagrams
and index parameters, (2) grain-size distributions, (3) plasticity, (4)
soil classification, (5) compaction, (6) groundwater, (7) subsurface
stresses (geostatic and induced), (8) Mohr circle analyses, (9)
consolidation settlement and rate, (10) shear strength, (11) bearing
capacity, (12) lateral earth pressures, (13) slope stability, and (14)
subsurface explorations. Geotechnical engineering students, educators,
researchers, and practitioners will find this package useful.

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

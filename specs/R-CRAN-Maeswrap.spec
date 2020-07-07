%global packname  Maeswrap
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          3%{?dist}
Summary:          Wrapper Functions for MAESTRA/MAESPA

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
Requires:         R-CRAN-rgl 
Requires:         R-lattice 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-stringr 
Requires:         R-tools 

%description
A bundle of functions for modifying MAESTRA/MAESPA input files,reading
output files, and visualizing the stand in 3D. Handy for running
sensitivity analyses, scenario analyses, etc.

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
%{rlibdir}/%{packname}/INDEX

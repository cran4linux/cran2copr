%global packname  LSDinterface
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Reading LSD Results (.res) Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-abind 
Requires:         R-parallel 

%description
Interfaces R with LSD. Reads object-oriented data in results files (.res)
produced by LSD and creates appropriate multi-dimensional arrays in R.
Supports multiple core parallelization of multi-file data reading for
increased performance. Also provides functions to extract basic
information and statistics from data files. LSD (Laboratory for Simulation
Development) is free software developed by Marco Valente (documentation
and downloads available at <http://labsimdev.org>).

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

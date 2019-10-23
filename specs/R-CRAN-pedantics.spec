%global packname  pedantics
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Functions to Facilitate Power and Sensitivity Analyses forGenetic Studies of Natural Populations

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildRequires:    R-CRAN-MasterBayes 
BuildRequires:    R-CRAN-MCMCglmm 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-genetics 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-MasterBayes 
Requires:         R-CRAN-MCMCglmm 
Requires:         R-CRAN-kinship2 
Requires:         R-grid 
Requires:         R-CRAN-genetics 
Requires:         R-CRAN-mvtnorm 

%description
Functions for sensitivity and power analysis, for calculating statistics
describing pedigrees from wild populations, and for viewing pedigrees.

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
%doc %{rlibdir}/%{packname}/pedanticsTutorial.pdf
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

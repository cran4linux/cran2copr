%global __brp_check_rpaths %{nil}
%global packname  MetFns
%global packver   3.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Visual Meteor Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-astroFns 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-astroFns 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-pracma 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions for selection of visual meteor data, calculations of Zenithal
Hourly Rate (ZHR) and population index, graphics of population index, ZHR
and magnitude distribution.

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

%global packname  MCI2
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Market Area Models for Retail and Service Locations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCI 
BuildRequires:    R-CRAN-REAT 
BuildRequires:    R-CRAN-tmaptools 
BuildRequires:    R-CRAN-osrm 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-MCI 
Requires:         R-CRAN-REAT 
Requires:         R-CRAN-tmaptools 
Requires:         R-CRAN-osrm 
Requires:         R-CRAN-reshape 

%description
Market area models are used to analyze and predict store choices and
market areas concerning retail and service locations. This package is a
more user-friendly wrapper of the functions in the package 'MCI' (Wieland
2017) providing market area analysis using the Huff Model or the
Multiplicative Competitive Interaction (MCI) Model. In 'MCI2', also a
function for creating transport costs matrices is provided.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX

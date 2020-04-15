%global packname  osrm
%global packver   3.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.3
Release:          1%{?dist}
Summary:          Interface Between R and the OpenStreetMap-Based Routing ServiceOSRM

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-isoband 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gepaf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-RCurl 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-isoband 
Requires:         R-methods 
Requires:         R-CRAN-gepaf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 

%description
An interface between R and the OSRM API. OSRM is a routing service based
on OpenStreetMap data. See <http://project-osrm.org/> for more
information. This package allows to compute distances (travel time and
kilometric distance) between points and travel time matrices.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/forReadme.R
%doc %{rlibdir}/%{packname}/test.r
%{rlibdir}/%{packname}/INDEX

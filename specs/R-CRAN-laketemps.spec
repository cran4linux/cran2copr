%global __brp_check_rpaths %{nil}
%global packname  laketemps
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Lake Temperatures Collected by Situ and Satellite Methods from1985-2009

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 

%description
Lake temperature records, metadata, and climate drivers for 291 global
lakes during the time period 1985-2009. Temperature observations were
collected using satellite and in situ methods. Climatic drivers and
geomorphometric characteristics were also compiled and are included for
each lake. Data are part of the associated publication from the Global
Lake Temperature Collaboration project (http://www.laketemperature.org).
See citation('laketemps') for dataset attribution.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

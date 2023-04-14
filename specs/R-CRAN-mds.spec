%global __brp_check_rpaths %{nil}
%global packname  mds
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}%{?buildtag}
Summary:          Medical Devices Surveillance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-stats 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-lubridate 

%description
A set of core functions for handling medical device event data in the
context of post-market surveillance, pharmacovigilance, signal detection
and trending, and regulatory reporting. Primary inputs are data on events
by device and data on exposures by device. Outputs include: standardized
device-event and exposure datasets, defined analyses, and time series.

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
%{rlibdir}/%{packname}

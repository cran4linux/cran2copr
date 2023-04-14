%global __brp_check_rpaths %{nil}
%global packname  waver
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Calculate Fetch and Wave Energy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-geosphere >= 1.5
BuildRequires:    R-CRAN-sp >= 1.1
BuildRequires:    R-CRAN-rgdal >= 0.8
BuildRequires:    R-CRAN-rgeos >= 0.3
BuildRequires:    R-methods 
Requires:         R-CRAN-geosphere >= 1.5
Requires:         R-CRAN-sp >= 1.1
Requires:         R-CRAN-rgdal >= 0.8
Requires:         R-CRAN-rgeos >= 0.3
Requires:         R-methods 

%description
Functions for calculating the fetch (length of open water distance along
given directions) and estimating wave energy from wind and wave monitoring
data.

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

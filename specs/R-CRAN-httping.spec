%global __brp_check_rpaths %{nil}
%global packname  httping
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          'Ping' 'URLs' to Time 'Requests'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-httpcode >= 0.2.0
BuildRequires:    R-CRAN-pryr >= 0.1.3
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-httpcode >= 0.2.0
Requires:         R-CRAN-pryr >= 0.1.3
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 

%description
A suite of functions to ping 'URLs' and to time 'HTTP' 'requests'.
Designed to work with 'httr'.

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

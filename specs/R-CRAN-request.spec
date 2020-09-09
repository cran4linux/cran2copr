%global packname  request
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          High Level 'HTTP' Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.1.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-curl >= 0.9
BuildRequires:    R-CRAN-jsonlite >= 0.9.19
BuildRequires:    R-CRAN-whisker >= 0.3
BuildRequires:    R-CRAN-lazyeval >= 0.1.10
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.1.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-curl >= 0.9
Requires:         R-CRAN-jsonlite >= 0.9.19
Requires:         R-CRAN-whisker >= 0.3
Requires:         R-CRAN-lazyeval >= 0.1.10
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
High level and easy 'HTTP' client for 'R'. Provides functions for building
'HTTP' queries, including query parameters, body requests, headers,
authentication, and more.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

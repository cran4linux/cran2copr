%global packname  webmockr
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stubbing and Setting Expectations on 'HTTP' Requests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.1.3
BuildRequires:    R-CRAN-urltools >= 1.6.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-crul >= 0.7.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-fauxpas 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-R6 >= 2.1.3
Requires:         R-CRAN-urltools >= 1.6.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-crul >= 0.7.0
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-fauxpas 
Requires:         R-CRAN-base64enc 

%description
Stubbing and setting expectations on 'HTTP' requests. Includes tools for
stubbing 'HTTP' requests, including expected request conditions and
response conditions. Match on 'HTTP' method, query parameters, request
body, headers and more. Can be used for unit tests or outside of a testing
context.

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

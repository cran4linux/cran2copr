%global packname  opentripplanner
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Setup and connect to 'OpenTripPlanner'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 0.9.3
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-googlePolylines 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-sf >= 0.9.3
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-googlePolylines 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-tibble 

%description
Setup and connect to 'OpenTripPlanner' (OTP)
<http://www.opentripplanner.org/>. OTP is an open source platform for
multi-modal and multi-agency journey planning written in 'Java'. The
package allows you to manage a local version or connect to remote OTP
server to find walking, cycling, driving, or transit routes. This package
has been peer-reviewed by rOpenSci (v. 0.2.0.0).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

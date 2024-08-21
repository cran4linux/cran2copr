%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sched
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Request Scheduler

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-fscache >= 1.0.3
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-openssl 
Requires:         R-CRAN-fscache >= 1.0.3
Requires:         R-CRAN-R6 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-lgr 
Requires:         R-methods 
Requires:         R-CRAN-RCurl 
Requires:         R-tools 
Requires:         R-CRAN-openssl 

%description
Offers classes and functions to contact web servers while enforcing
scheduling rules required by the sites. The URL class makes it easy to
construct a URL by providing parameters as a vector. The Request class
allows to describes SOAP (Simple Object Access Protocol) or standard
requests: URL, method (POST or GET), header, body. The Scheduler class
controls the request frequency for each server address by mean of rules
(Rule class). The RequestResult class permits to get the request status to
handle error cases and the content.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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

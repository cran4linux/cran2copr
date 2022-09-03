%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RSelenium
%global packver   1.7.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.9
Release:          1%{?dist}%{?buildtag}
Summary:          R Bindings for 'Selenium WebDriver'

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wdman >= 0.2.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-wdman >= 0.2.2
Requires:         R-methods 
Requires:         R-CRAN-caTools 
Requires:         R-utils 
Requires:         R-CRAN-httr 

%description
Provides a set of R bindings for the 'Selenium 2.0 WebDriver' (see
<https://www.selenium.dev/documentation/> for more information) using the
'JsonWireProtocol' (see
<https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol> for more
information). 'Selenium 2.0 WebDriver' allows driving a web browser
natively as a user would either locally or on a remote machine using the
Selenium server it marks a leap forward in terms of web browser
automation. Selenium automates web browsers (commonly referred to as
browsers). Using RSelenium you can automate browsers locally or remotely.

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

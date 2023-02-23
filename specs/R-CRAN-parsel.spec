%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  parsel
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Dynamic Web-Scraping Using 'RSelenium'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.6.2
BuildRequires:    R-methods >= 3.3.1
BuildRequires:    R-utils >= 2.10.1
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-RSelenium 
BuildRequires:    R-CRAN-rlang 
Requires:         R-parallel >= 3.6.2
Requires:         R-methods >= 3.3.1
Requires:         R-utils >= 2.10.1
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-RSelenium 
Requires:         R-CRAN-rlang 

%description
A system to increase the efficiency of dynamic web-scraping with
'RSelenium' by leveraging parallel processing. You provide a function
wrapper for your 'RSelenium' scraping routine with a set of inputs, and
'parsel' runs it in several browser instances. Chunked input processing as
well as error catching and logging ensures seamless execution and minimal
data loss, even when unforeseen 'RSelenium' errors occur. You can
additionally build safe scraping functions with minimal coding by
utilizing constructor functions that act as wrappers around 'RSelenium'
methods.

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

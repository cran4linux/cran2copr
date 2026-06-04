%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  twscrapeR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Twitter/X Scraping via Python's 'twscrape' Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-reticulate >= 1.20
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-reticulate >= 1.20
Requires:         R-CRAN-jsonlite 

%description
A comprehensive R interface to Python's 'twscrape' library for scraping
Twitter/X data. This package uses 'reticulate' to provide a seamless R
interface to the fully functional Python 'twscrape' library. Supports
searching tweets, user timelines, followers, and more, with built-in rate
limiting and multi-account support. Built on top of 'twscrape' by vladkens
<https://github.com/vladkens/twscrape> and inspired by 'snscrape' by
JustAnotherArchivist <https://github.com/JustAnotherArchivist/snscrape>.

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

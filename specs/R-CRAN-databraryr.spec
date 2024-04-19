%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  databraryr
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Interact with the 'Databrary.org' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods >= 4.3.2
BuildRequires:    R-utils >= 4.3.2
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-magick >= 2.8.2
BuildRequires:    R-CRAN-jsonlite >= 1.8.8
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-httr >= 1.4.7
BuildRequires:    R-CRAN-keyring >= 1.3.2
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-lifecycle >= 1.0.4
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-xfun >= 0.41
BuildRequires:    R-CRAN-getPass >= 0.2.4
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rvest 
Requires:         R-methods >= 4.3.2
Requires:         R-utils >= 4.3.2
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-magick >= 2.8.2
Requires:         R-CRAN-jsonlite >= 1.8.8
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-httr >= 1.4.7
Requires:         R-CRAN-keyring >= 1.3.2
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-lifecycle >= 1.0.4
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-xfun >= 0.41
Requires:         R-CRAN-getPass >= 0.2.4
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rvest 

%description
'Databrary.org' is a restricted access repository for research data,
especially video and audio.  This package provides commands to interact
with the data stored on 'Databrary.org'.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  togglr
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          'Toggl.com' Api for 'Rstudio'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 
Requires:         R-utils 

%description
Use the <https://toggl.com> time tracker api through R.

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

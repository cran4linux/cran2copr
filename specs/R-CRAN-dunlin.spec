%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dunlin
%global packver   0.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Preprocessing Tools for Clinical Trial Data

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.15
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.1
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-glue >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-methods 
Requires:         R-CRAN-yaml >= 2.1.15
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.1
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-glue >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-methods 

%description
A collection of functions to preprocess data and organize them in a format
amenable to use by chevron.

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

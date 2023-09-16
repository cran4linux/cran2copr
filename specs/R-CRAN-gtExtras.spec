%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtExtras
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extending 'gt' for Beautiful HTML Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-glue >= 1.6.1
BuildRequires:    R-CRAN-paletteer >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.35
BuildRequires:    R-CRAN-scales >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-rlang >= 1.0.4
BuildRequires:    R-CRAN-gt >= 0.9.0
BuildRequires:    R-CRAN-htmltools >= 0.5.3
BuildRequires:    R-CRAN-fontawesome >= 0.4.0
BuildRequires:    R-CRAN-commonmark 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-glue >= 1.6.1
Requires:         R-CRAN-paletteer >= 1.4.0
Requires:         R-CRAN-knitr >= 1.35
Requires:         R-CRAN-scales >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-rlang >= 1.0.4
Requires:         R-CRAN-gt >= 0.9.0
Requires:         R-CRAN-htmltools >= 0.5.3
Requires:         R-CRAN-fontawesome >= 0.4.0
Requires:         R-CRAN-commonmark 

%description
Provides additional functions for creating beautiful tables with 'gt'. The
functions are generally wrappers around boilerplate or adding opinionated
niche capabilities and helpers functions.

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

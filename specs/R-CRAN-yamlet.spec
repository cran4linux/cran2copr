%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  yamlet
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Versatile Curation of Table Metadata

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-csv >= 0.6.2
BuildRequires:    R-CRAN-spork >= 0.3.3
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-encode 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-csv >= 0.6.2
Requires:         R-CRAN-spork >= 0.3.3
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-encode 
Requires:         R-CRAN-units 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-knitr 

%description
A YAML-based mechanism for working with table metadata. Supports compact
syntax for creating, modifying, viewing, exporting, importing, displaying,
and plotting metadata coded as column attributes. The 'yamlet' dialect is
valid 'YAML' with defaults and conventions chosen to improve readability.
See ?yamlet, ?decorate, ?modify, ?io_csv, and ?ggplot.decorated.

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

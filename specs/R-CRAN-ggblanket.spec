%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggblanket
%global packver   21.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          21.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Publication-Quality 'ggplot2' Visualisation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-scales >= 1.4.0
BuildRequires:    R-CRAN-ggnewscale >= 0.5.2
BuildRequires:    R-CRAN-blends 
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-CRAN-ggrefine 
BuildRequires:    R-CRAN-jumble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-scales >= 1.4.0
Requires:         R-CRAN-ggnewscale >= 0.5.2
Requires:         R-CRAN-blends 
Requires:         R-CRAN-farver 
Requires:         R-CRAN-ggrefine 
Requires:         R-CRAN-jumble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-viridis 

%description
Wrapper 'ggplot2' functions for publication-quality visualisation. Aligned
with 'ggplot2' and 'tidyverse'. Covers much of what 'ggplot2' does.

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

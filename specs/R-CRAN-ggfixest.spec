%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggfixest
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dedicated 'ggplot2' Methods for 'fixest' Objects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-fixest >= 0.11.2
BuildRequires:    R-CRAN-marginaleffects >= 0.10.0
BuildRequires:    R-CRAN-dreamerr 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-fixest >= 0.11.2
Requires:         R-CRAN-marginaleffects >= 0.10.0
Requires:         R-CRAN-dreamerr 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides 'ggplot2' equivalents of fixest::coefplot() and fixest::iplot(),
for producing nice coefficient plots and interaction plots. Enables some
additional functionality and convenience features, including grouped
multi-'fixest' object faceting and programmatic updates to existing plots
(e.g., themes and aesthetics).

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

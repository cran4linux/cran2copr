%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hatchR
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Predict Fish Hatch and Emergence Timing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-lubridate >= 1.9.4
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-lifecycle >= 1.0.4
BuildRequires:    R-CRAN-ggtext >= 0.1.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-lubridate >= 1.9.4
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-lifecycle >= 1.0.4
Requires:         R-CRAN-ggtext >= 0.1.2
Requires:         R-stats 
Requires:         R-utils 

%description
Predict hatch and emergence timing for a wide range of wild fishes using
the effective value framework (Sparks et al., (2019)
<DOI:10.1139/cjfas-2017-0468>). 'hatchR' offers users access to
established phenological models and the flexibility to incorporate custom
parameterizations using external datasets.

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

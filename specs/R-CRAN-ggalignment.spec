%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggalignment
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Plots 'D&D'-Style Alignment Charts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-magrittr >= 1.0.0
BuildRequires:    R-CRAN-ggimage >= 0.2.0
BuildRequires:    R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-magrittr >= 1.0.0
Requires:         R-CRAN-ggimage >= 0.2.0
Requires:         R-CRAN-rlang >= 0.1.2

%description
'D&D' alignment charts show 9 boxes with values for good through evil and
values for chaotic through lawful. This package easily creates these
alignment charts from user-provided image paths and alignment values.

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

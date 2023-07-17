%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ediblecity
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling Urban Agriculture at City Scale

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-CRAN-rlang >= 1.0
BuildRequires:    R-CRAN-sf >= 0.9
BuildRequires:    R-CRAN-stars >= 0.5
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-CRAN-rlang >= 1.0
Requires:         R-CRAN-sf >= 0.9
Requires:         R-CRAN-stars >= 0.5

%description
The purpose of this package is to estimate the potential of urban
agriculture to contribute to addressing several urban challenges at the
city-scale. Within this aim, we selected 8 indicators directly related to
one or several urban challenges. Also, a function is provided to compute
new scenarios of urban agriculture. Methods are described by Pueyo-Ros,
Comas & Corominas (2023) <doi:10.12688/openreseurope.16054.1>.

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

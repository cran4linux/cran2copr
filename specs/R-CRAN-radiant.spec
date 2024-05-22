%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  radiant
%global packver   1.6.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Business Analytics using R and Shiny

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-radiant.data >= 1.6.6
BuildRequires:    R-CRAN-radiant.design >= 1.6.6
BuildRequires:    R-CRAN-radiant.basics >= 1.6.6
BuildRequires:    R-CRAN-radiant.model >= 1.6.6
BuildRequires:    R-CRAN-radiant.multivariate >= 1.6.6
BuildRequires:    R-CRAN-import >= 1.1.0
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-radiant.data >= 1.6.6
Requires:         R-CRAN-radiant.design >= 1.6.6
Requires:         R-CRAN-radiant.basics >= 1.6.6
Requires:         R-CRAN-radiant.model >= 1.6.6
Requires:         R-CRAN-radiant.multivariate >= 1.6.6
Requires:         R-CRAN-import >= 1.1.0

%description
A platform-independent browser-based interface for business analytics in
R, based on the shiny package. The application combines the functionality
of 'radiant.data', 'radiant.design', 'radiant.basics', 'radiant.model',
and 'radiant.multivariate'.

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

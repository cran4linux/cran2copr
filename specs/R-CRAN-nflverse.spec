%global __brp_check_rpaths %{nil}
%global packname  nflverse
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load the 'nflverse'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nflfastR >= 4.3.0
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-crayon >= 1.4.0
BuildRequires:    R-CRAN-nflreadr >= 1.1.2
BuildRequires:    R-CRAN-nflseedR >= 1.0.2
BuildRequires:    R-CRAN-nfl4th >= 1.0.1
BuildRequires:    R-CRAN-nflplotR >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-rstudioapi >= 0.13
Requires:         R-CRAN-nflfastR >= 4.3.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-crayon >= 1.4.0
Requires:         R-CRAN-nflreadr >= 1.1.2
Requires:         R-CRAN-nflseedR >= 1.0.2
Requires:         R-CRAN-nfl4th >= 1.0.1
Requires:         R-CRAN-nflplotR >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-rstudioapi >= 0.13

%description
The 'nflverse' is a set of packages dedicated to data of the National
Football League. This package is designed to make it easy to install and
load multiple 'nflverse' packages in a single step. Learn more about the
'nflverse' at <https://nflverse.nflverse.com/>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jetpack
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          A Friendly Package Manager

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-remotes >= 2.0.3
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-docopt >= 0.4
BuildRequires:    R-CRAN-renv >= 0.13.1
Requires:         R-CRAN-remotes >= 2.0.3
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-docopt >= 0.4
Requires:         R-CRAN-renv >= 0.13.1

%description
Manage project dependencies from your DESCRIPTION file. Create a
reproducible virtual environment with minimal additional files in your
project. Provides tools to add, remove, and update dependencies as well as
install existing dependencies with a single function.

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

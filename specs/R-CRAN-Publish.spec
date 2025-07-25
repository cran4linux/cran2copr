%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Publish
%global packver   2025.07.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2025.07.24
Release:          1%{?dist}%{?buildtag}
Summary:          Format Output of Various Routines in a Suitable Way for Reports and Publication

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 2.38
BuildRequires:    R-CRAN-prodlim >= 1.5.4
BuildRequires:    R-CRAN-lava >= 1.5.1
BuildRequires:    R-CRAN-multcomp >= 1.4
BuildRequires:    R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-survival >= 2.38
Requires:         R-CRAN-prodlim >= 1.5.4
Requires:         R-CRAN-lava >= 1.5.1
Requires:         R-CRAN-multcomp >= 1.4
Requires:         R-CRAN-data.table >= 1.10.4

%description
A bunch of convenience functions that transform the results of some basic
statistical analyses into table format nearly ready for publication. This
includes descriptive tables, tables of logistic regression and Cox
regression results as well as forest plots.

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

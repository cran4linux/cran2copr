%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcompanion
%global packver   2.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Support Extension Education Program Evaluation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.4.0
BuildRequires:    R-graphics >= 4.4.0
BuildRequires:    R-CRAN-plyr >= 1.8.9
BuildRequires:    R-CRAN-coin >= 1.4.3
BuildRequires:    R-CRAN-boot >= 1.3.30
BuildRequires:    R-CRAN-nortest >= 1.0.4
BuildRequires:    R-CRAN-DescTools >= 0.99.58
BuildRequires:    R-CRAN-lmtest >= 0.9.40
BuildRequires:    R-CRAN-multcompView >= 0.1.10
Requires:         R-stats >= 4.4.0
Requires:         R-graphics >= 4.4.0
Requires:         R-CRAN-plyr >= 1.8.9
Requires:         R-CRAN-coin >= 1.4.3
Requires:         R-CRAN-boot >= 1.3.30
Requires:         R-CRAN-nortest >= 1.0.4
Requires:         R-CRAN-DescTools >= 0.99.58
Requires:         R-CRAN-lmtest >= 0.9.40
Requires:         R-CRAN-multcompView >= 0.1.10

%description
Functions and datasets to support Summary and Analysis of Extension
Program Evaluation in R, and An R Companion for the Handbook of Biological
Statistics. Vignettes are available at <https://rcompanion.org>.

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

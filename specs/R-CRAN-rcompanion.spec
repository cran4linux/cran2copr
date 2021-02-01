%global packname  rcompanion
%global packver   2.3.27
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.27
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Support Extension Education Program Evaluation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.3.0
BuildRequires:    R-graphics >= 3.3.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-boot >= 1.3.18
BuildRequires:    R-CRAN-coin >= 1.1.2
BuildRequires:    R-CRAN-EMT >= 1.1
BuildRequires:    R-CRAN-nortest >= 1.0.4
BuildRequires:    R-CRAN-DescTools >= 0.99.17
BuildRequires:    R-CRAN-lmtest >= 0.9.34
BuildRequires:    R-CRAN-multcompView >= 0.1.7
Requires:         R-stats >= 3.3.0
Requires:         R-graphics >= 3.3.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-boot >= 1.3.18
Requires:         R-CRAN-coin >= 1.1.2
Requires:         R-CRAN-EMT >= 1.1
Requires:         R-CRAN-nortest >= 1.0.4
Requires:         R-CRAN-DescTools >= 0.99.17
Requires:         R-CRAN-lmtest >= 0.9.34
Requires:         R-CRAN-multcompView >= 0.1.7

%description
Functions and datasets to support "Summary and Analysis of Extension
Program Evaluation in R" and "An R Companion for the Handbook of
Biological Statistics". Vignettes are available at
<http://rcompanion.org>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  atable
%global packver   0.1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.14
Release:          1%{?dist}%{?buildtag}
Summary:          Create Tables for Reporting Clinical Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-doBy >= 4.6
BuildRequires:    R-CRAN-Hmisc >= 4.1
BuildRequires:    R-stats >= 3.4
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-DescTools >= 0.99.24
BuildRequires:    R-CRAN-effsize >= 0.7.1
BuildRequires:    R-CRAN-settings >= 0.2.4
Requires:         R-CRAN-doBy >= 4.6
Requires:         R-CRAN-Hmisc >= 4.1
Requires:         R-stats >= 3.4
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-DescTools >= 0.99.24
Requires:         R-CRAN-effsize >= 0.7.1
Requires:         R-CRAN-settings >= 0.2.4

%description
Create Tables for Reporting Clinical Trials. Calculates descriptive
statistics and hypothesis tests, arranges the results in a table ready for
reporting with LaTeX, HTML or Word.

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

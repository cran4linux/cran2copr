%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  remverse
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Meta-Package for Relational Event History Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-remify >= 4.0.0
BuildRequires:    R-CRAN-remstats >= 4.0.0
BuildRequires:    R-CRAN-remstimate >= 3.0.0
Requires:         R-CRAN-remify >= 4.0.0
Requires:         R-CRAN-remstats >= 4.0.0
Requires:         R-CRAN-remstimate >= 3.0.0

%description
A unified workflow for relational event modeling by re-exporting core
functions from 'remify', 'remstats', and 'remstimate'. Supports
tie-oriented and actor-oriented modeling with frequentist and Bayesian
estimation. Methods are described in Butts (2008)
<doi:10.1111/j.1467-9531.2008.00203.x> and Stadtfeld and Block (2017)
<doi:10.1177/0081175017709295>.

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

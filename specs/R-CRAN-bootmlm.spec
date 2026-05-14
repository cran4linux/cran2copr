%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bootmlm
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap Resampling for Multilevel Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot >= 1.3.19
BuildRequires:    R-CRAN-Matrix >= 1.2.11
BuildRequires:    R-CRAN-lme4 >= 1.1.16
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-boot >= 1.3.19
Requires:         R-CRAN-Matrix >= 1.2.11
Requires:         R-CRAN-lme4 >= 1.1.16
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions for bootstrapping with multilevel data and models (and
mixed-effect models). It implements multiple bootstrap methods under the
parametric, residual, and case bootstrap categories, as discussed in Van
der Leeden, Meijer, and Busing (2008) <doi:10.1007/978-0-387-73186-5_11>
and Carpenter, Goldstein, and Rasbash (2003)
<doi:10.1111/1467-9876.00415>. Currently it supports fitted objects from
the 'lme4' package.

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

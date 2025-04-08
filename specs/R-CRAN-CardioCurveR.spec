%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CardioCurveR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Modeling of R-R Interval Dynamics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-signal >= 1.8.1
BuildRequires:    R-CRAN-data.table >= 1.16.4
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-signal >= 1.8.1
Requires:         R-CRAN-data.table >= 1.16.4

%description
Automated and robust framework for analyzing R-R interval (RRi) signals
using advanced nonlinear modeling and preprocessing techniques. The
package implements a dual-logistic model to capture the rapid drop and
subsequent recovery of RRi during exercise, as described by
Castillo-Aguilar et al. (2025) <doi:10.1038/s41598-025-93654-6>. In
addition, 'CardioCurveR' includes tools for filtering RRi signals using
zero-phase Butterworth low-pass filtering and for cleaning ectopic beats
via adaptive outlier replacement using local regression and robust
statistics. These integrated methods preserve the dynamic features of RRi
signals and facilitate accurate cardiovascular monitoring and clinical
research.

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

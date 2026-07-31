%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ksamplesLTRC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          K-Sample Tests for Truncated and/or Censored Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Tools for the nonparametric analysis and comparison of distributions under
left truncation and right censoring. The package includes simulation
routines for truncated and/or censored survival data, nonparametric
distribution comparison methods based on Kolmogorov-Smirnov-type and
Cramér-von Mises-type statistics, and bootstrap routines for p-value
approximation. For methodological details, see Lago, de Uña-Álvarez and
Pardo-Fernández (2025) <doi:10.1007/s11749-024-00948-4> and Lago,
Pardo-Fernández and de Uña-Álvarez (2026)
<doi:10.1007/s10985-026-09713-1>.

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

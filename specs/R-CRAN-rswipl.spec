%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rswipl
%global packver   9.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          9.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Embed 'SWI'-'Prolog'

License:          FreeBSD
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-Rcpp >= 1.0.7

%description
Interface to 'SWI'-'Prolog', <https://www.swi-prolog.org/>. This package
is normally not loaded directly, please refer to package 'rolog' instead.
The purpose of this package is to provide the 'Prolog' runtime on systems
that do not have a software installation of 'SWI'-'Prolog'.

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

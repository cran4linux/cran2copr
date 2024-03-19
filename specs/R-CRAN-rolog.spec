%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rolog
%global packver   0.9.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.15
Release:          1%{?dist}%{?buildtag}
Summary:          Query 'SWI'-'Prolog' from R

License:          FreeBSD
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-rswipl >= 9.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-methods 
Requires:         R-utils 

%description
This R package connects to SWI-Prolog, <https://www.swi-prolog.org/>, so
that R can send deterministic and non-deterministic queries to prolog
(consult, query/submit, once, findall).

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

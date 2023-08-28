%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SuperRanker
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Rank Agreement

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-prodlim >= 1.5.7
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-prodlim >= 1.5.7
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-stats 
Requires:         R-graphics 

%description
Tools for analysing the agreement of two or more rankings of the same
items. Examples are importance rankings of predictor variables and risk
predictions of subjects. Benchmarks for agreement are computed based on
random permutation and bootstrap. See Ekstrøm CT, Gerds TA, Jensen, AK
(2018). "Sequential rank agreement methods for comparison of ranked
lists." _Biostatistics_, *20*(4), 582-598
<doi:10.1093/biostatistics/kxy017> for more information.

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

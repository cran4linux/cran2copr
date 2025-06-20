%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  m2r
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'Macaulay2'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mpoly >= 1.0.5
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-mpoly >= 1.0.5
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-Rcpp 

%description
Persistent interface to 'Macaulay2' <https://www.macaulay2.com> and
front-end tools facilitating its use in the 'R' ecosystem. For details see
Kahle et. al. (2020) <doi:10.18637/jss.v093.i09>.

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

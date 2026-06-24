%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  srr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'rOpenSci' Software Review 'Roclets'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-rprojroot 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-here 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-rprojroot 

%description
Companion package to 'rOpenSci' statistical software review project
('rOpenSci' authors, 2021; <doi:10.5281/zenodo.5556756>), to facilitate
documenting software compliance with statistical standards using
'Roxygen2' 'roclets'.

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

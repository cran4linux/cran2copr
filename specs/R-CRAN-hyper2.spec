%global __brp_check_rpaths %{nil}
%global packname  hyper2
%global packver   2.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          The Hyperdirichlet Distribution, Mark 2

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-disordR >= 0.0.9
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-calibrator 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-disordR >= 0.0.9
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-calibrator 

%description
A suite of routines for the hyperdirichlet distribution; supersedes the
'hyperdirichlet' package.

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

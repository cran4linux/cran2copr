%global __brp_check_rpaths %{nil}
%global packname  GPCMlasso
%global packver   0.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Differential Item Functioning in Generalized Partial Credit Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mirt 
Requires:         R-methods 

%description
Provides a framework to detect Differential Item Functioning (DIF) in
Generalized Partial Credit Models (GPCM) and special cases of the GPCM as
proposed by Schauberger and Mair (2019) <doi:10.3758/s13428-019-01224-2>.
A joint model is set up where DIF is explicitly parametrized and penalized
likelihood estimation is used for parameter selection. The big advantage
of the method called GPCMlasso is that several variables can be treated
simultaneously and that both continuous and categorical variables can be
used to detect DIF.

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

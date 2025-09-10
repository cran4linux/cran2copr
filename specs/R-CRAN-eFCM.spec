%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eFCM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exponential Factor Copula Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-nsRFA 
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-nsRFA 
Requires:         R-CRAN-ismev 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-progress 

%description
Implements the exponential Factor Copula Model (eFCM) of Castro-Camilo, D.
and Huser, R. (2020) for spatial extremes, with tools for dependence
estimation, tail inference, and visualization. The package supports
likelihood-based inference, Gaussian process modeling via Matérn
covariance functions, and bootstrap uncertainty quantification. See
Castro-Camilo and Huser (2020) <doi:10.1080/01621459.2019.1647842>.

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

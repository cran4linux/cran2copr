%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fdarep
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Dimensional FPCA, Marginal FPCA, and Product FPCA for Repeated Functional Data

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-CRAN-fdapace 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-fdapace 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-numDeriv 

%description
Provides an implementation of two-dimensional functional principal
component analysis (FPCA), Marginal FPCA, and Product FPCA for repeated
functional data. Marginal and Product FPCA implementations are done for
both dense and sparsely observed functional data. References: Chen, K.,
Delicado, P., & Müller, H. G. (2017) <doi:10.1111/rssb.12160>. Chen, K., &
Müller, H. G. (2012) <doi:10.1080/01621459.2012.734196>. Hall, P., Müller,
H.G. and Wang, J.L. (2006) <doi:10.1214/009053606000000272>. Yao, F.,
Müller, H. G., & Wang, J. L. (2005) <doi:10.1198/016214504000001745>.

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

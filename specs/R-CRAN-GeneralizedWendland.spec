%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeneralizedWendland
%global packver   0.5-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fully Parameterized Generalized Wendland Covariance Function

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-spam64 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-spam64 
Requires:         R-parallel 
Requires:         R-CRAN-optimParallel 
Requires:         R-CRAN-fields 

%description
A fully parameterized Generalized Wendland covariance function for use in
Gaussian process models, as well as multiple methods for approximating it
via covariance interpolation. The available methods are linear
interpolation, polynomial interpolation, and cubic spline interpolation.
Moreno Bevilacqua and Reinhard Furrer and Tarik Faouzi and Emilio Porcu
(2019)
<url:<https://projecteuclid.org/journalArticle/Download?urlId=10.1214%%2F17-AOS1652
>>. Moreno Bevilacqua and Christian Caamaño-Carrillo and Emilio Porcu
(2022) <arXiv:2008.02904>. Reinhard Furrer and Roman Flury and Florian
Gerber (2022) <url:<https://CRAN.R-project.org/package=spam >>.

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

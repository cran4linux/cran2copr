%global packname  cort
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Some Empiric and Nonparametric Copula Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-furrr >= 0.2.0
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-furrr >= 0.2.0
Requires:         R-CRAN-Rdpack 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-osqp 
Requires:         R-CRAN-Rcpp 

%description
Provides S4 classes and methods to fit several copula models: The classic
empirical checkerboard copula and the empirical checkerboard copula with
known margins, see Cuberos, Masiello and Maume-Deschamps (2019)
<doi:10.1080/03610926.2019.1586936> are proposed. These two models allow
to fit copulas in high dimension with a small number of observations, and
they are always proper copulas. Some flexibility is added via a
possibility to differentiate the checkerboard parameter by dimension. The
last model consist of the implementation of the Copula Recursive Tree
algorithm proposed by Laverny, Maume-Deschamps, Masiello and Rullière
(2020) <arXiv:2005.02912>, including the localised dimension reduction,
which fits a copula by recursive splitting of the copula domain. We also
provide an efficient way of mixing copulas, allowing to bag the algorithm
into a forest, and a generic way of measuring d-dimensional boxes with a
copula.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

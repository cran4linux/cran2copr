%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GWnorm
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          G-Wishart Normalising Constants for Gaussian Graphical Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.1.1
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-BDgraph 
BuildRequires:    R-CRAN-CholWishart 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.1.1
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-BDgraph 
Requires:         R-CRAN-CholWishart 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Computes G-Wishart normalising constants through a Fourier approach.
Either exact analytical results, numerical integration or Monte Carlo
estimation are employed. Details at C. Wong, G. Moffa and J. Kuipers
(2024), <doi:10.48550/arXiv.2404.06803>.

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

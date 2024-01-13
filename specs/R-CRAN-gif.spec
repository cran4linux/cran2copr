%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gif
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Independence Filtering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 

%description
Provides a method of recovering the precision matrix for Gaussian
graphical models efficiently. Our approach could be divided into three
categories. First of all, we use Hard Graphical Thresholding for best
subset selection problem of Gaussian graphical model, and the core concept
of this method was proposed by Luo et al. (2014) <arXiv:1407.7819>.
Secondly, a closed form solution for graphical lasso under acyclic graph
structure is implemented in our package (Fattahi and Sojoudi (2019)
<https://jmlr.org/papers/v20/17-501.html>). Furthermore, we implement
block coordinate descent algorithm to efficiently solve the covariance
selection problem (Dempster (1972) <doi:10.2307/2528966>). Our package is
computationally efficient and can solve ultra-high-dimensional problems,
e.g. p > 10,000, in a few minutes.

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

%global __brp_check_rpaths %{nil}
%global packname  dgumbel
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          The Gumbel Distribution Functions and Gradients

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.2

%description
Gumbel distribution functions (De Haan L. (2007)
<doi:10.1007/0-387-34471-3>) implemented with the techniques of automatic
differentiation (Griewank A. (2008) <isbn:978-0-89871-659-7>). With this
tool, a user should be able to quickly model extreme events for which the
Gumbel distribution is the domain of attraction. The package makes
available the density function, the distribution function the quantile
function and a random generating function. In addition, it supports
gradient functions. The package combines 'Adept' (C++ templated automatic
differentiation) (Hogan R. (2017) <doi:10.5281/zenodo.1004730>) and
'Eigen' (templated matrix-vector library) for fast computations of both
objective functions and exact gradients. It relies on 'RcppEigen' for easy
access to 'Eigen' and bindings to R.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

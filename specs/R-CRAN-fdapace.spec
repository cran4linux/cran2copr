%global packname  fdapace
%global packver   0.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Data Analysis and Empirical Dynamics

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-numDeriv 

%description
A versatile package that provides implementation of various methods of
Functional Data Analysis (FDA) and Empirical Dynamics. The core of this
package is Functional Principal Component Analysis (FPCA), a key technique
for functional data analysis, for sparsely or densely sampled random
trajectories and time courses, via the Principal Analysis by Conditional
Estimation (PACE) algorithm. This core algorithm yields covariance and
mean functions, eigenfunctions and principal component (scores), for both
functional data and derivatives, for both dense (functional) and sparse
(longitudinal) sampling designs. For sparse designs, it provides fitted
continuous trajectories with confidence bands, even for subjects with very
few longitudinal observations. PACE is a viable and flexible alternative
to random effects modeling of longitudinal data. There is also a Matlab
version (PACE) that contains some methods not available on fdapace and
vice versa. Updates to fdapace were supported by grants from NIH Echo and
NSF DMS-1712864 and DMS-2014626. Please cite our package if you use it
(You may run the command citation("fdapace") to get the citation format
and bibtex entry). References: Wang, J.L., Chiou, J., Müller, H.G. (2016)
<doi:10.1146/annurev-statistics-041715-033624>; Chen, K., Zhang, X.,
Petersen, A., Müller, H.G. (2017) <doi:10.1007/s12561-015-9137-5>.

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

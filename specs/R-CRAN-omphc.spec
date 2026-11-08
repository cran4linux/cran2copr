%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  omphc
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Network Learning Using the OMP Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-pchc 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-pchc 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 

%description
Bayesian network learning using the orthogonal matching pursuit to perform
variable selection and then application of the Hill-Climbing greedy search
or the TABU search to orient the edges. Some relevant papers are Tsagris
M. and Adam C. (2026) <doi:10.13140/RG.2.2.26278.28489>, Tsagris M. (2021)
<doi:10.1007/s10614-020-10065-7>, Tsagris M. (2022)
<doi:10.3390/math10152604>, Tsagris et al. (2022)
<doi:10.1109/TCBB.2020.3029952>, Tsamardinos I., Brown L.E. and Aliferis
C.F. (2006) <doi:10.1007/s10994-006-6889-7>, Mallat S. G. and Zhang Z.
(1993) <doi:10.1109/78.258082>.

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

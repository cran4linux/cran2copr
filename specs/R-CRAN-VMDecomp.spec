%global __brp_check_rpaths %{nil}
%global packname  VMDecomp
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variational Mode Decomposition

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8.3
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.8.3

%description
'RcppArmadillo' implementation for the Matlab code of the 'Variational
Mode Decomposition' and 'Two-Dimensional Variational Mode Decomposition'.
For more information, see (i) 'Variational Mode Decomposition' by K.
Dragomiretskiy and D. Zosso in IEEE Transactions on Signal Processing,
vol. 62, no. 3, pp. 531-544, Feb.1, 2014, <doi:10.1109/TSP.2013.2288675>;
(ii) 'Two-Dimensional Variational Mode Decomposition' by Dragomiretskiy,
K., Zosso, D. (2015), In: Tai, XC., Bae, E., Chan, T.F., Lysaker, M. (eds)
Energy Minimization Methods in Computer Vision and Pattern Recognition.
EMMCVPR 2015. Lecture Notes in Computer Science, vol 8932. Springer,
<doi:10.1007/978-3-319-14612-6_15>.

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

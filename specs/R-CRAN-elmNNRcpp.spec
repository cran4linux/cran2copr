%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  elmNNRcpp
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          The Extreme Learning Machine Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-CRAN-KernelKnn 
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-CRAN-KernelKnn 

%description
Training and predict functions for Single Hidden-layer Feedforward Neural
Networks (SLFN) using the Extreme Learning Machine (ELM) algorithm. The
ELM algorithm differs from the traditional gradient-based algorithms for
very short training times (it doesn't need any iterative tuning, this
makes learning time very fast) and there is no need to set any other
parameters like learning rate, momentum, epochs, etc. This is a
reimplementation of the 'elmNN' package using 'RcppArmadillo' after the
'elmNN' package was archived. For more information, see "Extreme learning
machine: Theory and applications" by Guang-Bin Huang, Qin-Yu Zhu,
Chee-Kheong Siew (2006), Elsevier B.V, <doi:10.1016/j.neucom.2005.12.126>.

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

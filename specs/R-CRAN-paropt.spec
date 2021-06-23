%global __brp_check_rpaths %{nil}
%global packname  paropt
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Parameter Optimizing of ODE-Systems

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.4

%description
Enable optimization of parameters of ordinary differential equations.
Therefore, using 'SUNDIALS' to solve the ODE-System (see Hindmarsh, Alan
C., Peter N. Brown, Keith E. Grant, Steven L. Lee, Radu Serban, Dan E.
Shumaker, and Carol S. Woodward. (2005) <doi:10.1145/1089014.1089020>).
Furthermore, for optimization the particle swarm algorithm is used (see:
Akman, Devin, Olcay Akman, and Elsa Schaefer. (2018)
<doi:10.1155/2018/9160793> and Sengupta, Saptarshi, Sanchita Basak, and
Richard Peters. (2018) <doi:10.3390/make1010010>). The ODE-System has to
be passed as 'Rcpp'-function. The information for the parameter boundaries
and states are conveyed using data.frames.

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

%global __brp_check_rpaths %{nil}
%global packname  rmumps
%global packver   5.2.1-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.2.1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Wrapper for MUMPS Library

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 

%description
Some basic features of 'MUMPS' (Multifrontal Massively Parallel sparse
direct Solver) are wrapped in a class whose methods can be used for
sequentially solving a sparse linear system (symmetric or not) with one or
many right hand sides (dense or sparse). There is a possibility to do
separately symbolic analysis, LU (or LDL^t) factorization and system
solving. Third part ordering libraries are included and can be used:
'PORD', 'METIS', 'SCOTCH'. 'MUMPS' method was first described in Amestoy
et al. (2001) <doi:10.1137/S0895479899358194> and Amestoy et al. (2006)
<doi:10.1016/j.parco.2005.07.004>.

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

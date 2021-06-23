%global __brp_check_rpaths %{nil}
%global packname  rBMF
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Boolean Matrix Factorization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Provides four boolean matrix factorization (BMF) methods. BMF has many
applications like data mining and categorical data analysis. BMF is also
known as boolean matrix decomposition (BMD) and was found to be an NP-hard
(non-deterministic polynomial-time) problem. Currently implemented methods
are 'Asso' Miettinen, Pauli and others (2008) <doi:10.1109/TKDE.2008.53>,
'GreConD' R. Belohlavek, V. Vychodil (2010)
<doi:10.1016/j.jcss.2009.05.002> , 'GreConDPlus' R. Belohlavek, V.
Vychodil (2010) <doi:10.1016/j.jcss.2009.05.002> , 'topFiberM' A. Desouki,
M. Roeder, A. Ngonga (2019) <arXiv:1903.10326>.

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

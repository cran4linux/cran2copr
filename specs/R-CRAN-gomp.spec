%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gomp
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The gamma-OMP Feature Selection Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-ordinal 
Requires:         R-parallel 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
The gamma-Orthogonal Matching Pursuit (gamma-OMP) is a recently suggested
modification of the OMP feature selection algorithm for a wide range of
response variables. The package offers many alternative regression models,
such linear, robust, survival, multivariate etc., including k-fold
cross-validation. References: Tsagris M., Papadovasilakis Z., Lakiotaki K.
and Tsamardinos I. (2018). "Efficient feature selection on gene expression
data: Which algorithm to use?" BioRxiv. <doi:10.1101/431734>. Tsagris M.,
Papadovasilakis Z., Lakiotaki K. and Tsamardinos I. (2022). "The gamma-OMP
algorithm for feature selection with application to gene expression data".
IEEE/ACM Transactions on Computational Biology and Bioinformatics 19(2):
1214--1224. <doi:10.1109/TCBB.2020.3029952>.

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

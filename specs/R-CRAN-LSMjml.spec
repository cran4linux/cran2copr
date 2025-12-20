%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LSMjml
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Latent Space Item Response Models using Joint Maximum Likelihood Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-psych 

%description
In Latent Space Item Response Models, subjects and items are embedded in a
multidimensional Euclidean latent space. As such, interactions among
persons, items, and person-item combinations can be revealed that are
unmodelled in more conventional item response theory models. This package
implements the methods from Molenaar & Jeon (in press) and can be used to
fit Latent Space Item Response Models to data using joint maximum
likelihood estimation. The package can handle binary data, ordinal data,
and data with mixed scales. The package incorporates facilities for data
simulation, rotation of the latent space, and K-fold cross-validation to
select the number of dimensions of the latent space.

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

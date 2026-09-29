%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FSSgam
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Full Subsets Multiple Regression Using GAMs

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-nnet 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Full-subsets information-theoretic approaches are increasingly used to
explore predictive power and variable importance when a wide range of
candidate predictors are being considered. This package provides functions
that can be used to construct, fit, and compare a complete model set of
possible ecological or environmental predictors for a given response
variable of interest. Models are based on Generalized Additive Models
(GAMs) and build on the 'MuMIn' package. Advantages include the capacity
to fit more predictors than there are replicates, automatic removal of
models with correlated predictors, and support for model sets that include
interactions between factors and smooth predictors, as well as
smooth-by-smooth interactions via te(). Methods are described in Fisher et
al. (2018) <doi:10.1002/ece3.4134>.

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

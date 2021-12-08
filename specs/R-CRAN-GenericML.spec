%global __brp_check_rpaths %{nil}
%global packname  GenericML
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generic Machine Learning Inference

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-mlr3learners 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-splitstackshape 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-mlr3learners 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-splitstackshape 
Requires:         R-stats 
Requires:         R-parallel 

%description
Generic Machine Learning Inference on heterogeneous treatment effects in
randomized experiments as proposed in Chernozhukov, Demirer, Duflo and
Fernández-Val (2020) <arXiv:1712.04802>. This package's workhorse is the
'mlr3' framework of Lang et al. (2019) <doi:10.21105/joss.01903>, which
enables the specification of a wide variety of machine learners. The main
functionality, GenericML(), runs Algorithm 1 in Chernozhukov, Demirer,
Duflo and Fernández-Val (2020) <arXiv:1712.04802> for a suite of
user-specified machine learners. All steps in the algorithm are
customizable via setup functions. Methods for printing and plotting are
available for objects returned by GenericML(). Parallel computing is
supported.

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

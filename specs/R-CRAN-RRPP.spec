%global __brp_check_rpaths %{nil}
%global packname  RRPP
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Model Evaluation with Randomized Residuals in a Permutation Procedure

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 

%description
Linear model calculations are made for many random versions of data. Using
residual randomization in a permutation procedure, sums of squares are
calculated over many permutations to generate empirical probability
distributions for evaluating model effects.  This packaged is described by
Collyer & Adams (2018) <doi:10.1111/2041-210X.13029>.  Additionally,
coefficients, statistics, fitted values, and residuals generated over many
permutations can be used for various procedures including pairwise tests,
prediction, classification, and model comparison.  This package should
provide most tools one could need for the analysis of high-dimensional
data, especially in ecology and evolutionary biology, but certainly other
fields, as well.

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

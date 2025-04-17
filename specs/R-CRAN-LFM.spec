%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LFM
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Laplace Factor Model Analysis and Evaluation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FarmTest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-SOPC 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-relliptical 
Requires:         R-stats 
Requires:         R-CRAN-FarmTest 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-SOPC 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-relliptical 

%description
Enables the generation of Laplace factor models across diverse Laplace
distributions and facilitates the application of Sparse Online Principal
Component (SOPC), Incremental Principal Component (IPC), Projected
Principal Component (PPC), Perturbation Principal Component (PPC),
Stochastic Approximation Principal Component (SAPC), Sparse Principal
Component (SPC) and other PC methods and Farm Test methods to these
models. Evaluates the efficacy of these methods within the context of
Laplace factor models by scrutinizing parameter estimation accuracy, mean
square error, and the degree of sparsity.

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

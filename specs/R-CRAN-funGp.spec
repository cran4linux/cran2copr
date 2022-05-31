%global __brp_check_rpaths %{nil}
%global packname  funGp
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Process Models for Scalar and Functional Inputs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-progressr 
Requires:         R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-future 
Requires:         R-CRAN-progressr 

%description
Construction and smart selection of Gaussian process models for analysis
of computer experiments with emphasis on treatment of functional inputs
that are regularly sampled. This package offers: (i) flexible modeling of
functional-input regression problems through the fairly general Gaussian
process model; (ii) built-in dimension reduction for functional inputs;
(iii) heuristic optimization of the structural parameters of the model
(e.g., active inputs, kernel function, type of distance). Metamodeling
background is provided in Betancourt et al. (2020)
<doi:10.1016/j.ress.2020.106870>. The algorithm for structural parameter
optimization is described in
<https://hal.archives-ouvertes.fr/hal-02532713>.

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

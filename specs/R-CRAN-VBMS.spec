%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VBMS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variational Bayesian Algorithm for Multi-Source Heterogeneous Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-selectiveInference 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-selectiveInference 
Requires:         R-CRAN-MASS 

%description
A Variational Bayesian algorithm for high-dimensional multi-source
heterogeneous linear models. More details have been written up in a paper
submitted to the journal Statistics in Medicine, and the details of
variational Bayesian methods can be found in Ray and Szabo (2021)
<doi:10.1080/01621459.2020.1847121>. It simultaneously performs parameter
estimation and variable selection. The algorithm supports two model
settings: (1) local models, where variable selection is only applied to
homogeneous coefficients, and (2) global models, where variable selection
is also performed on heterogeneous coefficients. Two forms of
Spike-and-Slab priors are available: the Laplace distribution and the
Gaussian distribution as the Slab component.

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

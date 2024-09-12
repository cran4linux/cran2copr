%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NeuralEstimators
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood-Free Parameter Estimation using Neural Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-JuliaConnectoR 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-JuliaConnectoR 
Requires:         R-CRAN-magrittr 

%description
An 'R' interface to the 'Julia' package 'NeuralEstimators.jl'. The package
facilitates the user-friendly development of neural point estimators,
which are neural networks that map data to a point summary of the
posterior distribution. These estimators are likelihood-free and
amortised, in the sense that, after an initial setup cost, inference from
observed data can be made in a fraction of the time required by
conventional approaches; see Sainsbury-Dale, Zammit-Mangion, and Huser
(2024) <doi:10.1080/00031305.2023.2249522> for further details and an
accessible introduction. The package also enables the construction of
neural networks that approximate the likelihood-to-evidence ratio in an
amortised manner, allowing one to perform inference based on the
likelihood function or the entire posterior distribution; see
Zammit-Mangion, Sainsbury-Dale, and Huser (2024, Sec. 5.2)
<doi:10.48550/arXiv.2404.12484>, and the references therein. The package
accommodates any model for which simulation is feasible by allowing the
user to implicitly define their model through simulated data.

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

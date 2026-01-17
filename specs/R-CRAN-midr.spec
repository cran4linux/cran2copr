%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  midr
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Learning from Black-Box Models by Maximum Interpretation Decomposition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
The goal of 'midr' is to provide a model-agnostic method for interpreting
and explaining black-box predictive models by creating a globally
interpretable surrogate model. The package implements 'Maximum
Interpretation Decomposition' (MID), a functional decomposition technique
that finds an optimal additive approximation of the original model. This
approximation is achieved by minimizing the squared error between the
predictions of the black-box model and the surrogate model. The
theoretical foundations of MID are described in Iwasawa & Matsumori (2025)
[Forthcoming], and the package itself is detailed in Asashiba et al.
(2025) <doi:10.48550/arXiv.2506.08338>.

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

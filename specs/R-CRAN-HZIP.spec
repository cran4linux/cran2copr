%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HZIP
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood-Based Inference for Joint Modeling of Correlated Count and Binary Outcomes with Extra Variability and Zeros

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-pscl 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-ggplot2 

%description
Inference approach for jointly modeling correlated count and binary
outcomes. This formulation allows simultaneous modeling of zero inflation
via the Bernoulli component while providing a more accurate assessment of
the Hierarchical Zero-Inflated Poisson's parsimony (Lizandra C. Fabio,
Jalmar M. F. Carrasco, Victor H. Lachos and Ming-Hui Chen,
Likelihood-based inference for joint modeling of correlated count and
binary outcomes with extra variability and zeros, 2025, under submission).

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  minimaxALT
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Optimal Designs of Accelerated Life Test using PSO-Based Algorithm

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-parallel >= 4.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 14.0.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-RcppGSL >= 0.3.13
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-parallel >= 4.0.0
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-RcppArmadillo >= 14.0.0.1
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-RcppGSL >= 0.3.13
Requires:         R-stats 
Requires:         R-graphics 

%description
A computationally efficient solution for generating optimal experimental
designs in Accelerated Life Testing (ALT). Leveraging a Particle Swarm
Optimization (PSO)-based hybrid algorithm, the package identifies optimal
test plans that minimize estimation variance under specified failure
models and stress profiles. For more detailed, see Lee et al. (2025),
Optimal Robust Strategies for Accelerated Life Tests and Fatigue Testing
of Polymer Composite Materials, submitted to Annals of Applied Statistics,
<https://imstat.org/journals-and-publications/annals-of-applied-statistics/annals-of-applied-statistics-next-issues/>,
and Hoang (2025), Model-Robust Minimax Design of Accelerated Life Tests
via PSO-based Hybrid Algorithm, Master' Thesis, Unpublished.

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

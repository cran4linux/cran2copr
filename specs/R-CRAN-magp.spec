%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  magp
%global packver   0.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mapping-Based Additive Gaussian Process Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-nloptr 
Requires:         R-parallel 
Requires:         R-stats 

%description
Fits mapping-based additive Gaussian process models for experiments in
which each component has both a quantitative level and a position in an
ordered sequence. Two model structures are available: a compact
two-dimensional mapping and a full mapping with one fewer dimension than
the number of components. Both models support parameter estimation, point
prediction, and plug-in predictive uncertainty. Input checks validate the
sequence data and apply consistent scaling to the quantitative inputs.
Computationally intensive covariance and gradient calculations are
implemented in C++ with 'Rcpp'. Initial-design functions combine a
space-filling Latin hypercube with sequence permutations. The sequence
portion can be generated randomly or optimized with simulated annealing or
space-filling threshold accepting. Expected improvement can be optimized
over both parts of the input, and a sequential interface supports Bayesian
optimization of an expensive user-supplied objective. An integrated
workflow can generate the initial design, evaluate the objective, and
continue the sequential search in one call. The model was introduced by
Xiao et al. (2024) <doi:10.1080/01621459.2022.2123335>.

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

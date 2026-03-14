%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rCausalMGM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Scalable Causal Discovery and Model Selection on Mixed Datasets with 'rCausalMGM'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-survival 

%description
Scalable methods for learning causal graphical models from mixed data,
including continuous, discrete, and censored variables. The package
implements CausalMGM, which combines a convex, score-based approach for
learning an initial moralized graph with a producer-consumer scheme that
enables efficient parallel conditional independence testing in
constraint-based causal discovery algorithms. The implementation supports
high-dimensional datasets and provides individual access to core
components of the workflow, including MGM and the PC-Stable and FCI-Stable
causal discovery algorithms. To support practical applications, the
package includes multiple model selection strategies, including
information criteria based on likelihood and model complexity,
cross-validation for out-of-sample likelihood estimation, and
stability-based approaches that assess graph robustness across subsamples.

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

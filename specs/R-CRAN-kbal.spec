%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kbal
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Balancing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 4.4.4
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-CRAN-RcppParallel >= 4.4.4
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RSpectra 

%description
Provides a weighting approach that employs kernels to make one group have
a similar distribution to another group on covariates. This method matches
not only means or marginal distributions but also higher-order
transformations implied by the choice of kernel. 'kbal' is applicable to
both treatment effect estimation and survey reweighting problems. Based on
Hazlett, C. (2020) "Kernel Balancing: A flexible non-parametric weighting
procedure for estimating causal effects." Statistica Sinica.
<https://www.researchgate.net/publication/299013953_Kernel_Balancing_A_flexible_non-parametric_weighting_procedure_for_estimating_causal_effects>.

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

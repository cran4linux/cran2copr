%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rfast
%global packver   2.1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Efficient and Extremely Fast R Functions

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-zigg 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-zigg 
Requires:         R-CRAN-RcppParallel 

%description
A collection of fast (utility) functions for data analysis. Column and row
wise means, medians, variances, minimums, maximums, many t, F and G-square
tests, many regressions (normal, logistic, Poisson), are some of the many
fast functions. References: a) Tsagris M., Papadakis M. (2018). Taking R
to its limits: 70+ tips. PeerJ Preprints 6:e26605v1
<doi:10.7287/peerj.preprints.26605v1>. b) Tsagris M. and Papadakis M.
(2018). Forward regression in R: from the extreme slow to the extreme
fast. Journal of Data Science, 16(4): 771--780.
<doi:10.6339/JDS.201810_16(4).00006>. c) Chatzipantsiou C., Dimitriadis
M., Papadakis M. and Tsagris M. (2020). Extremely Efficient Permutation
and Bootstrap Hypothesis Tests Using Hypothesis Tests Using R. Journal of
Modern Applied Statistical Methods, 18(2), eP2898.
<doi:10.48550/arXiv.1806.10947>. d) Tsagris M., Papadakis M., Alenazi A.
and Alzeley O. (2024). Computationally Efficient Outlier Detection for
High-Dimensional Data Using the MDP Algorithm. Computation, 12(9): 185.
<doi:10.3390/computation12090185>. e) Tsagris M. and Papadakis M. (2025).
Fast and light-weight energy statistics using the R package Rfast.
<doi:10.48550/arXiv.2501.02849>.

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

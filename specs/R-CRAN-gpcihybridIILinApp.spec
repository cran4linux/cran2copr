%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpcihybridIILinApp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Lindley Approximation for Capability Indices under Hybrid Censoring

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MleCensoR 
BuildRequires:    R-CRAN-gofPHCS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MleCensoR 
Requires:         R-CRAN-gofPHCS 

%description
Provides a comprehensive framework for estimating Generalized Process
Capability Indices (GPCIs) under Hybrid Type-II censored lifetime data
using Lindley's 3rd-order approximation method (Lindley, 1980
<doi:10.2307/2345271>). Supports user-supplied probability density/mass
functions (PDF/PMF), cumulative distribution functions (CDF), survival
functions (SF), and quantile functions. Computes Maximum Likelihood
Estimates (MLE) using the 'MleCensoR' package (Childs et al., 2003
<doi:10.1007/BF02517803>; Balakrishnan & Kundu, 2013
<doi:10.1002/nav.21545>) and Bayesian posterior expectations for classical
and non-normal capability indices, including Cpy (Maiti et al., 2010
<doi:10.1080/16843703.2010.11673233>), Spmk (Dey & Saha, 2019
<doi:10.1007/s41872-019-00081-4>), CpTk (Saha et al., 2019), Cpc (Saha et
al., 2022 <doi:10.1080/02664763.2021.1971632>), CNpmc (Alotaibi et al.,
2022 <doi:10.1155/2022/3135264>), CNpmkc (Saha et al., 2024
<doi:10.1142/S021853932450013X>), CNpk (Saha et al., 2018
<doi:10.1080/21681015.2018.1437793>), and Vannman's Cp(u,v) family.
Generates posterior parameter and GPCI chains via sampling with burn-in
and thinning, calculating Bias, Mean Squared Error (MSE), Bayes Risk (SEL
and Linex), Highest Posterior Density (HPD) credible intervals at 90%%,
95%%, and 99%% levels, and Heidelberger and Welch's MCMC Convergence
Diagnostics (Heidelberger & Welch, 1983 <doi:10.1287/opre.31.6.1109>) with
convergence probabilities. Evaluates parametric and non-parametric
bootstrap confidence intervals (Percentile, Normal, Basic, BCp, BCa) at
90%%, 95%%, and 99%% levels of significance. Integrates goodness-of-fit
testing for Hybrid Type-II censored data via the 'gofPHCS' package.

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

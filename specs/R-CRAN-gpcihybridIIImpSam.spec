%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpcihybridIIImpSam
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Process Capability Indices for Hybrid Type-II Data via Importance Sampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-graphics 

%description
Evaluates Generalized Process Capability Indices (GPCIs) under Hybrid
Type-II censored lifetime data using Importance Sampling (Sampling
Importance Resampling, SIR). Implements Bayesian parameter estimation and
evaluates classical and generalized capability indices including Cpy, Cp,
Cpk, Cpu, Cpl, Cpm, Cpmk, Spmk, CpTk, Cpc, CNp, CNpk, CNpm, CNpmk, CNpmc,
CNpmkc, and Vannman's Cp(u,v) family. Computes initial maximum likelihood
estimates under Hybrid Type-II censoring, parameter MCMC chains, GPCI
posterior chains, posterior point estimates, bias, mean squared error
(MSE), Bayes risk, Highest Posterior Density (HPD) credible intervals at
90%%, 95%%, and 99%% levels, Heidelberger and Welch's MCMC convergence
diagnostics, and convergence probabilities. Accommodates user-defined
probability density/mass functions, cumulative distribution functions, and
survival functions. Goodness-of-fit testing for Hybrid Type-II censored
data is supported via 'gofPHCS'. Methods are based on Childs et al. (2003)
<doi:10.1080/0266476032000053637>, Kundu and Pradhan (2009)
<doi:10.1016/j.spl.2008.09.006>, Maiti et al. (2010)
<doi:10.1080/16843703.2010.11673233>, Dey and Saha (2019)
<doi:10.1007/s41872-019-00081-4>, Alotaibi et al. (2022)
<doi:10.1155/2022/3135264>, Saha et al. (2022)
<doi:10.1080/02664763.2021.1971632>, and Saha et al. (2024)
<doi:10.1142/S021853932450013X>.

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

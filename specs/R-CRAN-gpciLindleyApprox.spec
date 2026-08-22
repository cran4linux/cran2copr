%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpciLindleyApprox
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Lindley Approximation Method for Generalized Process Capability Indices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-boot 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-boot 

%description
Provides a comprehensive framework for estimating Generalized Process
Capability Indices (GPCIs) using the Lindley approximation method for
uncensored data under Bayesian inference. Evaluates point estimates and
posterior expectations for classical and non-normal capability indices,
including Cpy (Maiti et al., 2010), Spmk (Dey & Saha, 2019), CpTk (Saha et
al., 2019), Cpc (Saha et al., 2022), CNpmc (Alotaibi et al., 2022), CNpmkc
(Saha et al., 2024), CNpk (Saha et al., 2018), and Vannman's Cp(u,v)
family. Computes parametric and non-parametric bootstrap confidence
intervals at 90%%, 95%%, and 99%% levels of significance. Supports MCMC chain
generation with burn-in and thinning, Highest Posterior Density (HPD)
intervals, Bias, MSE, Risk values, and Heidelberger and Welch's MCMC
Convergence Diagnostic with convergence probabilities. References: Lindley
(1980) <doi:10.2307/2345271>, Maiti, Saha & Nanda (2010)
<doi:10.1080/16843703.2010.11673233>, Saha, Dey & Maiti (2018)
<doi:10.1080/21681015.2018.1437793>, Dey & Saha (2019)
<doi:10.1007/s41872-019-00081-4>, Saha, Dey & Maiti (2019), Alotaibi, Dey
& Saha (2022) <doi:10.1155/2022/3135264>, Saha, Dey & Nadarajah (2022)
<doi:10.1080/02664763.2021.1971632>, Saha, Tripathi & Dey (2024)
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

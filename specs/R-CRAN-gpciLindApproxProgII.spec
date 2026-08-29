%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpciLindApproxProgII
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Lindley Approximation for Capability Indices under Progressive Censoring

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
BuildRequires:    R-CRAN-coda 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-coda 

%description
Implements Bayesian parameter and Generalized Process Capability Indices
(GPCIs) estimation using the Lindley approximation method (Lindley, 1980
<doi:10.2307/2345271>) under progressive Type-II censored data
(Balakrishnan & Aggarwala, 2000 <doi:10.1007/978-1-4612-1334-5>).
Evaluates point estimates and posterior expectations for classical and
non-normal capability indices, including Cpy (Maiti et al., 2010
<doi:10.1080/16843703.2010.11673233>), Spmk (Dey & Saha, 2019
<doi:10.1007/s41872-019-00081-4>), CpTk (Saha et al., 2019
<doi:10.1007/s13198-019-00789-7>), Cpc (Saha et al., 2022
<doi:10.1080/02664763.2021.1971632>), CNpmc (Alotaibi et al., 2022
<doi:10.1155/2022/3135264>), CNpmkc (Saha et al., 2024
<doi:10.1142/S021853932450013X>), CNpk (Saha et al., 2018
<doi:10.1080/21681015.2018.1437793>), and Vannman's Cp(u,v) family
(Vannman, 1995 <doi:10.1111/j.1467-9574.1995.tb01472.x>). Calculates point
estimates, bias, mean squared error (MSE), Bayes risk under Linex and
squared error loss, Highest Posterior Density (HPD) credible intervals at
90%%, 95%%, and 99%% levels, and Heidelberger and Welch's MCMC convergence
diagnostics (Heidelberger & Welch, 1983 <doi:10.1287/opre.31.6.1109>) with
convergence probabilities. Accommodates user-defined probability
density/mass functions, cumulative distribution functions, and survival
functions. Supports progressive parametric and non-parametric bootstrap
confidence intervals (Efron, 1987 <doi:10.1080/01621459.1987.10478410>) at
90%%, 95%%, and 99%% significance levels.

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

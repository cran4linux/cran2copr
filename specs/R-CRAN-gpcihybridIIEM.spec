%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpcihybridIIEM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Process Capability Indices via EM for Hybrid Type-II Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-UniCensorEM 
BuildRequires:    R-CRAN-gofPHCS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-UniCensorEM 
Requires:         R-CRAN-gofPHCS 

%description
Implements the Expectation-Maximization (EM) algorithm of Dempster, Laird,
and Rubin (1977) <doi:10.1111/j.2517-6161.1977.tb01600.x> for parameter
estimation under Hybrid Type-II censored data (Childs et al. (2003)
<doi:10.1007/BF02517803>; Balakrishnan and Kundu (2013)
<doi:10.1002/nav.21545>) using the 'UniCensorEM' package and computes
Generalized Process Capability Indices (GPCIs). Supports classical and
generalized capability indices including Cpy (Maiti et al. (2010)
<doi:10.1080/16843703.2010.11673233>), Cp, Cpk, Cpu, Cpl, Cpm, Cpmk, Spmk
(Dey and Saha (2019) <doi:10.1007/s41872-019-00081-4>), CpTk (Saha et al.
(2018) <doi:10.1080/21681015.2018.1437793>), Cpc, CNpmc (Alotaibi et al.
(2022) <doi:10.1155/2022/3135264>), CNpmkc (Saha et al. (2024)
<doi:10.1142/S021853932450013X>), and CNpk (Saha et al. (2022)
<doi:10.1080/02664763.2021.1971632>). Computes point estimates, bias, mean
squared error, risk, Heidelberger and Welch convergence diagnostics,
convergence probability, Bayesian MCMC sampling chains, goodness-of-fit
testing via 'gofPHCS', and bootstrap confidence intervals at 90 percent,
95 percent, and 99 percent levels. Accommodates user-defined probability
density or mass functions, cumulative distribution functions, and survival
functions.

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

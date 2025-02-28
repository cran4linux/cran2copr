%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CFO
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          CFO-Type Designs in Phase I/II Clinical Trials

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Iso 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-scales 

%description
In phase I clinical trials, the primary objective is to ascertain the
maximum tolerated dose (MTD) corresponding to a specified target toxicity
rate. The subsequent phase II trials are designed to examine the potential
efficacy of the drug based on the MTD obtained from the phase I trials,
with the aim of identifying the optimal biological dose (OBD). The 'CFO'
package facilitates the implementation of dose-finding trials by utilizing
calibration-free odds type (CFO-type) designs. Specifically, it
encompasses the calibration-free odds (CFO) (Jin and Yin (2022)
<doi:10.1177/09622802221079353>), randomized CFO (rCFO), precision CFO
(pCFO), two-dimensional CFO (2dCFO) (Wang et al. (2023)
<doi:10.3389/fonc.2023.1294258>), time-to-event CFO (TITE-CFO) (Jin and
Yin (2023) <doi:10.1002/pst.2304>), fractional CFO (fCFO), accumulative
CFO (aCFO), TITE-aCFO, and f-aCFO (Fang and Yin (2024) <doi:
10.1002/sim.10127>). It supports phase I/II trials for the CFO design and
only phase I trials for the other CFO-type designs. The ‘CFO' package
accommodates diverse CFO-type designs, allowing users to tailor the
approach based on factors such as dose information inclusion, handling of
late-onset toxicity, and the nature of the target drug (single-drug or
drug-combination). The functionalities embedded in 'CFO' package include
the determination of the dose level for the next cohort, the selection of
the MTD for a real trial, and the execution of single or multiple
simulations to obtain operating characteristics. Moreover, these functions
are equipped with early stopping and dose elimination rules to address
safety considerations. Users have the flexibility to choose different
distributions, thresholds, and cohort sizes among others for their
specific needs. The output of the 'CFO' package can be summary statistics
as well as various plots for better visualization. An interactive web
application for CFO is available at the provided URL.

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

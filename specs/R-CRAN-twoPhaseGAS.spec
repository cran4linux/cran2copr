%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  twoPhaseGAS
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Phase Genetic Association Study Design and Analysis with Missing Covariates by Design

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-kofnGA >= 1.2
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-enrichwith 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-kofnGA >= 1.2
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-enrichwith 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nloptr 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides functionality for designing and analysing two-phase genetic
association studies. Phase 1 data usually come from genome-wide
association study (GWAS) results and we assume phase 2 data will be part
of a targeted genome sequencing or fine-mapping study. At design stage,
the package assists in selecting a subset of individuals that will be
sequenced for phase 2 via alternative approaches, including a flexible
genetic algorithm (GA) for near-optimal designs. Once phase 2 data have
been collected, the package implements methods to analyse phase 1 and
phase 2 data together using semi-parametric regression models via the
expectation-maximization (EM) algorithm. For more details see
Espin-Garcia, Craiu and Bull (2018) <doi:10.1002/gepi.22099> and
Espin-Garcia, Craiu and Bull (2021) <doi:10.1002/sim.9211>.

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

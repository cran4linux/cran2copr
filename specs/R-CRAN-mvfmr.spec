%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mvfmr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Multivariable Mendelian Randomization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-fdapace 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-fdapace 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-gridExtra 
Requires:         R-stats 

%description
Implements Multivariable Functional Mendelian Randomization (MV-FMR) to
estimate time-varying causal effects of multiple longitudinal exposures on
health outcomes. Extends univariable functional Mendelian Randomisation
(MR) (Tian et al., 2024 <doi:10.1002/sim.10222>) to the multivariable
setting, enabling joint estimation of multiple time-varying exposures with
pleiotropy and mediation scenarios. Key features include: (1) data-driven
cross-validation for basis component selection, (2) handling of mediation
pathways between exposures, (3) support for both continuous and binary
outcomes using Generalized Method of Moments (GMM) and control function
approaches, (4) one-sample and two-sample MR designs, (5) bootstrap
inference and instrument diagnostics including Q-statistics for
overidentification testing. Methods are described in Fontana et al. (2025)
<doi:10.48550/arXiv.2512.19064>.

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

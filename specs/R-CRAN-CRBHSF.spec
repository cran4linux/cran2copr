%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CRBHSF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cyber-Resilient Bayesian Healthcare Surveillance Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 

%description
Provides methods for healthcare performance surveillance using Bayesian
risk estimation, latent organisational trust modelling, cyber-resilience
assessment, external validation, decision-theoretic optimisation, and
digital-twin deployment simulation. The package supports prospective
deterioration monitoring, uncertainty-aware risk assessment, intervention
prioritisation, ablation analysis, and operational evaluation for
healthcare performance management and health system resilience research.
The methodological framework is informed by contemporary guidance on
prediction model development and validation (Efthimiou et al., 2024
<doi:10.1136/bmj-2023-078276>), transparent reporting of prediction models
(Collins et al., 2024 <doi:10.1136/bmj-2023-078378>), and
decision-analytic model evaluation (Vickers and Elkin, 2006
<doi:10.1177/0272989X06295361>).

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

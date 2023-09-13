%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlpsem
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Linear and Nonlinear Longitudinal Process in Structural Equation Modeling Framework

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-OpenMx >= 2.21.8
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-methods 
Requires:         R-CRAN-OpenMx >= 2.21.8
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-readr 
Requires:         R-methods 

%description
Provides computational tools for nonlinear longitudinal models, in
particular the intrinsically nonlinear models, in four scenarios: (1)
univariate longitudinal processes with growth factors, with or without
covariates including time-invariant covariates (TICs) and time-varying
covariates (TVCs); (2) multivariate longitudinal processes that facilitate
the assessment of correlation or causation between multiple longitudinal
variables; (3) multiple-group models for scenarios (1) and (2) to evaluate
differences among manifested groups, and (4) longitudinal mixture models
for scenarios (1) and (2), with an assumption that trajectories are from
multiple latent classes. The methods implemented are introduced in Jin Liu
(2023) <arXiv:2302.03237v2>.

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

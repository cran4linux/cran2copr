%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LongDecompHE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Longitudinal Decomposition of Health Expectancy by Age and Cause

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-corpcor 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-grDevices 
Requires:         R-CRAN-tidyr 

%description
Provides tools to decompose differences in cohort health expectancy (HE)
by age and cause using longitudinal data. The package implements a novel
longitudinal attribution method based on a semiparametric additive hazards
model with time-dependent covariates, specifically designed to address
interval censoring and semi-competing risks via a copula framework. The
resulting age-cause-specific contributions to disability prevalence and
death probability can be used to quantify and decompose differences in
cohort HE between groups. The package supports stepwise replacement
decomposition algorithms and is applicable to cohort-based health
disparity research across diverse populations. Related methods include Sun
et al. (2023) <doi:10.1177/09622802221133552>.

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

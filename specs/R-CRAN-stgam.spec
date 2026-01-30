%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stgam
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatially and Temporally Varying Coefficient Models Using Generalized Additive Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv >= 1.9.1
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-mgcv >= 1.9.1
Requires:         R-CRAN-glue 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 

%description
A framework for undertaking space and time varying coefficient models
(varying parameter models) using a Generalized Additive Model (GAM) with
smooths approach. The framework suggests the need to investigate for the
presence and nature of any space-time dependencies in the data. It
proposes a workflow that creates and refines an initial space-time GAM and
includes tools to create and evaluate multiple model forms. The workflow
sequence is to: i) Prepare the data by lengthening it to have a single
location and time variables for each observation. ii) Create all possible
space and/or time models in which each predictor is specified in different
ways in smooths. iii) Evaluate each model via their AIC value and pick the
best one. iv) Create the final model. v) Calculate the varying coefficient
estimates to quantify how the relationships between the target and
predictor variables vary over space, time or space-time. vi) Create maps,
time series plots etc. The number of knots used in each smooth can be
specified directly or iteratively increased. This is illustrated with a
climate point dataset of the dry rain forest in South America. This builds
on work in Comber et al (2024) <doi:10.1080/13658816.2023.2270285> and
Comber et al (2004) <doi:10.3390/ijgi13120459>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jmSurface
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Parametric Association Surfaces for Joint Longitudinal-Survival Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Implements interpretable multi-biomarker fusion in joint
longitudinal-survival models via semi-parametric association surfaces.
Provides a two-stage estimation framework where Stage 1 fits mixed-effects
longitudinal models and extracts Best Linear Unbiased Predictors
('BLUP's), and Stage 2 fits transition-specific penalized Cox models with
tensor-product spline surfaces linking latent biomarker summaries to
transition hazards. Supports multi-state disease processes with
transition-specific surfaces, Restricted Maximum Likelihood ('REML')
smoothing parameter selection, effective degrees of freedom ('EDF')
diagnostics, dynamic prediction of transition probabilities, and three
interpretability visualizations (surface plots, contour heatmaps, marginal
effect slices). Methods are described in Bhattacharjee (2025, under
review).

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

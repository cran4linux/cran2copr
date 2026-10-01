%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecoGLMM
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Ecological Generalized Linear Mixed Model Pipelines

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DHARMa 
BuildRequires:    R-CRAN-ggeffects 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-DHARMa 
Requires:         R-CRAN-ggeffects 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmmTMB 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-performance 
Requires:         R-stats 
Requires:         R-CRAN-writexl 

%description
Fits and compares generalized linear mixed models for multiple ecological
responses and environmental predictors. The package supports additive and
temporal-interaction candidate models, AICc model selection,
likelihood-ratio tests, coefficient extraction, Nakagawa R-squared,
simulation-based diagnostics, figures, and spreadsheet exports. Model
selection follows Burnham and Anderson (2002, ISBN:9780387953649);
marginal and conditional R-squared follow Nakagawa and Schielzeth (2013)
<doi:10.1111/j.2041-210x.2012.00261.x>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NonlinearDiD
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Staggered Difference-in-Differences with Nonlinear Outcomes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-ggplot2 

%description
Supports staggered difference-in-differences designs with nonlinear
outcomes for both panel and repeated cross-section data. Implements
estimators for staggered treatment adoption with binary, count, and other
nonlinear outcomes, extending Callaway and Sant'Anna (2021)
<doi:10.1016/j.jeconom.2020.12.001> to settings with nonlinear outcome
models such as logit, probit, and Poisson. For panel data, units are
followed over time and 'idname' identifies repeated observations. For
repeated cross-section data, observations are independent within each time
period; 'idname' is optional and may identify survey records or
households, but the estimator does not require the same units to appear
across periods. Repeated cross-section estimation includes pooled
quasi-maximum likelihood approaches motivated by Wooldridge (2023)
<doi:10.1093/ectj/utad016>, with optional weighting and clustered
inference. Methods also draw on Roth and Sant'Anna (2023)
<doi:10.3982/ECTA19402> and Sant'Anna and Zhao (2020)
<doi:10.1016/j.jeconom.2020.06.003>.

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

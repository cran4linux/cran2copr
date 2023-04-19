%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  InteractionPoweR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analyses for Interaction Effects in Cross-Sectional Regressions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-chngpt 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggbeeswarm 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-chngpt 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-ggbeeswarm 
Requires:         R-CRAN-Matrix 

%description
Power analysis for regression models which test the interaction of two
independent variables on a single dependent variable. Includes options for
continuous, binary, or ordinal variables, as well as correlated
interacting variables. Also includes options to specify variable
reliability. Power analyses can be done either analytically or via
simulation.  Includes tools for simulating single data sets and
visualizing power analysis results. The primary functions are
power_interaction_r2() and power_interaction(). Please cite as: Baranger
DAA, Finsaas MC, Goldstein BL, Vize CE, Lynam DR, Olino TM (2022).
"Tutorial: Power analyses for interaction effects in cross-sectional
regressions." <doi:10.31234/osf.io/5ptd7>.

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

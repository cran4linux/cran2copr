%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SRMERS
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Parametric Shape-Restricted Fixed/Mixed Effect(s) Regression Spline

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-coneproj 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-splines2 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-coneproj 
Requires:         R-CRAN-Matrix 

%description
Select the most suitable shape to describe the relationship between the
exposure and the outcome among increasing, decreasing, convex, and concave
shapes (Yin et al. (2021) <DOI:10.1007/s13571-020-00246-7>); estimate the
direct and indirect effects with prior knowledge on the relationship
between the mediator and the outcome with binary exposure (Yin et al.
(2024) <DOI:10.1007/s13571-024-00336-w>); estimate the direct and indirect
effects using linear regression-based approach (VanderWeele (2015,
ISBN:9780199325870)).

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

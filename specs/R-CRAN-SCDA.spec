%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SCDA
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatially-Clustered Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatialreg 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-spatialreg 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spdep 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-performance 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 

%description
Contains functions for statistical data analysis based on
spatially-clustered techniques. The package allows estimating the
spatially-clustered spatial regression models presented in Cerqueti,
Maranzano & Mattera (2024), "Spatially-clustered spatial autoregressive
models with application to agricultural market concentration in Europe",
arXiv preprint 2407.15874 <doi:10.48550/arXiv.2407.15874>. Specifically,
the current release allows the estimation of the spatially-clustered
linear regression model (SCLM), the spatially-clustered spatial
autoregressive model (SCSAR), the spatially-clustered spatial Durbin model
(SCSEM), and the spatially-clustered linear regression model with
spatially-lagged exogenous covariates (SCSLX).

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

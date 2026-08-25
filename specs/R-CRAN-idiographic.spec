%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  idiographic
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Person-Specific (Idiographic) and Heterogeneous Complex Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 

%description
Person-specific and within-person network estimation from intensive
longitudinal and panel data. Estimators include ordinary vector
autoregression (VAR), graphical vector autoregression (graphical VAR),
multilevel vector autoregression (mlVAR), rolling ordinary and graphical
VAR, native Bayesian VAR and multilevel Bayesian VAR, unified Structural
Equation Modeling (uSEM), and Group Iterative Multiple Model Estimation
(GIMME). All estimators are native clean-room implementations. All
functions are validated against authoritative literature. Also provides
preprocessing audits, edge-stability diagnostics, model-comparison
reports, and rolling forecast validation. Methods are described in
<doi:10.1007/978-3-031-95365-1_20> and
<doi:10.1080/00273171.2018.1454823>.

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

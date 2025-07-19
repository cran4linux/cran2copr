%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdhte
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Heterogeneous Treatment Effects in Regression Discontinuity Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rdrobust 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-multcomp 
Requires:         R-CRAN-rdrobust 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-multcomp 

%description
Understanding heterogeneous causal effects based on pretreatment
covariates is a crucial step in modern empirical work in data science.
Building on the recent developments in Calonico et al (2025)
<https://rdpackages.github.io/references/Calonico-Cattaneo-Farrell-Palomba-Titiunik_2025_HTERD.pdf>,
this package provides tools for estimation and inference of heterogeneous
treatment effects in Regression Discontinuity (RD) Designs. The package
includes two main commands: 'rdhte' to conduct estimation and robust
bias-corrected inference for conditional RD treatment effects (given
choice of bandwidth parameter); 'rdbwhte', which implements automatic
bandwidth selection methods; and 'rdhte_lincom' to test linear
combinations of parameters.

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

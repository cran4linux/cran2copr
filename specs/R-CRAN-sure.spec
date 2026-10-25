%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sure
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Surrogate Residuals for Ordinal and General Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
An implementation of the surrogate approach to residuals and diagnostics
for ordinal and general regression models; for details, see Liu and Zhang
(2018) <doi:10.1080/01621459.2017.1292915> and Greenwell et al. (2018)
<doi:10.32614/RJ-2018-004>. These residuals can be used to construct
standard residual plots for model diagnostics (e.g., residual-vs-fitted
value plots, residual-vs-covariate plots, Q-Q plots, etc.). The package
also provides 'plot' methods for producing standard diagnostic plots using
lightweight base R graphics (via 'tinyplot'). The package currently
supports cumulative link models from packages 'MASS', 'ordinal', 'rms',
and 'VGAM', binary and other generalized linear models fit with 'glm', and
multinomial models or general classifiers via a matrix of predicted class
probabilities.

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

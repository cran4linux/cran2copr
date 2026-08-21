%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MLMES
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Based Effect Sizes for Multilevel Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.6.5
BuildRequires:    R-CRAN-lme4 >= 1.1.34
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-Matrix >= 1.6.5
Requires:         R-CRAN-lme4 >= 1.1.34
Requires:         R-CRAN-dplyr 
Requires:         R-stats 

%description
Computes model-based effect sizes for fixed-effect coefficients in
multilevel (hierarchical) models. The coefficient effect sizes are
standardized mean differences from zero (d) and unique variance-explained
measures (squared semi-partial correlations, sr2). The package also
reports variance components and level-specific and total R-squared values.
It supports 2-level and 3-level linear and binary logistic models fitted
with 'lme4' (Bates et al., 2015) <doi:10.18637/jss.v067.i01>, and 2-level
Gaussian and Bernoulli models fitted with 'brms' (Bürkner, 2017)
<doi:10.18637/jss.v080.i01>. Sanders, Konold, and Cheng (in press),
"Model-based effect sizes for multilevel linear regression coefficients,"
Methodology: European Journal of Research Methods for the Behavioral and
Social Sciences, describe the 2-level linear-model methods.

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

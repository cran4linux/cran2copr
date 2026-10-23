%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  twoPhaseSens
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis for Covariates Observed in Two-Phase Samples

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtsummary >= 2.0.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jomo 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-gtsummary >= 2.0.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jomo 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 

%description
Provides a structured method-comparison sensitivity-analysis workflow for
linear regression when important continuous adjustment covariates are
observed only in a Phase-2 subsample. Implements naive analysis,
complete-case analysis, fully conditional specification multiple
imputation, joint-model multiple imputation, inverse probability
weighting, and augmented inverse probability weighting, with standardized
tables, diagnostics, and publication-style forest plots. Methodological
background is provided by Little and Rubin (2019)
<doi:10.1002/9781119482260> for general missing-data methods, White and
Carlin (2010) <doi:10.1002/sim.3944> for complete-case analysis with
missing covariates, White, Royston and Wood (2011) <doi:10.1002/sim.4067>
and van Buuren and Groothuis-Oudshoorn (2011) <doi:10.18637/jss.v045.i03>
for chained-equations multiple imputation, Quartagno, Grund and Carpenter
(2019) <doi:10.32614/RJ-2019-028> for joint-model multiple imputation,
Robins, Rotnitzky and Zhao (1994) <doi:10.1080/01621459.1994.10476818> for
inverse-probability weighting with missing regressors, and Bang and Robins
(2005) <doi:10.1111/j.1541-0420.2005.00377.x> for doubly robust
estimation.

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

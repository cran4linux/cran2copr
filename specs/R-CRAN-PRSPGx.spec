%global __brp_check_rpaths %{nil}
%global packname  PRSPGx
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Construct PGx PRS

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 4.0.2
BuildRequires:    R-methods >= 3.6.3
BuildRequires:    R-CRAN-Rfast >= 1.9.9
BuildRequires:    R-CRAN-bigsnpr >= 1.5.2
BuildRequires:    R-CRAN-gglasso >= 1.5
BuildRequires:    R-CRAN-MCMCpack >= 1.4.6
BuildRequires:    R-CRAN-bdsmatrix >= 1.3.4
BuildRequires:    R-CRAN-SGL >= 1.3
BuildRequires:    R-CRAN-bigstatsr >= 1.2.3
BuildRequires:    R-CRAN-Matrix >= 1.2.18
BuildRequires:    R-CRAN-mvtnorm >= 1.1.0
BuildRequires:    R-CRAN-propagate >= 1.0.6
BuildRequires:    R-CRAN-matrixcalc >= 1.0.3
BuildRequires:    R-CRAN-lmtest >= 0.9.37
BuildRequires:    R-CRAN-GIGrvg >= 0.5
BuildRequires:    R-CRAN-bigsparser >= 0.4.0
BuildRequires:    R-CRAN-bigparallelr >= 0.2.3
Requires:         R-CRAN-glmnet >= 4.0.2
Requires:         R-methods >= 3.6.3
Requires:         R-CRAN-Rfast >= 1.9.9
Requires:         R-CRAN-bigsnpr >= 1.5.2
Requires:         R-CRAN-gglasso >= 1.5
Requires:         R-CRAN-MCMCpack >= 1.4.6
Requires:         R-CRAN-bdsmatrix >= 1.3.4
Requires:         R-CRAN-SGL >= 1.3
Requires:         R-CRAN-bigstatsr >= 1.2.3
Requires:         R-CRAN-Matrix >= 1.2.18
Requires:         R-CRAN-mvtnorm >= 1.1.0
Requires:         R-CRAN-propagate >= 1.0.6
Requires:         R-CRAN-matrixcalc >= 1.0.3
Requires:         R-CRAN-lmtest >= 0.9.37
Requires:         R-CRAN-GIGrvg >= 0.5
Requires:         R-CRAN-bigsparser >= 0.4.0
Requires:         R-CRAN-bigparallelr >= 0.2.3

%description
Construct pharmacogenomics (PGx) polygenic risk score (PRS) with
PRS-PGx-Unadj (unadjusted), PRS-PGx-CT (clumping and thresholding),
PRS-PGx-L, -GL, -SGL (penalized regression), PRS-PGx-Bayes (Bayesian
regression). Package is based on ''Pharmacogenomics Polyenic Risk Score
for Drug Response Prediction Using PRS-PGx Methods'' by Zhai, S., Zhang,
H., Mehrotra, D.V., and Shen, J., 2021 (submitted).

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

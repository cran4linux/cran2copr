%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rocvb
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          ROC-Based Inference for Diagnostic Accuracy Under Verification Bias

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-emplik 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-stats 
Requires:         R-CRAN-emplik 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pROC 
Requires:         R-stats 

%description
Provides point estimates and confidence intervals for receiver operating
characteristic (ROC)–based diagnostic accuracy metrics for tests and
biomarkers subject to verification bias. Supported metrics include the
Area Under the ROC Curve (AUC), the Youden index, and the sensitivity at a
user‑specified specificity level for two‑class continuous tests under
missing‑at‑random (MAR) disease verification. Point estimation follows
Alonzo and Pepe (2005) <doi:10.1111/j.1467-9876.2005.00477.x>. Multiple
types of confidence intervals are implemented and compared, including
bootstrap‑based, Method of Variance Estimates Recovery (MOVER)–based, and
empirical likelihood (EL)–based intervals; see Wang et al. (2025)
<doi:10.1177/09622802251322989> and <https://github.com/swang1021/rocvb>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Usmile
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Threshold-Free Class-Specific Comparison of Binary Classifiers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-pROC 

%description
Implements the U-smile methodology for threshold-free, class-specific
comparison of probabilistic binary classifiers. The package quantifies
prediction improvement and worsening separately for non-events and events
using the Brier alteration (BA), relative Brier (RB), improvement
proportion (I) coefficients, and relative likelihood ratio (rLR)
coefficients, and provides U-smile, prediction improvement-worsening,
receiver operating characteristic, and precision-recall plots. The
original U-smile framework is described in Kubiak et al. (2024)
<doi:10.1371/journal.pone.0303276>, its three-level extension for
imbalanced binary classification in Wieckowska et al. (2025)
<doi:10.1371/journal.pone.0321661>, and the likelihood-based extension in
Wieckowska and Guzik (2026) <doi:10.1038/s41598-026-40545-z>.

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

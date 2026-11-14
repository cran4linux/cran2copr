%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  imbalanceKit
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Resampling Methods and Tools for Imbalanced Classification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-Rfast 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-Rfast 

%description
A collection of resampling methods for class imbalance in classification
problems. Includes the oversampling methods SMOTE with boosting (SMOTEWB)
by F. Sağlam and M. A. Cengiz (2022) <doi:10.1016/j.eswa.2022.117023>,
Markov chain SMOTE (MCSMOTE) by F. Sağlam and M. A. Cengiz (2025)
<doi:10.1016/j.asoc.2025.113906>, uncertainty guided oversampling (UGO) by
F. Sağlam and M. A. Cengiz (2026) <doi:10.1016/j.knosys.2026.115886>, and
bi-directional SMOTE (BiSMOTE) by F. Sağlam and U. Yamak (2027)
<doi:10.1016/j.eswa.2026.134648>, and the data relocation approach DatRel
by F. Sağlam (2025) <doi:10.1007/s10994-025-06755-8>, together with
commonly used alternatives such as SMOTE, ADASYN, Borderline-SMOTE,
Safe-Level-SMOTE, geometric SMOTE, random oversampling and undersampling.
The methods share the same interface: they take a feature matrix and a
factor class variable and return the resampled data together with the
synthetic samples.

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

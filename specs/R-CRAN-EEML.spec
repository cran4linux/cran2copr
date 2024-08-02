%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EEML
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ensemble Explainable Machine Learning Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MCS 
BuildRequires:    R-CRAN-WeightedEnsemble 
BuildRequires:    R-CRAN-topsis 
Requires:         R-stats 
Requires:         R-CRAN-MCS 
Requires:         R-CRAN-WeightedEnsemble 
Requires:         R-CRAN-topsis 

%description
We introduced a novel ensemble-based explainable machine learning model
using Model Confidence Set (MCS) and two stage Technique for Order of
Preference by Similarity to Ideal Solution (TOPSIS) algorithm. The model
combined the predictive capabilities of different machine-learning models
and integrates the interpretability of explainability methods. To develop
the proposed algorithm, a two-stage Technique for Order of Preference by
Similarity to Ideal Solution (TOPSIS) framework was employed. The package
has been developed using the algorithm of Paul et al. (2023)
<doi:10.1007/s40009-023-01218-x> and Yeasin and Paul (2024)
<doi:10.1007/s11227-023-05542-3>.

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

%global __brp_check_rpaths %{nil}
%global packname  Allspice
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          RNA-Seq Profile Classifier

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
We developed a lightweight machine learning tool for RNA profiling of
acute lymphoblastic leukemia (ALL), however, it can be used for any
problem where multiple classes need to be identified from
multi-dimensional data. The methodology is described in Makinen V-P, Rehn
J, Breen J, Yeung D, White DL (2022) Multi-cohort transcriptomic subtyping
of B-cell acute lymphoblastic leukemia, medRxiv,
<doi:10.1101/2022.02.17.22270919>. The classifier contains optimized mean
profiles of the classes (centroids) as observed in the training data, and
new samples are matched to these centroids using the shortest Euclidean
distance. Centroids derived from a dataset of 1,598 ALL patients are
included, but users can train the models with their own data as well. The
output includes both numerical and visual presentations of the
classification results. Samples with mixed features from multiple classes
or atypical values are also identified.

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

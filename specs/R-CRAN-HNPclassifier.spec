%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HNPclassifier
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Neyman-Pearson Classification for Ordered Classes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-randomForest 

%description
The Hierarchical Neyman-Pearson (H-NP) classification framework extends
the Neyman-Pearson classification paradigm to multi-class settings where
classes have a natural priority ordering. This is particularly useful for
classification in unbalanced dataset, for example, disease severity
classification, where under-classification errors (misclassifying patients
into less severe categories) are more consequential than other
misclassifications. The package implements H-NP umbrella algorithms that
controls under-classification errors under user specified control levels
with high probability. It supports the creation of H-NP classifiers using
scoring functions based on built-in classification methods (including
logistic regression, support vector machines, and random forests), as well
as user-trained scoring functions. For theoretical details, please refer
to Lijia Wang, Y. X. Rachel Wang, Jingyi Jessica Li & Xin Tong (2024)
<doi:10.1080/01621459.2023.2270657>.

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

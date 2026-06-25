%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blockwise
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Reduced Modeling for Tabular Data with Blockwise Missingness

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VIM 
BuildRequires:    R-CRAN-withr 
Requires:         R-stats 
Requires:         R-CRAN-VIM 
Requires:         R-CRAN-withr 

%description
Supervised learning on tabular data with blockwise missing patterns, using
the Blockwise Reduced Modeling (BRM) method of Srinivasan, Currim, and Ram
(2025) <doi:10.1287/ijds.2022.9016>. BRM partitions the training data into
overlapping subsets based on per-row feature-missing patterns, fits one
user-supplied learner per subset with minimal imputation, and at
prediction time routes each test instance to the best-matching subset
model. The interface is learner-agnostic: any fit-and-predict pair can be
plugged in, and convenience specifications are provided for linear models,
tree models, random forests, and gradient boosting.

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

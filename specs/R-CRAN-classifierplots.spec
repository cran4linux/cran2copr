%global packname  classifierplots
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generates a Visualization of Classifier Performance as a Grid of Diagnostic Plots

License:          BSD 3-clause License + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-gridExtra >= 2.2
BuildRequires:    R-CRAN-data.table >= 1.10
BuildRequires:    R-CRAN-Rcpp >= 0.12
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-gridExtra >= 2.2
Requires:         R-CRAN-data.table >= 1.10
Requires:         R-CRAN-Rcpp >= 0.12
Requires:         R-grid 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-caret 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-png 

%description
Generates a visualization of binary classifier performance as a grid of
diagnostic plots with just one function call. Includes ROC curves,
prediction density, accuracy, precision, recall and calibration plots, all
using ggplot2 for easy modification. Debug your binary classifiers faster
and easier!

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

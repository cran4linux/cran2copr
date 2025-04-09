%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spect
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survival Prediction Ensemble Classification Tool

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-riskRegression 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-caretEnsemble 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-riskRegression 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-caretEnsemble 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rlang 

%description
A tool for survival analysis using a discrete time approach with ensemble
binary classification. 'spect' provides a simple interface consistent with
commonly used R data analysis packages, such as 'caret', a variety of
parameter options to help facilitate search automation, a high degree of
transparency to the end-user - all intermediate data sets and parameters
are made available for further analysis and useful, out-of-the-box
visualizations of model performance. Methods for transforming survival
data into discrete-time are adapted from the 'autosurv' package by Suresh
et al., (2022) <doi:10.1186/s12874-022-01679-6>.

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

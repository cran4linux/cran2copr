%global __brp_check_rpaths %{nil}
%global packname  QWDAP
%global packver   1.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Quantum Walk-Based Data Analysis and Prediction

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-StepReg 
BuildRequires:    R-CRAN-MTS 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-CORElearn 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-StepReg 
Requires:         R-CRAN-MTS 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-CORElearn 

%description
Modeling and predicting time series based on continuous time quantum.This
package can be divided into three parts: Basis Generation, Data Modeling
and Prediction, and Model Evaluation according to the analysis process of
time series. 'Basis Generation' has realized the continuous time quantum
walk simulation for generating modes as the basis. Some regression methods
are used to model the observed time series and predict in 'Data Modeling
and Prediction', and 'Model Evaluation' can be used to evaluate the data
correspondence between two series.

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

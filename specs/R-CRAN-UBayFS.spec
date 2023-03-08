%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UBayFS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A User-Guided Bayesian Framework for Ensemble Feature Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DirichletReg 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-hyper2 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mRMRe 
BuildRequires:    R-CRAN-Rdimtools 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
Requires:         R-CRAN-DirichletReg 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-hyper2 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-mRMRe 
Requires:         R-CRAN-Rdimtools 
Requires:         R-CRAN-shiny 
Requires:         R-utils 

%description
The framework proposed in Jenul et al., (2022)
<doi:10.1007/s10994-022-06221-9>, together with an interactive Shiny
dashboard. 'UBayFS' is an ensemble feature selection technique embedded in
a Bayesian statistical framework. The method combines data and user
knowledge, where the first is extracted via data-driven ensemble feature
selection. The user can control the feature selection by assigning prior
weights to features and penalizing specific feature combinations. 'UBayFS'
can be used for common feature selection as well as block feature
selection.

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

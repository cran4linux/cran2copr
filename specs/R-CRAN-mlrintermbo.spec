%global __brp_check_rpaths %{nil}
%global packname  mlrintermbo
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Based Optimization for 'mlr3' Through 'mlrMBO'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr3misc >= 0.1.4
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-bbotk 
BuildRequires:    R-CRAN-mlr3tuning 
Requires:         R-CRAN-mlr3misc >= 0.1.4
Requires:         R-CRAN-backports 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-bbotk 
Requires:         R-CRAN-mlr3tuning 

%description
The 'mlrMBO' package can ordinarily not be used for optimization within
'mlr3', because of incompatibilities of their respective class systems.
'mlrintermbo' offers a compatibility interface that provides 'mlrMBO' as
an 'mlr3tuning' 'Tuner' object, for tuning of machine learning algorithms
within 'mlr3', as well as a 'bbotk' 'Optimizer' object for optimization of
general objective functions using the 'bbotk' black box optimization
framework. The control parameters of 'mlrMBO' are faithfully reproduced as
a 'paradox' 'ParamSet'.

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

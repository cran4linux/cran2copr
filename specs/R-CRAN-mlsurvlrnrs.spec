%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlsurvlrnrs
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          R6-Based ML Survival Learners for 'mlexperiments'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-kdry 
BuildRequires:    R-CRAN-mlexperiments 
BuildRequires:    R-CRAN-mllrnrs 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-kdry 
Requires:         R-CRAN-mlexperiments 
Requires:         R-CRAN-mllrnrs 
Requires:         R-CRAN-R6 
Requires:         R-stats 

%description
Enhances 'mlexperiments'
<https://CRAN.R-project.org/package=mlexperiments> with additional machine
learning ('ML') learners for survival analysis. The package provides
R6-based survival learners for the following algorithms: 'glmnet'
<https://CRAN.R-project.org/package=glmnet>, 'ranger'
<https://CRAN.R-project.org/package=ranger>, 'xgboost'
<https://CRAN.R-project.org/package=xgboost>, and 'rpart'
<https://CRAN.R-project.org/package=rpart>. These can be used directly
with the 'mlexperiments' R package.

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

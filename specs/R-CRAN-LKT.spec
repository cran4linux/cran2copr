%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LKT
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Logistic Knowledge Tracing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 4.0.2
BuildRequires:    R-CRAN-LiblineaR >= 2.10.8
BuildRequires:    R-CRAN-cluster >= 2.1.3
BuildRequires:    R-CRAN-SparseM >= 1.83
BuildRequires:    R-CRAN-pROC >= 1.16.2
BuildRequires:    R-CRAN-data.table >= 1.13.2
BuildRequires:    R-CRAN-glmnetUtils >= 1.1.8
BuildRequires:    R-CRAN-lme4 >= 1.1.23
BuildRequires:    R-CRAN-HDInterval >= 0.2.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-glmnet >= 4.0.2
Requires:         R-CRAN-LiblineaR >= 2.10.8
Requires:         R-CRAN-cluster >= 2.1.3
Requires:         R-CRAN-SparseM >= 1.83
Requires:         R-CRAN-pROC >= 1.16.2
Requires:         R-CRAN-data.table >= 1.13.2
Requires:         R-CRAN-glmnetUtils >= 1.1.8
Requires:         R-CRAN-lme4 >= 1.1.23
Requires:         R-CRAN-HDInterval >= 0.2.2
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-crayon 

%description
Computes Logistic Knowledge Tracing ('LKT') which is a general method for
tracking human learning in an educational software system. Please see
Pavlik, Eglington, and Harrel-Williams (2021)
<https://ieeexplore.ieee.org/document/9616435>. 'LKT' is a method to
compute features of student data that are used as predictors of subsequent
performance. 'LKT' allows great flexibility in the choice of predictive
components and features computed for these predictive components. The
system is built on top of 'LiblineaR', which enables extremely fast
solutions compared to base glm() in R.

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

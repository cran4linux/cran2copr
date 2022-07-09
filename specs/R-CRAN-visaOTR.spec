%global __brp_check_rpaths %{nil}
%global packname  visaOTR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Valid Improved Sparsity A-Learning for Optimal Treatment Decision

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-randomForest 
Requires:         R-stats 
Requires:         R-CRAN-xgboost 

%description
Valid Improved Sparsity A-Learning (VISA) provides a new method for
selecting important variables involved in optimal treatment regime from a
multiply robust perspective. The VISA estimator achieves its success by
borrowing the strengths of both model averaging (ARM, Yuhong Yang, 2001)
<doi:10.1198/016214501753168262> and variable selection (PAL, Chengchun
Shi, Ailin Fan, Rui Song and Wenbin Lu, 2018) <doi:10.1214/17-AOS1570>.
The package is an implementation of Zishu Zhan and Jingxiao Zhang.
(2022+).

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

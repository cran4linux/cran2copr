%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  srlars
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Scalable Cellwise-Robust Ensemble

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cellWise 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-mvnfast 
Requires:         R-CRAN-cellWise 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-mvnfast 

%description
Functions to perform robust variable selection and regression using the
Fast and Scalable Cellwise-Robust Ensemble (FSCRE) algorithm. The approach
establishes a robust foundation using the Detect Deviating Cells (DDC)
algorithm and robust correlation estimates. It then employs a competitive
ensemble architecture where a robust Least Angle Regression (LARS) engine
proposes candidate variables and cross-validation arbitrates their
assignment. A final robust MM-estimator is applied to the selected
predictors.

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

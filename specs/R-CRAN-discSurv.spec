%global __brp_check_rpaths %{nil}
%global packname  discSurv
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Time Survival Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-treeClust 
BuildRequires:    R-CRAN-functional 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-mvnfast 
Requires:         R-CRAN-treeClust 
Requires:         R-CRAN-functional 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-mvnfast 

%description
Provides data transformations, estimation utilities, predictive evaluation
measures and simulation functions for discrete time survival analysis.

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

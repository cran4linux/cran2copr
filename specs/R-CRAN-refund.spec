%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  refund
%global packver   0.1-38
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.38
Release:          1%{?dist}%{?buildtag}
Summary:          Regression with Functional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv >= 1.9
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-gamm4 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-RLRsim 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pbs 
BuildRequires:    R-methods 
Requires:         R-CRAN-mgcv >= 1.9
Requires:         R-CRAN-fda 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-gamm4 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-RLRsim 
Requires:         R-splines 
Requires:         R-CRAN-grpreg 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-pbs 
Requires:         R-methods 

%description
Methods for regression for functional data, including function-on-scalar,
scalar-on-function, and function-on-function regression. Some of the
functions are applicable to image data.

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

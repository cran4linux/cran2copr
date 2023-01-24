%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fsemipar
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation, Variable Selection and Prediction for Functional Semiparametric Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-splines 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-grpreg 
Requires:         R-CRAN-DiceKriging 
Requires:         R-graphics 
Requires:         R-stats 

%description
Routines for estimation or simultaneous estimation and variable selection
of several functional semiparametric models with scalar response, such as
the functional single-index model, the semi-functional partial linear
model or the semi-functional partial linear single-index model. In
addition, it includes algorithms for dealing with scalar covariates with
linear effect coming from the discretization of a curve in the cases of
the linear model, the multi-functional partial linear model and the
multi-functional partial linear single-index model.

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

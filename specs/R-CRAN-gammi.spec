%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gammi
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Additive Mixed Model Interface

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 

%description
An interface for fitting generalized additive models (GAMs) and
generalized additive mixed models (GAMMs) using the 'lme4' package as the
computational engine, as described in Helwig (2024)
<doi:10.3390/stats7010003>. Supports default and formula methods for model
specification, additive and tensor product splines for capturing nonlinear
effects, and automatic determination of spline type based on the class of
each predictor. Includes an S3 plot method for visualizing the (nonlinear)
model terms, an S3 predict method for forming predictions from a fit
model, and an S3 summary method for conducting significance testing using
the Bayesian interpretation of a smoothing spline.

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

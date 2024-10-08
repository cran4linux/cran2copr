%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MLEcens
%global packver   0.1-7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of the MLE for Bivariate Interval Censored Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10

%description
We provide functions to compute the nonparametric maximum likelihood
estimator (MLE) for the bivariate distribution of (X,Y), when realizations
of (X,Y) cannot be observed directly. To be more precise, we consider the
situation where we observe a set of rectangles in R^2 that are known to
contain the unobservable realizations of (X,Y). We compute the MLE based
on such a set of rectangles. The methods can also be used for univariate
censored data (see data set 'cosmesis'), and for censored data with
competing risks (see data set 'menopause'). We also provide functions to
visualize the observed data and the MLE.

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

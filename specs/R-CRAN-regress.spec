%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  regress
%global packver   1.3-22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.22
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Linear Models with Linear Covariance Structure

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Functions to fit Gaussian linear model by maximising the residual log
likelihood where the covariance structure can be written as a linear
combination of known matrices.  Can be used for multivariate models and
random effects models.  Easy straight forward manner to specify random
effects models, including random interactions. Code now optimised to use
Sherman Morrison Woodbury identities for matrix inversion in random
effects models. We've added the ability to fit models using any kernel as
well as a function to return the mean and covariance of random effects
conditional on the data (best linear unbiased predictors, BLUPs). Clifford
and McCullagh (2006)
<https://www.r-project.org/doc/Rnews/Rnews_2006-2.pdf>.

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

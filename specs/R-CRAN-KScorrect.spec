%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KScorrect
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Lilliefors-Corrected Kolmogorov-Smirnov Goodness-of-Fit Tests

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.0
BuildRequires:    R-CRAN-mclust >= 5.4
BuildRequires:    R-parallel >= 3.6.0
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-doParallel >= 1.0.14
BuildRequires:    R-CRAN-iterators >= 1.0.10
Requires:         R-CRAN-MASS >= 7.3.0
Requires:         R-CRAN-mclust >= 5.4
Requires:         R-parallel >= 3.6.0
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-doParallel >= 1.0.14
Requires:         R-CRAN-iterators >= 1.0.10

%description
Implements the Lilliefors-corrected Kolmogorov-Smirnov test for use in
goodness-of-fit tests, suitable when population parameters are unknown and
must be estimated by sample statistics. P-values are estimated by
simulation. Can be used with a variety of continuous distributions,
including normal, lognormal, univariate mixtures of normals, uniform,
loguniform, exponential, gamma, and Weibull distributions. Functions to
generate random numbers and calculate density, distribution, and quantile
functions are provided for use with the log uniform and mixture
distributions.

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

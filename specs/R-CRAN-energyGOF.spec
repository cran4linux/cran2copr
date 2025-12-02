%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  energyGOF
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Tests for Univariate Data via Energy

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-statmod 

%description
Conduct one- and two-sample goodness-of-fit tests for univariate data. In
the one-sample case, normal, uniform, exponential, Bernoulli, binomial,
geometric, beta, Poisson, lognormal, Laplace, asymmetric Laplace, inverse
Gaussian, half-normal, chi-squared, gamma, F, Weibull, Cauchy, and Pareto
distributions are supported. egof.test() can also test goodness-of-fit to
any distribution with a continuous distribution function. A subset of the
available distributions can be tested for the composite goodness-of-fit
hypothesis, that is, one can test for distribution fit with unknown
parameters. P-values are calculated via parametric bootstrap.

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

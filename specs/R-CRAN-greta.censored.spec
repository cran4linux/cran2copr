%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  greta.censored
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Censored Distributions for 'greta'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow >= 2.7.0
BuildRequires:    R-CRAN-greta >= 0.4.2
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-tensorflow >= 2.7.0
Requires:         R-CRAN-greta >= 0.4.2
Requires:         R-CRAN-glue 
Requires:         R-CRAN-reticulate 

%description
Provides additional censored distributions for use with 'greta', a
probabilistic programming framework for Bayesian modeling. Includes
censored versions of Normal, Log-Normal, Student's T, Gamma, Exponential,
Weibull, Pareto, and Beta distributions with support for right, left, and
interval censoring. For details on 'greta', see Golding (2019)
<doi:10.21105/joss.01601>. The methods are implemented using 'TensorFlow'
and 'TensorFlow Probability' for efficient computation.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Delaporte
%global packver   8.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Functions for the Delaporte Distribution

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-parallel 

%description
Provides probability mass, distribution, quantile, random-variate
generation, and method-of-moments parameter-estimation functions for the
Delaporte distribution with parameterization based on Vose (2008)
<isbn:9780470512845>. The Delaporte is a discrete probability distribution
which can be considered the convolution of a negative binomial
distribution with a Poisson distribution. Alternatively, it can be
considered a counting distribution with both Poisson and negative binomial
components. It has been studied in actuarial science as a frequency
distribution which has more variability than the Poisson, but less than
the negative binomial.

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

%global __brp_check_rpaths %{nil}
%global packname  EDFtest
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness of Fit Based on Empirical Distribution Function

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm >= 1.4.3
BuildRequires:    R-CRAN-rmutil >= 1.1.5
BuildRequires:    R-stats 
Requires:         R-CRAN-CompQuadForm >= 1.4.3
Requires:         R-CRAN-rmutil >= 1.1.5
Requires:         R-stats 

%description
This repository contains software for the calculation of goodness-of-fit
test statistics and their P-values. The three statistics computed are the
Empirical Distribution function statistics called Cramer-von Mises,
Anderson-Darling, and Watson statistics. The statistics and their P-values
can be used to assess an assumed distribution.The following distributions
are available: Uniform, Normal, Gamma, Logistic, Laplace, Weibull, Extreme
Value, and Exponential.

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

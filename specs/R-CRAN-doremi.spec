%global __brp_check_rpaths %{nil}
%global packname  doremi
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamics of Return to Equilibrium During Multiple Inputs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-futile.logger 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-futile.logger 

%description
Provides models to fit the dynamics of a regulated system experiencing
exogenous inputs. The underlying models use differential equations and
linear mixed-effects regressions to estimate the coefficients of the
equation. With them, the functions can provide an estimated signal. The
package provides simulation and analysis functions and also print,
summary, plot and predict methods, adapted to the function outputs, for
easy implementation and presentation of results.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

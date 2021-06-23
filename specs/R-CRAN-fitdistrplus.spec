%global __brp_check_rpaths %{nil}
%global packname  fitdistrplus
%global packver   1.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Help to Fit of a Parametric Distribution to Non-Censored or Censored Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-grDevices 
Requires:         R-CRAN-survival 
Requires:         R-methods 
Requires:         R-stats 

%description
Extends the fitdistr() function (of the MASS package) with several
functions to help the fit of a parametric distribution to non-censored or
censored data. Censored data may contain left censored, right censored and
interval censored values, with several lower and upper bounds. In addition
to maximum likelihood estimation (MLE), the package provides moment
matching (MME), quantile matching (QME), maximum goodness-of-fit
estimation (MGE) and maximum spacing estimation (MSE) methods (available
only for non-censored data). Weighted versions of MLE, MME, QME and MSE
are available. See e.g. Casella & Berger (2002), Statistical inference,
Pacific Grove, for a general introduction to parametric estimation.

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

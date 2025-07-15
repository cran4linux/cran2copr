%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glsm
%global packver   0.0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Saturated Model Log-Likelihood for Multinomial Outcomes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-VGAM >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-VGAM >= 1.0.0
Requires:         R-stats 
Requires:         R-CRAN-plyr 

%description
When the response variable Y takes one of R > 1 values, the function
'glsm()' computes the maximum likelihood estimates (MLEs) of the
parameters under four models: null, complete, saturated, and logistic. It
also calculates the log-likelihood values for each model. This method
assumes independent, non-identically distributed variables. For grouped
data with a multinomial outcome, where observations are divided into J
populations, the function 'glsm()' provides estimation for any number K of
explanatory variables.

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

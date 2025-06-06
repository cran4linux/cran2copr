%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lsm
%global packver   0.2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of the log Likelihood of the Saturated Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-stats 

%description
When the values of the outcome variable Y are either 0 or 1, the function
lsm() calculates the estimation of the log likelihood in the saturated
model. This model is characterized by Llinas (2006, ISSN:2389-8976) in
section 2.3 through the assumptions 1 and 2. The function LogLik() works
(almost perfectly) when the number of independent variables K is high, but
for small K it calculates wrong values in some cases. For this reason,
when Y is dichotomous and the data are grouped in J populations, it is
recommended to use the function lsm() because it works very well for all
K.

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

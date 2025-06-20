%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggeffects
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Tidy Data Frames of Marginal Effects for 'ggplot' from Model Outputs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-insight >= 1.0.1
BuildRequires:    R-CRAN-datawizard >= 1.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-insight >= 1.0.1
Requires:         R-CRAN-datawizard >= 1.0.0
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Compute marginal effects and adjusted predictions from statistical models
and returns the result as tidy data frames. These data frames are ready to
use with the 'ggplot2'-package. Effects and predictions can be calculated
for many different models. Interaction terms, splines and polynomial terms
are also supported. The main functions are ggpredict(), ggemmeans() and
ggeffect(). There is a generic plot()-method to plot the results using
'ggplot2'.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Greg
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Helper Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlTable >= 2.0.0
BuildRequires:    R-CRAN-Gmisc >= 1.0.3
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-Epi 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-htmlTable >= 2.0.0
Requires:         R-CRAN-Gmisc >= 1.0.3
Requires:         R-CRAN-forestplot 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-nlme 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-Epi 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Methods for manipulating regression models and for describing these in a
style adapted for medical journals. Contains functions for generating an
HTML table with crude and adjusted estimates, plotting hazard ratio,
plotting model estimates and confidence intervals using forest plots,
extending this to comparing multiple models in a single forest plots. In
addition to the descriptive methods, there are add-ons for the robust
covariance matrix provided by the 'sandwich' package, a function for
adding non-linearities to a model, and a wrapper around the 'Epi'
package's Lexis() functions for time-splitting a dataset when modeling
non-proportional hazards in Cox regressions.

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

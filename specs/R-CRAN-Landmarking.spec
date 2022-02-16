%global __brp_check_rpaths %{nil}
%global packname  Landmarking
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis using Landmark Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-riskRegression 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-mstate 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-riskRegression 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-pec 
Requires:         R-methods 
Requires:         R-CRAN-prodlim 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-mstate 
Requires:         R-CRAN-ggplot2 

%description
The landmark approach allows survival predictions to be updated
dynamically as new measurements from an individual are recorded. The idea
is to set predefined time points, known as "landmark times", and form a
model at each landmark time using only the individuals in the risk set.
This package allows the longitudinal data to be modelled either using the
last observation carried forward or linear mixed effects modelling. There
is also the option to model competing risks, either through cause-specific
Cox regression or Fine-Gray regression. To find out more about the methods
in this package, please see
<https://isobelbarrott.github.io/Landmarking/articles/Landmarking>.

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

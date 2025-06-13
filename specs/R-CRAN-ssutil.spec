%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ssutil
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size Calculation Tools

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-gsDesign 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-gsDesign 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tibble 

%description
Functions for sample size estimation and simulation in clinical trials.
Includes methods for selecting the best group using the Indifference-zone
approach, as well as designs for non-inferiority, equivalence, and
negative binomial models. For the sample size calculation for
non-inferiority of vaccines, the approach is based on Fleming, Powers, and
Huang (2021) <doi:10.1177/1740774520988244>. The Indifference-zone
approach is based on Sobel and Huyett (1957)
<doi:10.1002/j.1538-7305.1957.tb02411.x> and Bechhofer, Santner, and
Goldsman (1995, ISBN:978-0-471-57427-9).

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

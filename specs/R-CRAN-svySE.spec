%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  svySE
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sampling Error Estimation for Complex Surveys

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-stats 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-openxlsx 
Requires:         R-stats 

%description
Estimates sampling errors and produces indicator tables for complex survey
data. Supports weighted totals, proportions, standard errors, confidence
intervals, coefficients of variation, design effects, unweighted
frequencies, grouped estimates, domain estimates, optional stratification
and clustering variables, and customizable exports to '.xlsx' files.
Survey estimation is based on design-based inference using Taylor series
linearization implemented in the 'survey' package (Lumley, 2004,
<doi:10.18637/jss.v009.i08>; Lumley, 2010, ISBN:9780470284308). The
package provides a reproducible workflow for official statistics,
household surveys, and applied survey research.

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

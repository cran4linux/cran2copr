%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baytrends
%global packver   2.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Long Term Water Quality Trend Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dataRetrieval 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-sessioninfo 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-dataRetrieval 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-grDevices 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-sessioninfo 
Requires:         R-CRAN-survival 

%description
Enable users to evaluate long-term trends using a Generalized Additive
Modeling (GAM) approach. The model development includes selecting a GAM
structure to describe nonlinear seasonally-varying changes over time,
incorporation of hydrologic variability via either a river flow or
salinity, the use of an intervention to deal with method or laboratory
changes suspected to impact data values, and representation of left- and
interval-censored data. The approach has been applied to water quality
data in the Chesapeake Bay, a major estuary on the east coast of the
United States to provide insights to a range of management- and
research-focused questions.  Methodology described in Murphy (2019)
<doi:10.1016/j.envsoft.2019.03.027>.

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

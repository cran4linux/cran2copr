%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RDS
%global packver   0.9-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          1%{?dist}%{?buildtag}
Summary:          Respondent-Driven Sampling

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.1
Requires:         R-core >= 2.5.1
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-statnet.common 
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-isotone 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-methods 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-network 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-statnet.common 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-isotone 

%description
Provides functionality for carrying out estimation with data collected
using Respondent-Driven Sampling. This includes Heckathorn's RDS-I and
RDS-II estimators as well as Gile's Sequential Sampling estimator. The
package is part of the "RDS Analyst" suite of packages for the analysis of
respondent-driven sampling data. See Gile and Handcock (2010)
<doi:10.1111/j.1467-9531.2010.01223.x> and Gile and Handcock (2015)
<doi:10.1111/rssa.12091>.

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

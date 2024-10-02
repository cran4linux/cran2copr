%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surveillance
%global packver   1.24.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.24.0
Release:          1%{?dist}%{?buildtag}
Summary:          Temporal and Spatio-Temporal Modeling and Monitoring of Epidemic Phenomena

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-sp >= 2.1.4
BuildRequires:    R-CRAN-xtable >= 1.7.0
BuildRequires:    R-CRAN-polyCub >= 0.8.0
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-CRAN-sp >= 2.1.4
Requires:         R-CRAN-xtable >= 1.7.0
Requires:         R-CRAN-polyCub >= 0.8.0
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-spatstat.geom 

%description
Statistical methods for the modeling and monitoring of time series of
counts, proportions and categorical data, as well as for the modeling of
continuous-time point processes of epidemic phenomena. The monitoring
methods focus on aberration detection in count data time series from
public health surveillance of communicable diseases, but applications
could just as well originate from environmetrics, reliability engineering,
econometrics, or social sciences. The package implements many typical
outbreak detection procedures such as the (improved) Farrington algorithm,
or the negative binomial GLR-CUSUM method of Hoehle and Paul (2008)
<doi:10.1016/j.csda.2008.02.015>. A novel CUSUM approach combining
logistic and multinomial logistic modeling is also included. The package
contains several real-world data sets, the ability to simulate outbreak
data, and to visualize the results of the monitoring in a temporal,
spatial or spatio-temporal fashion. A recent overview of the available
monitoring procedures is given by Salmon et al. (2016)
<doi:10.18637/jss.v070.i10>. For the retrospective analysis of epidemic
spread, the package provides three endemic-epidemic modeling frameworks
with tools for visualization, likelihood inference, and simulation. hhh4()
estimates models for (multivariate) count time series following Paul and
Held (2011) <doi:10.1002/sim.4177> and Meyer and Held (2014)
<doi:10.1214/14-AOAS743>. twinSIR() models the
susceptible-infectious-recovered (SIR) event history of a fixed
population, e.g, epidemics across farms or networks, as a multivariate
point process as proposed by Hoehle (2009) <doi:10.1002/bimj.200900050>.
twinstim() estimates self-exciting point process models for a
spatio-temporal point pattern of infective events, e.g., time-stamped
geo-referenced surveillance data, as proposed by Meyer et al. (2012)
<doi:10.1111/j.1541-0420.2011.01684.x>. A recent overview of the
implemented space-time modeling frameworks for epidemic phenomena is given
by Meyer et al. (2017) <doi:10.18637/jss.v077.i11>.

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

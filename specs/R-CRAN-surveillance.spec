%global packname  surveillance
%global packver   1.17.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.17.3
Release:          1%{?dist}
Summary:          Temporal and Spatio-Temporal Modeling and Monitoring of EpidemicPhenomena

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-xtable >= 1.7.0
BuildRequires:    R-CRAN-spatstat >= 1.36.0
BuildRequires:    R-CRAN-sp >= 1.0.15
BuildRequires:    R-CRAN-polyCub >= 0.6.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-nlme 
Requires:         R-CRAN-xtable >= 1.7.0
Requires:         R-CRAN-spatstat >= 1.36.0
Requires:         R-CRAN-sp >= 1.0.15
Requires:         R-CRAN-polyCub >= 0.6.0
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-nlme 

%description
Statistical methods for the modeling and monitoring of time series of
counts, proportions and categorical data, as well as for the modeling of
continuous-time point processes of epidemic phenomena. The monitoring
methods focus on aberration detection in count data time series from
public health surveillance of communicable diseases, but applications
could just as well originate from environmetrics, reliability engineering,
econometrics, or social sciences. The package implements many typical
outbreak detection procedures such as the (improved) Farrington algorithm,
or the negative binomial GLR-CUSUM method of H<f6>hle and Paul (2008)
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
point process as proposed by H<f6>hle (2009) <doi:10.1002/bimj.200900050>.
twinstim() estimates self-exciting point process models for a
spatio-temporal point pattern of infective events, e.g., time-stamped
geo-referenced surveillance data, as proposed by Meyer et al. (2012)
<doi:10.1111/j.1541-0420.2011.01684.x>. A recent overview of the
implemented space-time modeling frameworks for epidemic phenomena is given
by Meyer et al. (2017) <doi:10.18637/jss.v077.i11>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/jags
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/shapes
%doc %{rlibdir}/%{packname}/THANKS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

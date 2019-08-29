%global packname  etasFLP
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Mixed FLP and ML Estimation of ETAS Space-Time Point Processes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-mapdata 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-maps 
Requires:         R-CRAN-mapdata 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-maps 

%description
Estimation of the components of an ETAS (Epidemic Type Aftershock
Sequence) model for earthquake description. Non-parametric background
seismicity can be estimated through FLP (Forward Likelihood Predictive),
while parametric components are estimated through maximum likelihood. The
two estimation steps are alternated until convergence is obtained. For
each event the probability of being a background event is estimated and
used as a weight for declustering steps. Many options to control the
estimation process are present, together with some diagnostic tools. Some
descriptive functions for earthquakes catalogs are present; also plot,
print, summary, profile methods are defined for main output (objects of
class 'etasclass').

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

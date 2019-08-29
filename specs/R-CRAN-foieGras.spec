%global packname  foieGras
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Fit Continuous-Time State-Space Models for Filtering ArgosSatellite (and Other) Telemetry Data

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-argosfilter 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-argosfilter 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 

%description
Fits continuous-time random walk and correlated random walk state-space
models to filter Argos satellite location data. Template Model Builder
('TMB') is used for fast estimation. The Argos data can be: (older) least
squares-based locations; (newer) Kalman filter-based locations with error
ellipse information; or a mixture of both. Separate measurement models are
used for these two data types. The models estimate two sets of location
states corresponding to: 1) each observation, which are (usually)
irregularly timed; and 2) user-specified time intervals (regular or
irregular). Jonsen I, McMahon CR, Patterson TA, Auger-Methe M, Harcourt R,
Hindell MA, Bestley S (2019) Movement responses to environment: fast
inference of variation among southern elephant seals with a mixed effects
model. Ecology 100:e02566 <doi:10.1002/ecy.2566>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

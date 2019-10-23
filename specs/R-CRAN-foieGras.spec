%global packname  foieGras
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Fit Continuous-Time State-Space and Latent Variable Models forFiltering Argos Satellite (and Other) Telemetry Data andEstimating Movement Behaviour

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-TMB >= 1.7.15
BuildRequires:    R-CRAN-future >= 1.13.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-sf >= 0.8.0
BuildRequires:    R-CRAN-furrr >= 0.1.0
BuildRequires:    R-CRAN-argosfilter 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rworldmap 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-TMB >= 1.7.15
Requires:         R-CRAN-future >= 1.13.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-sf >= 0.8.0
Requires:         R-CRAN-furrr >= 0.1.0
Requires:         R-CRAN-argosfilter 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rworldmap 
Requires:         R-parallel 

%description
Fits continuous-time random walk and correlated random walk state-space
models to filter animal tracking data ('Argos', processed light-level
'geolocation', 'GPS'). Template Model Builder ('TMB') is used for fast
estimation. The 'Argos' data can be: (older) least squares-based
locations; (newer) Kalman filter-based locations with error ellipse
information; or a mixture of both. The models estimate two sets of
location states corresponding to: 1) each observation, which are (usually)
irregularly timed; and 2) user-specified time intervals (regular or
irregular). Latent variable models are provided to estimate move
persistence along tracks as an index of behaviour. 'Jonsen I', 'McMahon
CR', 'Patterson TA', 'Auger-Methe M', 'Harcourt R', 'Hindell MA', 'Bestley
S' (2019) Movement responses to environment: fast inference of variation
among southern elephant seals with a mixed effects model. Ecology
100:e02566 <doi:10.1002/ecy.2566>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

%global packname  joineR
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          Joint Modelling of Repeated Measurements and Time-to-Event Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-graphics 
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-survival 
Requires:         R-graphics 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-nlme 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-utils 

%description
Analysis of repeated measurements and time-to-event data via random
effects joint models. Fits the joint models proposed by Henderson and
colleagues <doi:10.1093/biostatistics/1.4.465> (single event time) and by
Williamson and colleagues (2008) <doi:10.1002/sim.3451> (competing risks
events time) to a single continuous repeated measure. The time-to-event
data is modelled using a (cause-specific) Cox proportional hazards
regression model with time-varying covariates. The longitudinal outcome is
modelled using a linear mixed effects model. The association is captured
by a latent Gaussian process. The model is estimated using am Expectation
Maximization algorithm. Some plotting functions and the variogram are also
included. This project is funded by the Medical Research Council (Grant
numbers G0400615 and MR/M013227/1).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

%global packname  survPen
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Multidimensional Penalized Splines for Survival and Net SurvivalModels

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
Requires:         R-CRAN-statmod 
Requires:         R-stats 

%description
Fits hazard and excess hazard models with multidimensional penalized
splines allowing for time-dependent effects, non-linear effects and
interactions between several continuous covariates. In survival and net
survival analysis, in addition to modelling the effect of time (via the
baseline hazard), one has often to deal with several continuous covariates
and model their functional forms, their time-dependent effects, and their
interactions. Model specification becomes therefore a complex problem and
penalized regression splines represent an appealing solution to that
problem as splines offer the required flexibility while penalization
limits overfitting issues. Current implementations of penalized survival
models can be slow or unstable and sometimes lack some key features like
taking into account expected mortality to provide net survival and excess
hazard estimates. In contrast, survPen provides an automated, fast, and
stable implementation (thanks to explicit calculation of the derivatives
of the likelihood) and offers a unified framework for multidimensional
penalized hazard and excess hazard models. survPen may be of interest to
those who 1) analyse any kind of time-to-event data: mortality, disease
relapse, machinery breakdown, unemployment, etc 2) wish to describe the
associated hazard and to understand which predictors impact its dynamics.
See Fauvernier et al. (2019a) <doi:10.21105/joss.01434> for an overview of
the package and Fauvernier et al. (2019b) <doi:10.1111/rssc.12368> for the
method.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

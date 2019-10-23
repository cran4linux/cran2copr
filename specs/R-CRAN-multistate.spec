%global packname  multistate
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Fitting Multistate Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-date 
BuildRequires:    R-CRAN-relsurv 
Requires:         R-survival 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-date 
Requires:         R-CRAN-relsurv 

%description
Medical researchers are often interested in investigating the relationship
between explicative variables and multiple times-to-event.
Time-inhomogeneous Markov models consist of modelling the probabilities of
transitions according to the chronological times (times since the baseline
of the study). Semi-Markov (SM) models consist of modelling the
probabilities of transitions according to the times spent in states. In
this package, we propose functions implementing such 3-state and 4-state
multivariable and multistate models. The user can introduce multiple
covariates to estimate conditional (subject-specific) effects. We also
propose to adjust for possible confounding factors by using the Inverse
Probability Weighting (IPW). When a state is patient death, the user can
consider to take into account the mortality of the general population
(relative survival approach). Finally, in the particular situation of one
initial transient state and two competing and absorbing states, this
package allows for estimating mixture models.

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
%{rlibdir}/%{packname}/INDEX

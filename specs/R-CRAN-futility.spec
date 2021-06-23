%global __brp_check_rpaths %{nil}
%global packname  futility
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Interim Analysis of Operational Futility in Randomized Trialswith Time-to-Event Endpoints and Fixed Follow-Up

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Randomized clinical trials commonly follow participants for a
time-to-event efficacy endpoint for a fixed period of time. Consequently,
at the time when the last enrolled participant completes their follow-up,
the number of observed endpoints is a random variable. Assuming data
collected through an interim timepoint, simulation-based estimation and
inferential procedures in the standard right-censored failure time
analysis framework are conducted for the distribution of the number of
endpoints--in total as well as by treatment arm--at the end of the
follow-up period. The future (i.e., yet unobserved) enrollment, endpoint,
and dropout times are generated according to mechanisms specified in the
simTrial() function in the 'seqDesign' package. A Bayesian model for the
endpoint rate, offering the option to specify a robust mixture prior
distribution, is used for generating future data (see the vignette for
details). Inference can be restricted to participants who received
treatment according to the protocol and are observed to be at risk for the
endpoint at a specified timepoint. Plotting functions are provided for
graphical display of results.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

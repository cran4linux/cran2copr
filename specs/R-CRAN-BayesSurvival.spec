%global packname  BayesSurvival
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Bayesian Survival Analysis for Right Censored Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 

%description
Performs unadjusted Bayesian survival analysis for right censored
time-to-event data. The main function, BayesSurv(), computes the posterior
mean and a credible band for the survival function and for the cumulative
hazard, as well as the posterior mean for the hazard, starting from a
piecewise exponential (histogram) prior with Gamma distributed heights
that are either independent, or have a Markovian dependence structure. A
function, PlotBayesSurv(), is provided to easily create plots of the
posterior means of the hazard, cumulative hazard and survival function,
with a credible band accompanying the latter two. The priors and samplers
are described in more detail in Castillo and Van der Pas (2020)
"Multiscale Bayesian survival analysis" <arXiv:2005.02889>. In that paper
it is also shown that the credible bands for the survival function and the
cumulative hazard can be considered confidence bands (under mild
conditions) and thus offer reliable uncertainty quantification.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/INDEX

%global __brp_check_rpaths %{nil}
%global packname  ratesci
%global packver   0.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Confidence Intervals for Comparisons of Binomial or PoissonRates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch

%description
Computes confidence intervals for the rate (or risk) difference ('RD') or
rate ratio (or relative risk, 'RR') for binomial proportions or Poisson
rates, or for odds ratio ('OR', binomial only). Also confidence intervals
for a single binomial or Poisson rate, and intervals for matched pairs.
Includes skewness-corrected asymptotic score ('SCAS') methods, which have
been developed in Laud (2017) <doi:10.1002/pst.1813> from Miettinen &
Nurminen (1985) <doi:10.1002/sim.4780040211> and Gart & Nam (1988)
<doi:10.2307/2531848>. Also includes MOVER methods (Method Of Variance
Estimates Recovery) for all contrasts, derived from the Newcombe method
but using equal-tailed Jeffreys intervals, and generalised for Bayesian
applications incorporating prior information. So-called 'exact' methods
for strictly conservative coverage are approximated using continuity
corrections. Also includes methods for stratified calculations (e.g.
meta-analysis), either assuming fixed effects or incorporating stratum
heterogeneity.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

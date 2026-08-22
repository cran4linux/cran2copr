%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bruno
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predicting User-Defined Event Recurrence under Exchangeability

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implements analytical prediction of recurrence for user-defined binary
events; 'bruno' abbreviates Beta-Bernoulli Recurrence for Unobserved Next
Outcomes. The procedure applies when the observed and future event
indicators are judged exchangeable for the intended prediction. For an
indefinitely extendible exchangeable binary sequence, de Finetti's
representation theorem expresses the assigned joint probabilities as a
mixture of Bernoulli laws over a mixing distribution on the unit interval
(de Finetti, 1931) <doi:10.4064/fm-17-1-298-329>. The package adopts a
beta distribution as an additional parametric specification of this mixing
distribution. Users specify an initial probability mu0 assigned to the
event and a positive concentration parameter tau, giving beta parameters a
= mu0 * tau and b = (1 - mu0) * tau. If the declared event occurs s times
among n observed cases, conditioning gives Beta(a + s, b + n - s). From
this conditional assessment, the package computes analytically the
probability assigned to occurrence of the same event in the next
exchangeable case and, for a prespecified future sample size, the exact
beta-binomial predictive distribution of the number of future event
occurrences. Events may be supplied directly as logical or binary
indicators or defined from paired pre-post measurements through a
user-specified logical expression. Prediction may be performed for a
single predictive class or separately across user-defined predictive
classes, using common or class-specific initial probabilities and
concentration parameters. Cases for which event status cannot be
determined, and cases with missing predictive-class membership in grouped
analyses, are excluded without imputation; case-level classification and
inclusion information are retained for audit purposes. Summary methods
provide central probability intervals for the conditional beta assessment
and, for future samples larger than one case, predictive intervals for the
future recurrence count. The package is intended for psychological,
educational, pilot-study, and research decision-making applications in
which recurrence of an explicitly defined event is the predictive target
and the predictive relevance of observed cases for future cases can be
substantively justified. The resulting probabilities concern recurrence of
the declared event within the stated predictive class and do not
independently establish latent change, intervention efficacy, causal
effects, measurement validity, or a research decision.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

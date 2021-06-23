%global __brp_check_rpaths %{nil}
%global packname  CoRpower
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Power Calculations for Assessing Correlates of Risk in Clinical Efficacy Trials

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-osDesign 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-osDesign 

%description
Calculates power for assessment of intermediate biomarker responses as
correlates of risk in the active treatment group in clinical efficacy
trials, as described in Gilbert, Janes, and Huang, Power/Sample Size
Calculations for Assessing Correlates of Risk in Clinical Efficacy Trials
(2016, Statistics in Medicine). The methods differ from past approaches by
accounting for the level of clinical treatment efficacy overall and in
biomarker response subgroups, which enables the correlates of risk results
to be interpreted in terms of potential correlates of efficacy/protection.
The methods also account for inter-individual variability of the observed
biomarker response that is not biologically relevant (e.g., due to
technical measurement error of the laboratory assay used to measure the
biomarker response), which is important because power to detect a
specified correlate of risk effect size is heavily affected by the
biomarker's measurement error. The methods can be used for a general
binary clinical endpoint model with a univariate dichotomous,
trichotomous, or continuous biomarker response measured in active
treatment recipients at a fixed timepoint after randomization, with either
case-cohort Bernoulli sampling or case-control without-replacement
sampling of the biomarker (a baseline biomarker is handled as a trivial
special case). In a specified two-group trial design, the computeN()
function can initially be used for calculating additional requisite design
parameters pertaining to the target population of active treatment
recipients observed to be at risk at the biomarker sampling timepoint.
Subsequently, the power calculation employs an inverse probability
weighted logistic regression model fitted by the tps() function in the
'osDesign' package. Power results as well as the relationship between the
correlate of risk effect size and treatment efficacy can be visualized
using various plotting functions. To link power calculations for detecting
a correlate of risk and a correlate of treatment efficacy, a baseline
immunogenicity predictor (BIP) can be simulated according to a specified
classification rule (for dichotomous or trichotomous BIPs) or correlation
with the biomarker response (for continuous BIPs), then outputted along
with biomarker response data under assignment to treatment, and clinical
endpoint data for both treatment and placebo groups.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ipeval
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluation of Interventional Predictions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-prodlim 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-prodlim 

%description
Provides methods to evaluate predictive performance of models that
estimate risks under hypothetical intervention scenarios
(interventional/causal/counterfactual predictions) with observational data
subject to treatment-outcome confounding. Inverse probability of treatment
weighting (IPTW) is used to construct a pseudopopulation in which all
individuals receive a specified intervention, enabling assessment of
agreement between predicted risks under the intervention and observed
outcomes in the pseudo-population corresponding to that intervention.
Package supports binary and time-to-event outcomes under binary
interventions made at a single time point. Performance measures supported
are AUC (Area Under the receiving operating characteristic Curve), Brier
score, observed-expected ratio, and calibration plots. Methods implemented
in this package are based on work by Keogh and Van Geloven (2024)
<DOI:10.1097/EDE.0000000000001713>.

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

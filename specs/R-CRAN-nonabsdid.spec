%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nonabsdid
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualize Heterogeneity-Robust Event Studies for Non-Absorbing Treatments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
Runs several heterogeneity-robust difference-in-differences (DID)
event-study estimators for non-absorbing (i.e., treatment can switch on
and off over time, allowing treatment reversal) binary treatments through
their respective packages, harmonizes their output onto a common time axis
and tidy data structure, and overlays them in a single 'ggplot2' panel for
visual comparison. Supported estimators include those provided by
'DIDmultiplegtDYN', 'PanelMatch', and 'fect', with an optional naive
two-way fixed-effects reference series via 'fixest'. The underlying
methods are respectively described in Clement de Chaisemartin and Xavier
D'Haultfoeuille. "Difference-in-Differences Estimators of Intertemporal
Treatment Effects." The Review of Economics and Statistics (2026)
<doi:10.1162/rest_a_01414>, Kosuke Imai, In Song Kim, and Erik H. Wang.
"Matching methods for causal inference with time‐series cross‐sectional
data." American Journal of Political Science 67.3 (2023)
<doi:10.1111/ajps.12685>, Licheng Liu, Ye Wang, and Yiqing Xu. "A
practical guide to counterfactual estimators for causal inference with
time‐series cross‐sectional data." American Journal of Political Science
68.1 (2024) <doi:10.1111/ajps.12723>, and Laurent R. Bergé, Kyle Butts,
and Grant McDermott. "Fast and user-friendly econometrics estimations: The
R package 'fixest'." arXiv preprint (2026)
<doi:10.48550/arXiv.2601.21749>. A single nabs_event_study() wrapper runs
any supported estimator with a common interface; nabs_event_study_simple()
provides a one-line front door for quick exploratory runs; the S3 generic
as_nabs_event_study() coerces estimator output into a tidy stable schema;
and nabs_event_plot() overlays multiple methods on a single 'ggplot2'
panel, with optional naive two-way fixed effects drawn in a neutral color
as a reference.

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

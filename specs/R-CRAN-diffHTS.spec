%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diffHTS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Differential Drug Sensitivity Analysis for Two-Condition High-Throughput Screens

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
A complete workflow for large-scale, two-condition high-throughput drug
screening (HTS). It compares drug sensitivity between any two experimental
conditions - for example irradiated versus non-irradiated cells, cancer
versus normal cell lines, or treated versus untreated samples - across
many plates and experiments. The package covers the full pipeline:
control-based normalisation, plate-level quality-control metrics
(Z-factor, Z-prime, signal-to-background, signal-to-noise and strictly
standardised mean difference), replicate-consistency checks,
four-parameter logistic dose-response fitting with area under the curve
(AUC) estimation, differential (delta) AUC scoring with within-plate
standardisation, cut-off and sigma-based hit selection, and
publication-ready heatmap, scatter and quality-control visualisations.

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

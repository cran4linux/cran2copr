%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metricT
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Directional Fragility Diagnostics for EEG Connectivity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Implements Metric-T, a permutation-based diagnostic that flags when the
reported direction of a group difference in electroencephalography (EEG)
functional connectivity depends on the choice of metric. Direction
consistency (DC) converts the weighted phase lag index (wPLI) and
magnitude-squared coherence (MSC), both derived from the same
cross-spectrum, into the percentage of channel-pair features for which one
group exceeds the other; Metric-T is T = DC(wPLI) - DC(MSC). Significance
is assessed by aligned label permutation with marginal and Westfall-Young
max-T multiplicity control. For small samples the reference set is
enumerated completely: exact two-group tests, the complete two-group
labelling space (in which cut-points, exclusions and batches are located
on one distribution), and a stratified exact test for a continuous
covariate. Core functions use base R only; a 'shiny' graphical interface
is included. Method: Kimura (2026) <doi:10.1016/j.neuri.2026.100286>.

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

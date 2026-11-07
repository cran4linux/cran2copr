%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DiallelAnalysisR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Diallel Analysis, Heterosis and Related Mating Designs

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Analysis of diallel crosses and related mating designs in plant breeding,
from the plot data of randomized complete block experiments: Griffing's
four methods and two models (Griffing, 1956 <doi:10.1071/BI9560463>), from
plot data, from a published table of means or over several environments,
with gca by environment and sca by environment interactions and a split of
reciprocal effects into maternal and non-maternal parts (Cockerham and
Weir, 1977); Hayman's analysis with the Wr-Vr graph and the components of
variation (Hayman, 1954 <doi:10.1093/genetics/39.6.789>); mid-parent,
better-parent and standard heterosis with t tests; Gardner and Eberhart's
(1966) Analyses II and III; the partial diallel (Kempthorne and Curnow,
1961 <doi:10.2307/2527989>); line by tester analysis with proportional
contributions; and the North Carolina designs I, II and III (Comstock and
Robinson, 1948). Missing plots are handled by least-squares means. Results
include analyses of variance, effects with standard errors, variance
components and genetic ratios, plots of the effects and a biplot of the
crosses, tables for papers in Word, LaTeX, HTML or Markdown, simulation of
diallel data and the power of the tests for planning the number of
replicates, and an interactive 'shiny' application.

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

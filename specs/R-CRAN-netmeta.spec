%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  netmeta
%global packver   3.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Network Meta-Analysis using Frequentist Methods

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 8.0.1
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
Requires:         R-CRAN-meta >= 8.0.1
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-colorspace 
Requires:         R-grid 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 

%description
A comprehensive set of functions providing frequentist methods for network
meta-analysis (Balduzzi et al., 2023) <doi:10.18637/jss.v106.i02> and
supporting Schwarzer et al. (2015) <doi:10.1007/978-3-319-21416-0>,
Chapter 8 "Network Meta-Analysis": - frequentist network meta-analysis
following Rücker (2012) <doi:10.1002/jrsm.1058>; - additive network
meta-analysis for combinations of treatments (Rücker et al., 2020)
<doi:10.1002/bimj.201800167>; - network meta-analysis of binary data using
the Mantel-Haenszel or non-central hypergeometric distribution method
(Efthimiou et al., 2019) <doi:10.1002/sim.8158>, or penalised logistic
regression (Evrenoglou et al., 2022) <doi:10.1002/sim.9562>; - rankograms
and ranking of treatments by the Surface under the cumulative ranking
curve (SUCRA) (Salanti et al., 2013) <doi:10.1016/j.jclinepi.2010.03.016>;
- ranking of treatments using P-scores (frequentist analogue of SUCRAs
without resampling) according to Rücker & Schwarzer (2015)
<doi:10.1186/s12874-015-0060-8>; - split direct and indirect evidence to
check consistency (Dias et al., 2010) <doi:10.1002/sim.3767>, (Efthimiou
et al., 2019) <doi:10.1002/sim.8158>; - league table with network
meta-analysis results; - 'comparison-adjusted' funnel plot (Chaimani &
Salanti, 2012) <doi:10.1002/jrsm.57>; - net heat plot and design-based
decomposition of Cochran's Q according to Krahn et al. (2013)
<doi:10.1186/1471-2288-13-35>; - measures characterizing the flow of
evidence between two treatments by König et al. (2013)
<doi:10.1002/sim.6001>; - automated drawing of network graphs described in
Rücker & Schwarzer (2016) <doi:10.1002/jrsm.1143>; - partial order of
treatment rankings ('poset') and Hasse diagram for 'poset' (Carlsen &
Bruggemann, 2014) <doi:10.1002/cem.2569>; (Rücker & Schwarzer, 2017)
<doi:10.1002/jrsm.1270>; - contribution matrix as described in
Papakonstantinou et al. (2018) <doi:10.12688/f1000research.14770.3> and
Davies et al. (2022) <doi:10.1002/sim.9346>; - subgroup network
meta-analysis.

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

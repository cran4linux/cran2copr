%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  netmeta
%global packver   2.8-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Network Meta-Analysis using Frequentist Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 6.2.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-metafor 
Requires:         R-CRAN-meta >= 6.2.0
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-magic 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-metafor 

%description
A comprehensive set of functions providing frequentist methods for network
meta-analysis and supporting Schwarzer et al. (2015)
<DOI:10.1007/978-3-319-21416-0>, Chapter 8 "Network Meta-Analysis": -
frequentist network meta-analysis following Rücker (2012)
<DOI:10.1002/jrsm.1058>; - net heat plot and design-based decomposition of
Cochran's Q according to Krahn et al. (2013)
<DOI:10.1186/1471-2288-13-35>; - measures characterizing the flow of
evidence between two treatments by König et al. (2013)
<DOI:10.1002/sim.6001>; - ranking of treatments (frequentist analogue of
SUCRA) according to Rücker & Schwarzer (2015)
<DOI:10.1186/s12874-015-0060-8>; - partial order of treatment rankings
('poset') and Hasse diagram for 'poset' (Carlsen & Bruggemann, 2014)
<DOI:10.1002/cem.2569>; (Rücker & Schwarzer, 2017)
<DOI:10.1002/jrsm.1270>; - split direct and indirect evidence to check
consistency (Dias et al., 2010) <DOI:10.1002/sim.3767>, (Efthimiou et al.,
2019) <DOI:10.1002/sim.8158>; - league table with network meta-analysis
results; - additive network meta-analysis for combinations of treatments
(Rücker et al., 2020) <DOI:10.1002/bimj.201800167>; - network
meta-analysis of binary data using the Mantel-Haenszel or non-central
hypergeometric distribution method (Efthimiou et al., 2019)
<DOI:10.1002/sim.8158>; - 'comparison-adjusted' funnel plot (Chaimani &
Salanti, 2012) <DOI:10.1002/jrsm.57>; - automated drawing of network
graphs described in Rücker & Schwarzer (2016) <DOI:10.1002/jrsm.1143>; -
rankograms and ranking by SUCRA; - contribution matrix as described in
Papakonstantinou et al. (2018) <DOI:10.12688/f1000research.14770.3> and
Davies et al. (2021) <arXiv:2107.02886>.

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

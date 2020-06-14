%global packname  netmeta
%global packver   1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          Network Meta-Analysis using Frequentist Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 4.9.8
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-MASS 
Requires:         R-CRAN-meta >= 4.9.8
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-magic 
Requires:         R-MASS 

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
(Rücker et al., 2019) <DOI:10.1002/bimj.201800167>; - network
meta-analysis of binary data using the Mantel-Haenszel or non-central
hypergeometric distribution method (Efthimiou et al., 2019)
<DOI:10.1002/sim.8158>; - 'comparison-adjusted' funnel plot (Chaimani &
Salanti, 2012) <DOI:10.1002/jrsm.57>; - automated drawing of network
graphs described in Rücker & Schwarzer (2016) <DOI:10.1002/jrsm.1143>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

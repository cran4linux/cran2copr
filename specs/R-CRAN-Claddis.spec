%global packname  Claddis
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Measuring Morphological Diversity and Evolutionary Tempo

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-strap 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-strap 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-gdata 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Measures morphological diversity from discrete character data and
estimates evolutionary tempo on phylogenetic trees. Imports morphological
data from #NEXUS (Maddison et al. (1997) <doi:10.1093/sysbio/46.4.590>)
format with ReadMorphNexus(), and writes to both #NEXUS and TNT format
(Goloboff et al. (2008) <doi:10.1111/j.1096-0031.2008.00217.x>). Main
functions are DiscreteCharacterRate(), which implements likelihood ratio
tests for discrete character rates introduced across Lloyd et al. (2012)
<doi:10.1111/j.1558-5646.2011.01460.x>, Brusatte et al. (2014)
<doi:10.1016/j.cub.2014.08.034>, Close et al. (2015)
<doi:10.1016/j.cub.2015.06.047>, and Lloyd (2016) <doi:10.1111/bij.12746>,
and MorphDistMatrix(), which implements multiple discrete character
distance metrics from Gower (1971) <doi:10.2307/2528823>, Wills (1998)
<doi:10.1006/bijl.1998.0255>, Lloyd (2016) <doi:10.1111/bij.12746>, and
Hopkins and St John (2018) <doi:10.1098/rspb.2018.1784>. Multiple
functions implement various morphospace plots:
ChronoPhyloMorphospacePlot() implements Sakamoto and Ruta (2012)
<doi:10.1371/journal.pone.0039752>, MorphospacePlot() implements Wills et
al. (1994) <doi:10.1017/S009483730001263X>, PlotCharacterChanges()
implements Wang and Lloyd (2016) <doi:10.1098/rspb.2016.0214>, and
StackPlot() implements Foote (1993) <doi:10.1017/S0094837300015864>. Other
functions include SafeTaxonomicReduction(), which implements Wilkinson
(1995) <doi:10.1093/sysbio/44.4.501>, and DolloSCM() implements the Dollo
stochastic character mapping of Tarver et al. (2018)
<doi:10.1093/gbe/evy096>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

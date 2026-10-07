%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hilldiv3
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Integral Analysis of Diversity Based on Hill Numbers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-cli 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
Measures and compares the diversity of biological communities (e.g. tables
of operational taxonomic units (OTUs), amplicon sequence variants (ASVs)
or metagenome-assembled genomes (MAGs)) based on Hill numbers, in a
unified framework for neutral, phylogenetic and functional diversity
measurement, diversity partitioning, (dis)similarity measurement,
diversity profiles, evenness and redundancy. The statistical framework
encompasses richness, Shannon and Simpson diversity, Faith's phylogenetic
diversity (PD), Rao's quadratic entropy and Sorensen- and UniFrac-type
dissimilarities, all grounded in a single Hill-number framework. Methods
are described in Jost (2007) <doi:10.1890/06-1736.1>, Chao et al. (2010)
<doi:10.1098/rstb.2010.0272>, Chiu et al. (2014) <doi:10.1890/12-0960.1>
and reviewed in Alberdi & Gilbert (2019) <doi:10.1111/1755-0998.13014>.
Optional import adapters interoperate with the Bioconductor packages
'phyloseq', 'SummarizedExperiment' and 'TreeSummarizedExperiment', which
are available from <https://bioconductor.org>.

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

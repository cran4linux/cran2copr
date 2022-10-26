%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phyclust
%global packver   0.1-32
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.32
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Clustering (Phyloclustering)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-ape 

%description
Phylogenetic clustering (phyloclustering) is an evolutionary Continuous
Time Markov Chain model-based approach to identify population structure
from molecular data without assuming linkage equilibrium. The package
phyclust (Chen 2011) provides a convenient implementation of
phyloclustering for DNA and SNP data, capable of clustering individuals
into subpopulations and identifying molecular sequences representative of
those subpopulations. It is designed in C for performance, interfaced with
R for visualization, and incorporates other popular open source programs
including ms (Hudson 2002) <doi:10.1093/bioinformatics/18.2.337>, seq-gen
(Rambaut and Grassly 1997) <doi:10.1093/bioinformatics/13.3.235>,
Hap-Clustering (Tzeng 2005) <doi:10.1002/gepi.20063> and PAML baseml (Yang
1997, 2007) <doi:10.1093/bioinformatics/13.5.555>,
<doi:10.1093/molbev/msm088>, for simulating data, additional analyses, and
searching the best tree. See the phyclust website for more information,
documentations and examples.

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

%global __brp_check_rpaths %{nil}
%global packname  datelife
%global packver   0.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Scientific Data on Time of Lineage Divergence for Your Taxa

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-bold 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-ips 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-compare 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rotl 
BuildRequires:    R-CRAN-paleotree 
BuildRequires:    R-CRAN-knitcitations 
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-treebase 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-phylocomr 
BuildRequires:    R-CRAN-BiocManager 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-bold 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-ips 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-compare 
Requires:         R-CRAN-geiger 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rotl 
Requires:         R-CRAN-paleotree 
Requires:         R-CRAN-knitcitations 
Requires:         R-CRAN-phylobase 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-treebase 
Requires:         R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-phylocomr 
Requires:         R-CRAN-BiocManager 
Requires:         R-CRAN-data.table 

%description
Methods and workflows to get chronograms (i.e., phylogenetic trees with
branch lengths proportional to time), using open, peer-reviewed,
state-of-the-art scientific data on time of lineage divergence. This
package constitutes the main underlying code of the DateLife web service
at <www.datelife.org>. To obtain a single summary chronogram from a group
of relevant chronograms, we implement the Super Distance Matrix (SDM)
method described in Criscuolo et al. (2006)
<doi:10.1080/10635150600969872>. To find the grove of chronograms with a
sufficiently overlapping set of taxa for summarizing, we implement theorem
1.1. from Ané et al. (2009) <doi:10.1007/s00026-009-0017-x>. A given
phylogenetic tree can be dated using time of lineage divergence data as
secondary calibrations (with caution, see Schenk (2016)
<doi:10.1371/journal.pone.0148228>). To obtain and apply secondary
calibrations, the package implements the congruification method described
in Eastman et al. (2013) <doi:10.1111/2041-210X.12051>. Tree dating can be
performed with different methods including BLADJ (Webb et al. (2008)
<doi:10.1093/bioinformatics/btn358>), PATHd8 (Britton et al. (2007)
<doi:10.1080/10635150701613783>), mrBayes (Huelsenbeck and Ronquist (2001)
<doi:10.1093/bioinformatics/17.8.754>), and treePL (Smith and O'Meara
(2012) <doi:10.1093/bioinformatics/bts492>).

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

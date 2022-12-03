%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scapGNN
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Graph Neural Network-Based Framework for Single Cell Active Pathways and Gene Modules Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ActivePathways 
BuildRequires:    R-CRAN-AdaptGauss 
BuildRequires:    R-CRAN-coop 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-methods 
BuildRequires:    R-compiler 
Requires:         R-CRAN-ActivePathways 
Requires:         R-CRAN-AdaptGauss 
Requires:         R-CRAN-coop 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-reticulate 
Requires:         R-methods 
Requires:         R-compiler 

%description
It is a single cell active pathway analysis tool based on the graph neural
network (F. Scarselli (2009) <doi:10.1109/TNN.2008.2005605>; Thomas N.
Kipf (2017) <arXiv:1609.02907v4>) to construct the gene-cell association
network, infer pathway activity scores from different single cell
modalities data, integrate multiple modality data on the same cells into
one pathway activity score matrix, identify cell phenotype activated gene
modules and parse association networks of gene modules under multiple cell
phenotype. In addition, abundant visualization programs are provided to
display the results.

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

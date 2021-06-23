%global __brp_check_rpaths %{nil}
%global packname  func2vis
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clean and Visualize Over Expression Results from'ConsensusPathDB'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-ggrepel 
Requires:         R-grDevices 

%description
Provides functions to have visualization and clean-up of enriched gene
ontologies (GO) terms, protein complexes and pathways (obtained from
multiple databases) using 'ConsensusPathDB' from gene set over-expression
analysis. Performs clustering of pathway based on similarity of
over-expressed gene sets and visualizations similar to Ingenuity Pathway
Analysis (IPA) when up and down regulated genes are known. The methods are
described in a paper currently submitted by Orecchioni et al, 2020 in
Nanoscale.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

%global packname  PhyInformR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Rapid Calculation of Phylogenetic Information Content

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-PBSmodelling 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-phytools 
Requires:         R-splines 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-PBSmodelling 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ggplot2 

%description
Enables rapid calculation of phylogenetic information content using the
latest advances in phylogenetic informativeness based theory. These
advances include modifications that incorporate uneven branch lengths and
any model of nucleotide substitution to provide assessments of the
phylogenetic utility of any given dataset or dataset partition. Also
provides new tools for data visualization and routines optimized for rapid
statistical calculations, including approaches making use of Bayesian
posterior distributions and parallel processing. Users can apply these
approaches toward screening datasets for phylogenetic/genomic information
content.

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

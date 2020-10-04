%global packname  RAM
%global packver   1.2.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1.7
Release:          2%{?dist}%{?buildtag}
Summary:          R for Amplicon-Sequencing-Based Microbial-Ecology

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-labdsv 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-VennDiagram 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RgoogleMaps 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-labdsv 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-VennDiagram 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-FD 
Requires:         R-MASS 
Requires:         R-CRAN-RgoogleMaps 
Requires:         R-lattice 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phytools 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-ape 

%description
Characterizing environmental microbiota diversity using amplicon-based
next generation sequencing (NGS) data. Functions are developed to
manipulate operational taxonomic unit (OTU) table, perform descriptive and
inferential statistics, and generate publication-quality plots.

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

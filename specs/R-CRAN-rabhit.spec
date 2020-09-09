%global packname  rabhit
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Inference Tool for Antibody Haplotype

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.7.1
BuildRequires:    R-CRAN-gtools >= 3.5.0
BuildRequires:    R-graphics >= 3.4.4
BuildRequires:    R-stats >= 3.4.4
BuildRequires:    R-methods >= 3.4.4
BuildRequires:    R-grid >= 3.4.4
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-dendextend >= 1.9.0
BuildRequires:    R-CRAN-plyr >= 1.8.5
BuildRequires:    R-CRAN-splitstackshape >= 1.4.8
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-stringi >= 1.4.3
BuildRequires:    R-CRAN-htmlwidgets >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-fastmatch >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-alakazam >= 1.0.0
BuildRequires:    R-CRAN-tigger >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-cowplot >= 0.9.1
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-gtable >= 0.3.0
BuildRequires:    R-CRAN-ggdendro >= 0.1.20
BuildRequires:    R-grDevices 
Requires:         R-CRAN-plotly >= 4.7.1
Requires:         R-CRAN-gtools >= 3.5.0
Requires:         R-graphics >= 3.4.4
Requires:         R-stats >= 3.4.4
Requires:         R-methods >= 3.4.4
Requires:         R-grid >= 3.4.4
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-dendextend >= 1.9.0
Requires:         R-CRAN-plyr >= 1.8.5
Requires:         R-CRAN-splitstackshape >= 1.4.8
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-stringi >= 1.4.3
Requires:         R-CRAN-htmlwidgets >= 1.3.0
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-fastmatch >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-alakazam >= 1.0.0
Requires:         R-CRAN-tigger >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-cowplot >= 0.9.1
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-gtable >= 0.3.0
Requires:         R-CRAN-ggdendro >= 0.1.20
Requires:         R-grDevices 

%description
Infers V-D-J haplotypes and gene deletions from AIRR-seq data, based on
IGHJ, IGHD or IGHV as anchor, by adapting a Bayesian framework. It also
calculates a Bayes factor, a number that indicates the certainty level of
the inference, for each haplotyped gene. Citation: Gidoni, et al (2019)
<doi:10.1038/s41467-019-08489-3>. Peres and Gidoni, et al (2019)
<doi:10.1093/bioinformatics/btz481>.

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

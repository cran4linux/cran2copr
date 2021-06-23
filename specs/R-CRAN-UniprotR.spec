%global __brp_check_rpaths %{nil}
%global packname  UniprotR
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieving Information of Proteins from Uniprot

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-grid 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-alakazam 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-gprofiler2 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-grid 
Requires:         R-graphics 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-alakazam 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-gprofiler2 

%description
Connect to Uniprot <https://www.uniprot.org/> to retrieve information
about proteins using their accession number such information could be name
or taxonomy information, For detailed information kindly read the
publication
<https://www.sciencedirect.com/science/article/pii/S1874391919303859>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

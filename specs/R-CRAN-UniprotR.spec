%global packname  UniprotR
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}
Summary:          Retrieving Information of Proteins from Uniprot

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-alakazam 
BuildRequires:    R-CRAN-curl 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyverse 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-alakazam 
Requires:         R-CRAN-curl 

%description
Connect to Uniprot <https://www.uniprot.org/> to retrieve information
about proteins using their accession number such information could be name
or taxonomy information, For detailed information kindly read the
publication
<https://www.sciencedirect.com/science/article/pii/S1874391919303859>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX

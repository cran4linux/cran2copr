%global packname  UCSCXenaShiny
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}
Summary:          A Shiny App for UCSC Xena Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-zip >= 2.0.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.3.2
BuildRequires:    R-CRAN-UCSCXenaTools >= 1.2.2
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-shinythemes >= 1.1.2
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-shinyBS >= 0.61
BuildRequires:    R-CRAN-DT >= 0.5
BuildRequires:    R-CRAN-shinyWidgets >= 0.4.8
BuildRequires:    R-CRAN-ggpubr >= 0.2
BuildRequires:    R-utils 
Requires:         R-CRAN-plotly >= 4.9.0
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-zip >= 2.0.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shiny >= 1.3.2
Requires:         R-CRAN-UCSCXenaTools >= 1.2.2
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-shinythemes >= 1.1.2
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-shinyBS >= 0.61
Requires:         R-CRAN-DT >= 0.5
Requires:         R-CRAN-shinyWidgets >= 0.4.8
Requires:         R-CRAN-ggpubr >= 0.2
Requires:         R-utils 

%description
Provides a web app for downloading, analyzing and visualizing datasets
from UCSC Xena (<http://xena.ucsc.edu/>), which is a collection of
UCSC-hosted public databases such as TCGA, ICGC, TARGET, GTEx, CCLE, and
others.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/modules_apps
%doc %{rlibdir}/%{packname}/shinyapp
%{rlibdir}/%{packname}/INDEX

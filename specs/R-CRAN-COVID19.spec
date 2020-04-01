%global packname  COVID19
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Coronavirus COVID-19 (2019-nCoV) Data Acquisition andVisualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-ggthemes 
Requires:         R-CRAN-devtools 
Requires:         R-utils 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-ggthemes 

%description
Pre-processed, ready-to-use, tidy format datasets of the 2019 Novel
Coronavirus COVID-19 (2019-nCoV) epidemic. The latest data are downloaded
in real-time, processed and merged with demographic indicators from
several trusted sources. The package implements advanced data
visualization across the space and time dimensions by means of animated
mapping. Besides worldwide data, the package includes granular data for
Italy, Switzerland and the Diamond Princess.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

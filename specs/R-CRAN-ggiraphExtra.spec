%global packname  ggiraphExtra
%global packver   0.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9
Release:          3%{?dist}%{?buildtag}
Summary:          Make Interactive 'ggplot2'. Extension to 'ggplot2' and 'ggiraph'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-ggiraph >= 0.3.2
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mycor 
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-grid 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-sjlabelled 
BuildRequires:    R-CRAN-sjmisc 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-webshot 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ztable 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-ggiraph >= 0.3.2
Requires:         R-CRAN-scales 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mycor 
Requires:         R-CRAN-ppcor 
Requires:         R-grid 
Requires:         R-mgcv 
Requires:         R-CRAN-sjlabelled 
Requires:         R-CRAN-sjmisc 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-webshot 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ztable 
Requires:         R-CRAN-RColorBrewer 

%description
Collection of functions to enhance 'ggplot2' and 'ggiraph'. Provides
functions for exploratory plots. All plot can be a 'static' plot or an
'interactive' plot using 'ggiraph'.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

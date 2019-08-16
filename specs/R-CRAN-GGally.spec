%global packname  GGally
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Extension to 'ggplot2'

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    openssl-devel
Requires:         openssl
BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-reshape >= 0.8.5
BuildRequires:    R-CRAN-gtable >= 0.2.0
BuildRequires:    R-CRAN-ggplot2 > 2.2.0
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-reshape >= 0.8.5
Requires:         R-CRAN-gtable >= 0.2.0
Requires:         R-CRAN-ggplot2 > 2.2.0
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
The R package 'ggplot2' is a plotting system based on the grammar of
graphics. 'GGally' extends 'ggplot2' by adding several functions to reduce
the complexity of combining geometric objects with transformed data. Some
of these functions include a pairwise plot matrix, a two group pairwise
plot matrix, a parallel coordinates plot, a survival plot, and several
functions to plot networks.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

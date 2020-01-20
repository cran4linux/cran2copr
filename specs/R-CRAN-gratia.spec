%global packname  gratia
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Graceful 'ggplot'-Based Graphics and Other Functions for GAMsFitted Using 'mgcv'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-grDevices 
Requires:         R-mgcv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cowplot 
Requires:         R-grid 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-grDevices 

%description
Graceful 'ggplot'-based graphics and utility functions for working with
generalized additive models (GAMs) fitted using the 'mgcv' package.
Provides a reimplementation of the plot() method for GAMs that 'mgcv'
provides, as well as 'tidyverse' compatible representations of estimated
smooths.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

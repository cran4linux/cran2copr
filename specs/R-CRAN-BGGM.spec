%global packname  BGGM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Bayesian Gaussian Graphical Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-sna >= 2.5
BuildRequires:    R-CRAN-pracma >= 2.2.5
BuildRequires:    R-CRAN-bayesplot >= 1.7.1
BuildRequires:    R-CRAN-foreach >= 1.4.7
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-GGally >= 1.4.0
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-network >= 1.15
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-mvtnorm >= 1.0.11
BuildRequires:    R-CRAN-cowplot >= 1.0.0
BuildRequires:    R-CRAN-ggridges >= 0.5.1
BuildRequires:    R-CRAN-mvnfast >= 0.2.5
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-MASS 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-sna >= 2.5
Requires:         R-CRAN-pracma >= 2.2.5
Requires:         R-CRAN-bayesplot >= 1.7.1
Requires:         R-CRAN-foreach >= 1.4.7
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-GGally >= 1.4.0
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-network >= 1.15
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-mvtnorm >= 1.0.11
Requires:         R-CRAN-cowplot >= 1.0.0
Requires:         R-CRAN-ggridges >= 0.5.1
Requires:         R-CRAN-mvnfast >= 0.2.5
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-Matrix 
Requires:         R-CRAN-reshape 
Requires:         R-MASS 

%description
Fit Bayesian Gaussian graphical models. The methods are separated into two
Bayesian approaches for inference: hypothesis testing and estimation.
There are extensions for confirmatory hypothesis testing, comparing
Gaussian graphical models, and node wise predictability. These methods
were recently introduced in the Gaussian graphical model literature,
including Williams (2019) <doi:10.31234/osf.io/x8dpr>, Williams and Mulder
(2019) <doi:10.31234/osf.io/ypxd8>, Williams, Rast, Pericchi, and Mulder
(2019) <doi:10.31234/osf.io/yt386>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

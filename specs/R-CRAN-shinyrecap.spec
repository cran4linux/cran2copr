%global __brp_check_rpaths %{nil}
%global packname  shinyrecap
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Shiny User Interface for Multiple Source Capture RecaptureModels

License:          MIT + file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcapture 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-conting 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-CARE1 
BuildRequires:    R-CRAN-dga 
BuildRequires:    R-CRAN-LCMCR 
BuildRequires:    R-CRAN-ipc 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-Rcapture 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-conting 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-CARE1 
Requires:         R-CRAN-dga 
Requires:         R-CRAN-LCMCR 
Requires:         R-CRAN-ipc 
Requires:         R-CRAN-future 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-testthat 

%description
Implements user interfaces for log-linear models, Bayesian model averaging
and Bayesian Dirichlet process mixture models.

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
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/apps
%{rlibdir}/%{packname}/INDEX

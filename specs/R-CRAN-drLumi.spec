%global packname  drLumi
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Multiplex Immunoassays Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-msm 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-minpack.lm 
Requires:         R-stats 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-msm 

%description
Contains quality control routines for multiplex immunoassay data,
including several approaches for: treating the background noise of the
assay, fitting the dose-response curves and estimating the limits of
quantification.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX

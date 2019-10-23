%global packname  MarketMatching
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Market Matching and Causal Impact Inference

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-CausalImpact 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-bsts 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-dtw 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-CausalImpact 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-bsts 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-dtw 

%description
For a given test market find the best control markets using time series
matching and analyze the impact of an intervention. The intervention could
be be a marketing event or some other local business tactic that is being
tested. The workflow implemented in the Market Matching package utilizes
dynamic time warping (the 'dtw' package) to do the matching and the
'CausalImpact' package to analyze the causal impact. In fact, this package
can be considered a "workflow wrapper" for those two packages.

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

%global packname  cassandRa
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Finds Missing Links and Metric Confidence Intervals inEcological Bipartite Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-vegan >= 2.5.3
BuildRequires:    R-CRAN-bipartite >= 2.11
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-tidyr >= 0.8
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-boot 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-vegan >= 2.5.3
Requires:         R-CRAN-bipartite >= 2.11
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-tidyr >= 0.8
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-dplyr 
Requires:         R-boot 

%description
Provides methods to deal with under sampling in ecological bipartite
networks. Includes tools to fit a variety of statistical network models
and sample coverage estimators to highlight most likely missing links.
Also includes simple functions to resample from observed networks to
generate confidence intervals for common ecological network metrics.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

%global packname  SUMMER
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Spatio-Temporal Under-Five Mortality Methods for Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-survey 
Requires:         R-stats 
Requires:         R-CRAN-spdep 
Requires:         R-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-sp 

%description
Provides methods for estimating, projecting, and plotting spatio-temporal
under-five mortality rates, described in Mercer et al. (2015)
<doi:10.1214/15-AOAS872> and Li et al. (2019)
<doi:10.1371/journal.pone.0210645>.

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

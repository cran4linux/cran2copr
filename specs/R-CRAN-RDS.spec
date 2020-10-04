%global packname  RDS
%global packver   0.9-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          4%{?dist}%{?buildtag}
Summary:          Respondent-Driven Sampling

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.1
Requires:         R-core >= 2.5.1
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-statnet.common 
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-isotone 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-methods 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-network 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-statnet.common 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-isotone 

%description
Provides functionality for carrying out estimation with data collected
using Respondent-Driven Sampling. This includes Heckathorn's RDS-I and
RDS-II estimators as well as Gile's Sequential Sampling estimator. The
package is part of the "RDS Analyst" suite of packages for the analysis of
respondent-driven sampling data. See Gile and Handcock (2010)
<doi:10.1111/j.1467-9531.2010.01223.x> and Gile and Handcock (2015)
<doi:10.1111/rssa.12091>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

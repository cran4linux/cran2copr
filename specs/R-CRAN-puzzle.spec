%global __brp_check_rpaths %{nil}
%global packname  puzzle
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Assembling Data Sets for Non-Linear Mixed Effects Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-readr 
Requires:         R-utils 
Requires:         R-CRAN-lubridate 
Requires:         R-stats 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-readr 

%description
To Simplify the time consuming and error prone task of assembling complex
data sets for non-linear mixed effects modeling. Users are able to select
from different absorption processes such as zero and first order, or a
combination of both. Furthermore, data sets containing data from several
entities, responses, and covariates can be simultaneously assembled.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

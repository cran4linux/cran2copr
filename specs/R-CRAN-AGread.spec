%global packname  AGread
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Read Data Files from ActiGraph Monitors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-seewave >= 2.0.5
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-GGIR >= 1.5.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-DescTools >= 0.99.20
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-binaryLogic >= 0.3.9
BuildRequires:    R-CRAN-anytime >= 0.3.0
BuildRequires:    R-CRAN-PAutilities >= 0.2.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-seewave >= 2.0.5
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-GGIR >= 1.5.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-DescTools >= 0.99.20
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-binaryLogic >= 0.3.9
Requires:         R-CRAN-anytime >= 0.3.0
Requires:         R-CRAN-PAutilities >= 0.2.0
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-stats 
Requires:         R-utils 

%description
Standardize the process of bringing various modes of output files into R.
Additionally, processes are provided to read and minimally pre- process
raw data from primary accelerometer and inertial measurement unit files,
as well as binary .gt3x files. ActiGraph monitors are used to estimate
physical activity outcomes via body-worn sensors that measure (e.g.)
acceleration or rotational velocity.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

%global packname  aemo
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Download and Process AEMO Price and Demand Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.3.3
BuildRequires:    R-CRAN-stringr >= 0.6.2
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-lubridate >= 1.3.3
Requires:         R-CRAN-stringr >= 0.6.2
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-stats 
Requires:         R-utils 

%description
Download and process real time trading prices and demand data freely
provided by the Australian Energy Market Operator (AEMO). Note that this
includes a sample data set.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

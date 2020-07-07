%global packname  tigerhitteR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Pre-Process of Time Series Data Set in R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 3.17.4
BuildRequires:    R-CRAN-openxlsx >= 3.0.0
BuildRequires:    R-CRAN-zoo >= 1.7.13
BuildRequires:    R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-Hmisc >= 3.17.4
Requires:         R-CRAN-openxlsx >= 3.0.0
Requires:         R-CRAN-zoo >= 1.7.13
Requires:         R-CRAN-magrittr >= 1.5

%description
Pre-process for discrete time series data set which is not continuous at
the column of 'date'. Refilling records of missing 'date' and other
columns to the hollow data set so that final data set is able to be dealt
with time series analysis.

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
%{rlibdir}/%{packname}/INDEX

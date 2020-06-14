%global packname  PhysActBedRest
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Marks Periods of 'Bedrest' in Actigraph Accelerometer Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lubridate 

%description
Contains a function to categorize accelerometer readings collected in
free-living (e.g., for 24 hours/day for 7 days), preprocessed and
compressed as counts (unit-less value) in a specified time period termed
epoch (e.g., 1 minute) as either bedrest (sleep) or active.  The input is
a matrix with a timestamp column and a column with number of counts per
epoch. The output is the same dataframe with an additional column termed
bedrest. In the bedrest column each line (epoch) contains a
function-generated classification 'br' or 'a' denoting bedrest/sleep and
activity, respectively.  The package is designed to be used after
wear/nonwear marking function in the 'PhysicalActivity' package.

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

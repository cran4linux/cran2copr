%global packname  rsatscan
%global packver   0.3.9200
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9200
Release:          1%{?dist}
Summary:          Tools, Classes, and Methods for Interfacing with SaTScanStand-Alone Software

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-foreign 
Requires:         R-utils 
Requires:         R-foreign 

%description
SaTScan(TM) (http://www.satscan.org) is software for finding regions in
Time, Space, or Time-Space that have excess risk, based on scan
statistics, and uses Monte Carlo hypothesis testing to generate P-values
for these regions.  The rsatscan package provides functions for writing R
data frames in SaTScan-readable formats, for setting SaTScan parameters,
for running SaTScan in the OS, and for reading the files that SaTScan
creates.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

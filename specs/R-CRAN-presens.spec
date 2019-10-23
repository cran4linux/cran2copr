%global packname  presens
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Interface for PreSens Fiber Optic Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-marelac >= 2.1.4
BuildRequires:    R-CRAN-measurements 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-marelac >= 2.1.4
Requires:         R-CRAN-measurements 
Requires:         R-stats 
Requires:         R-utils 

%description
Makes output files from select PreSens Fiber Optic Oxygen Transmitters
easier to work with in R. See <http://www.presens.de> for more information
about PreSens (Precision Sensing GmbH). Note: this package is neither
created nor maintained by PreSens.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

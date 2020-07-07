%global packname  wildlifeDI
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Calculate Indices of Dynamic Interaction for Wildlife TrackingData

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-adehabitatLT 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-adehabitatLT 
Requires:         R-stats 
Requires:         R-graphics 

%description
Dynamic interaction refers to spatial-temporal associations in the
movements of two (or more) animals. This package provides tools for
calculating a suite of indices used for quantifying dynamic interaction
with wildlife telemetry data. For more information on each of the methods
employed see the references within. The package (as of version 0.3) also
has new tools for automating contact analysis in large tracking datasets.
The package draws heavily on the classes and methods developed in the
'adehabitat' packages.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

%global packname  magicaxis
%global packver   2.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.10
Release:          3%{?dist}
Summary:          Pretty Scientific Plotting with Minor-Tick and Log Minor-TickSupport

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-celestial >= 1.4.1
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-celestial >= 1.4.1
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-RColorBrewer 

%description
Functions to make useful (and pretty) plots for scientific plotting.
Additional plotting features are added for base plotting, with particular
emphasis on making attractive log axis plots.

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

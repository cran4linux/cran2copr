%global packname  TreeDep
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Air Pollution Removal by Dry Deposition on Trees

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-ggplot2 

%description
The model estimates air pollution removal by dry deposition on trees. It
also estimates or uses hourly values for aerodynamic resistance, boundary
layer resistance, canopy resistance, stomatal resistance, cuticular
resistance, mesophyll resistance, soil resistance, friction velocity and
deposition velocity. It also allows plotting graphical results for a
specific time period. The pollutants are nitrogen dioxide, ozone, sulphur
dioxide, carbon monoxide and particulate matter. Baldocchi D (1994)
<doi:10.1093/treephys/14.7-8-9.1069>. Farquhar GD, von Caemmerer S, Berry
JA (1980) Planta 149: 78-90. Hirabayashi S, Kroll CN, Nowak DJ (2015)
i-Tree Eco Dry Deposition Model. Nowak DJ, Crane DE, Stevens JC (2006)
<doi:10.1016/j.ufug.2006.01.007>. US EPA (1999) PCRAMMET User's Guide.
EPA-454/B-96-001. Weiss A, Norman JM (1985) Agricultural and Forest
Meteorology 34: 205—213.

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

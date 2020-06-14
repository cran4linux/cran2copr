%global packname  multifluo
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Dealing with Several Images of a Same Object Constituted ofDifferent Zones

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-agricolae 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-imager 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-agricolae 

%description
Deals with several images of a same object, constituted of different
zones. Each image constitutes a variable for a given pixel. The user can
interactively select different zones of an image. Then, multivariate
analysis (PCA) can be run in order to characterize the different selected
zones, according to the different images. Hotelling (Hotelling, 1931,
<doi:10.1214/aoms/1177732979>) and Srivastava (Srivastava, 2009,
<doi:10.1016/j.jmva.2006.11.002>) tests can be run to detect multivariate
differences between the zones.

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

%global packname  LS2Wstat
%global packver   2.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          A Multiscale Test of Spatial Stationarity for LS2W Processes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-LS2W >= 1.3.1
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-spdep 
Requires:         R-CRAN-LS2W >= 1.3.1
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-geoR 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-spdep 

%description
Wavelet-based methods for testing stationarity and quadtree segmenting of
images, see Taylor et al (2014) <doi:10.1080/00401706.2013.823890>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

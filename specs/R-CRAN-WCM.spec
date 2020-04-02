%global packname  WCM
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Water Cloud Model (WCM) for the Simulation of Leaf Area Index(LAI) and Soil Moisture (SM) from Microwave Backscattering

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-raster 

%description
Retrieval the leaf area index (LAI) and soil moisture (SM) from microwave
backscattering data using water cloud model (WCM) model . The WCM
algorithm attributed to Pervot et al.(1993)
<doi:10.1016/0034-4257(93)90053-Z>. The authors are grateful to SAC, ISRO,
Ahmedabad for providing financial support to Dr. Prashant K Srivastava to
conduct this research work.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

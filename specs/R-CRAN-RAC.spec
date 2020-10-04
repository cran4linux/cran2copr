%global packname  RAC
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}%{?buildtag}
Summary:          R Package for Aqua Culture

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-raster 

%description
Solves the individual bioenergetic balance for different aquaculture sea
fish (Sea Bream and Sea Bass; Brigolin et al., 2014
<doi:10.3354/aei00093>) and shellfish (Mussel and Clam; Brigolin et al.,
2009 <doi:10.1016/j.ecss.2009.01.029>; Solidoro et al., 2000
<doi:10.3354/meps199137>). Allows for spatialized model runs and
population simulations.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

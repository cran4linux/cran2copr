%global packname  agroclim
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Climatic Indices for Agriculture

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-easyNCDF 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-multiApply 
BuildRequires:    R-tools 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-easyNCDF 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-multiApply 
Requires:         R-tools 

%description
Collection of functions to compute agroclimatic indices useful to zoning
areas based on climatic variables and to evaluate the importance of
temperature and precipitation for individual crops, or in general for
agricultural lands. Some of the indices are adapted from Gladstones (1992,
ISBN:1875130128); Trnka et al. (2014) <doi:10.1038/nclimate2242>; Wrinkler
et al. (1974, ISBN:9780520025912); Jones et al. (2010)
<doi:10.1111/j.1755-0238.2010.00100.x>; Huglin (1978)
<https://prodinra.inra.fr/record/116105>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

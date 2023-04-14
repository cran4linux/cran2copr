%global __brp_check_rpaths %{nil}
%global packname  phenomap
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Projecting Satellite-Derived Phenology in Space

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-phenex 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-phenex 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-doParallel 

%description
This tool projects annual phenology metrics and long-term phenology
trends, following methodologies described in John (2016)
<https://etda.libraries.psu.edu/catalog/13521clj5135>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

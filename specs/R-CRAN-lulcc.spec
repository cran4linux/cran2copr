%global __brp_check_rpaths %{nil}
%global packname  lulcc
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Land Use Change Modelling in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-rasterVis 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ROCR 
Requires:         R-lattice 
Requires:         R-CRAN-rasterVis 

%description
Classes and methods for spatially explicit land use change modelling in R.

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

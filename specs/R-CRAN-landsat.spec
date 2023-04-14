%global __brp_check_rpaths %{nil}
%global packname  landsat
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Radiometric and Topographic Correction of Satellite Imagery

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.0
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-lmodel2 
BuildRequires:    R-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
Requires:         R-CRAN-sp >= 1.0
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-lmodel2 
Requires:         R-mgcv 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 

%description
Processing of Landsat or other multispectral satellite imagery. Includes
relative normalization, image-based radiometric correction, and
topographic correction options.

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

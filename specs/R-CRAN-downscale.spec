%global packname  downscale
%global packver   3.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          2%{?dist}
Summary:          Downscaling Species Occupancy

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.4.20
BuildRequires:    R-CRAN-sp >= 1.2.0
BuildRequires:    R-CRAN-minpack.lm >= 1.1.9
BuildRequires:    R-CRAN-cubature >= 1.1.2
BuildRequires:    R-CRAN-Rmpfr >= 0.5.7
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-raster >= 2.4.20
Requires:         R-CRAN-sp >= 1.2.0
Requires:         R-CRAN-minpack.lm >= 1.1.9
Requires:         R-CRAN-cubature >= 1.1.2
Requires:         R-CRAN-Rmpfr >= 0.5.7
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 

%description
Downscales species occupancy at coarse grain sizes to predict species
occupancy at fine grain sizes. Ten models are provided to fit and
extrapolate the occupancy-area relationship, as well as methods for
preparing atlas data for modelling. See Marsh et. al. (2018)
doi:10.18637/jss.v086.c03.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

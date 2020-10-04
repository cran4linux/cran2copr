%global packname  geoTS
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Methods for Handling and Analyzing Time Series of SatelliteImages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.3
Requires:         R-core >= 2.15.3
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.6.1
BuildRequires:    R-CRAN-raster >= 2.9.5
BuildRequires:    R-CRAN-ff >= 2.2.14
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-sp >= 1.2.0
BuildRequires:    R-CRAN-doParallel >= 1.0.14
BuildRequires:    R-CRAN-iterators >= 1.0.10
BuildRequires:    R-methods 
Requires:         R-parallel >= 3.6.1
Requires:         R-CRAN-raster >= 2.9.5
Requires:         R-CRAN-ff >= 2.2.14
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-sp >= 1.2.0
Requires:         R-CRAN-doParallel >= 1.0.14
Requires:         R-CRAN-iterators >= 1.0.10
Requires:         R-methods 

%description
Provides functions and methods for: splitting large raster objects into
smaller chunks, transferring images from a binary format into raster
layers, transferring raster layers into an 'RData' file, calculating the
maximum gap (amount of consecutive missing values) of a numeric vector,
and fitting harmonic regression to periodic time series. The methods
implemented for harmonic regression are based on G. Roerink, M. Menenti
and W. Verhoef (2000) <doi:10.1080/014311600209814>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

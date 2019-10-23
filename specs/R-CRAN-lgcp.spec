%global packname  lgcp
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Log-Gaussian Cox Process

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 1.50.0
BuildRequires:    R-CRAN-rpanel >= 1.1.3
BuildRequires:    R-CRAN-spatstat.utils 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-rgeos 
Requires:         R-CRAN-spatstat >= 1.50.0
Requires:         R-CRAN-rpanel >= 1.1.3
Requires:         R-CRAN-spatstat.utils 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-tcltk 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-ncdf4 
Requires:         R-methods 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-maptools 
Requires:         R-Matrix 
Requires:         R-CRAN-rgeos 

%description
Spatial and spatio-temporal modelling of point patterns using the
log-Gaussian Cox process. Bayesian inference for spatial, spatiotemporal,
multivariate and aggregated point processes using Markov chain Monte
Carlo.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

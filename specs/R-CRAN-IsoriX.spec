%global packname  IsoriX
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          3%{?dist}
Summary:          Isoscape Computation and Inference of Spatial Origins usingMixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spaMM >= 2.4
BuildRequires:    R-CRAN-rasterVis >= 0.30
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-spaMM >= 2.4
Requires:         R-CRAN-rasterVis >= 0.30
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-viridisLite 

%description
Building isoscapes using mixed models and inferring the geographic origin
of samples based on their isotopic ratios. This package is essentially a
simplified interface to several other packages which implements a new
statistical framework based on mixed models. It uses 'spaMM' for fitting
and predicting isoscapes, and assigning an organism's origin depending on
its isotopic ratio. 'IsoriX' also relies heavily on the package
'rasterVis' for plotting the maps produced with 'raster' using 'lattice'.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX

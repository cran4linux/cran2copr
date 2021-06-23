%global __brp_check_rpaths %{nil}
%global packname  rasterList
%global packver   0.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          3%{?dist}%{?buildtag}
Summary:          A Raster Where Cells are Generic Objects

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
Requires:         R-CRAN-raster 
Requires:         R-methods 

%description
A S4 class has been created such that complex operations can be executed
on each cells of a raster map. The raster of objects contains the
traditional raster map with the addition of a list of generic objects: one
object for each raster cells. It allows to write few lines of R code for
complex map algebra. Two environmental applications about frequency
analysis of raster map of precipitation and creation of a raster map of
soil water retention curves have been presented.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/example_scripts
%doc %{rlibdir}/%{packname}/map
%{rlibdir}/%{packname}/INDEX

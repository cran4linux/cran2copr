%global packname  satellite
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Handling and Manipulating Remote Sensing Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.10.3
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-tools 
BuildRequires:    R-stats4 
Requires:         R-CRAN-Rcpp >= 0.10.3
Requires:         R-CRAN-raster 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-plyr 
Requires:         R-tools 
Requires:         R-stats4 

%description
Herein, we provide a broad variety of functions which are useful for
handling, manipulating, and visualizing satellite-based remote sensing
data. These operations range from mere data import and layer handling (eg
subsetting), over Raster* typical data wrangling (eg crop, extend), to
more sophisticated (pre-)processing tasks typically applied to satellite
imagery (eg atmospheric and topographic correction). This functionality is
complemented by a full access to the satellite layers' metadata at any
stage and the documentation of performed actions in a separate log file.
Currently available sensors include Landsat 4-5 (TM), 7 (ETM+), and 8
(OLI/TIRS Combined), and additional compatibility is ensured for the
Landsat Global Land Survey data set.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

%global packname  TreeLS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Terrestrial Point Cloud Processing of Forest Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-raster >= 2.8.19
BuildRequires:    R-CRAN-lidR >= 2.0.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-rgl >= 0.99.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-raster >= 2.8.19
Requires:         R-CRAN-lidR >= 2.0.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-rgl >= 0.99.0

%description
Algorithms for tree detection, noise removal, stem modelling, 3D
visualization and manipulation of terrestrial 'LiDAR' (but not only) point
clouds, currently focusing on high performance applications for forest
inventory - being fully compatible with the 'LAS' infrastructure provided
by 'lidR'. For in depth descriptions of the stem classification and
segmentation algorithms check out Conto et al. (2017)
<doi:10.1016/j.compag.2017.10.019>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

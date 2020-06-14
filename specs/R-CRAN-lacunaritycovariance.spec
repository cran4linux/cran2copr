%global packname  lacunaritycovariance
%global packver   1.0-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.13
Release:          2%{?dist}
Summary:          Gliding Box Lacunarity and Other Metrics for 2D Random ClosedSets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-RcppRoll 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-RcppRoll 

%description
Functions for estimating the gliding box lacunarity (GBL), covariance, and
pair-correlation of a random closed set (RACS) in 2D from a binary
coverage map (e.g. presence-absence land cover maps).  Contains a number
of newly-developed covariance-based estimators of GBL (Hingee et al.,
2019) <doi:10.1007/s13253-019-00351-9> and balanced estimators, proposed
by Picka (2000) <http://www.jstor.org/stable/1428408>, for covariance,
centred covariance, and pair-correlation.  Also contains methods for
estimating contagion-like properties of RACS and simulating 2D Boolean
models.  Binary coverage maps are usually represented as raster images
with pixel values of TRUE, FALSE or NA, with NA representing unobserved
pixels.  A demo for extracting such a binary map from a geospatial data
format is provided.  Binary maps may also be represented using polygonal
sets as the foreground, however for most computations such maps are
converted into raster images.  The package is based on research conducted
during the author's PhD studies.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

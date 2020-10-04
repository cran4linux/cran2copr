%global packname  RGCxGC
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Preprocessing and Multivariate Analysis of Bidimensional GasChromatography Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-colorRamps >= 2.3
BuildRequires:    R-CRAN-ptw >= 1.9.13
BuildRequires:    R-CRAN-RNetCDF >= 1.9.1
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-prettydoc >= 0.2
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-CRAN-colorRamps >= 2.3
Requires:         R-CRAN-ptw >= 1.9.13
Requires:         R-CRAN-RNetCDF >= 1.9.1
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-prettydoc >= 0.2
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 

%description
Implementation of chemometrics analysis for bidimensional gas
chromatography data. This package can handle data for common scientific
data format (netCDF) and fold it to 2D chromatogram. Then, it can perform
preprocessing and multivariate analysis. In the preprocessing algorithms,
baseline correction, smoothing, and peak alignment are available. While in
multivariate analysis, multiway principal component analysis is
incorporated.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX

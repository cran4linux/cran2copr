%global packname  apcf
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Adapted Pair Correlation Function

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel >= 2.0.0
BuildRequires:    geos-devel >= 3.4.0
Requires:         gdal
Requires:         geos
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp >= 0.12
Requires:         R-graphics 

%description
The adapted pair correlation function transfers the concept of the pair
correlation function from point patterns to patterns of objects of finite
size and irregular shape (e.g. lakes within a country). This is a
reimplementation of the method suggested by Nuske et al. (2009)
<doi:10.1016/j.foreco.2009.09.050> using the libraries 'GEOS' and 'GDAL'
directly instead of through 'PostGIS'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shapes
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

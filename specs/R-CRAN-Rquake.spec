%global packname  Rquake
%global packver   2.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          3%{?dist}
Summary:          Seismic Hypocenter Determination

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12
Requires:         R-core >= 2.12
BuildArch:        noarch
BuildRequires:    R-CRAN-RPMG 
BuildRequires:    R-CRAN-RSEIS 
BuildRequires:    R-CRAN-GEOmap 
BuildRequires:    R-CRAN-MBA 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-RPMG 
Requires:         R-CRAN-RSEIS 
Requires:         R-CRAN-GEOmap 
Requires:         R-CRAN-MBA 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-rgl 

%description
Hypocenter estimation and analysis of seismic data collected continuously,
or in trigger mode. The functions organize other functions from RSEIS and
GEOmap to help researchers pick, locate, and store hypocenters for
detailed seismic investigation.

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
%{rlibdir}/%{packname}/INDEX

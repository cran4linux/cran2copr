%global packname  RSEIS
%global packver   3.9-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.9.0
Release:          3%{?dist}
Summary:          Seismic Time Series Analysis Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-RPMG 
BuildRequires:    R-CRAN-Rwave 
Requires:         R-CRAN-RPMG 
Requires:         R-CRAN-Rwave 

%description
Multiple interactive codes to view and analyze seismic data, via spectrum
analysis, wavelet transforms, particle motion, hodograms.  Includes
general time-series tools, plotting, filtering, interactive display.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/vignettes
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

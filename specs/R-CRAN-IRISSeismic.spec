%global packname  IRISSeismic
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}
Summary:          Classes and Methods for Seismic Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-seismicRoll >= 1.1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-stats 
Requires:         R-CRAN-seismicRoll >= 1.1.0
Requires:         R-methods 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-XML 
Requires:         R-stats 

%description
Provides classes and methods for seismic data analysis. The base classes
and methods are inspired by the python code found in the 'ObsPy' python
toolbox <https://github.com/obsypy/obspy>. Additional classes and methods
support data returned by web services provided by the 'IRIS DMC'
<http://service.iris.edu/>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

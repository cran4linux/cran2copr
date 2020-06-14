%global packname  spacetime
%global packver   1.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          2%{?dist}
Summary:          Classes and Methods for Spatio-Temporal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.9
BuildRequires:    R-CRAN-sp >= 1.1.0
BuildRequires:    R-CRAN-xts >= 0.8.8
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-intervals 
Requires:         R-CRAN-zoo >= 1.7.9
Requires:         R-CRAN-sp >= 1.1.0
Requires:         R-CRAN-xts >= 0.8.8
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-CRAN-intervals 

%description
Classes and methods for spatio-temporal data, including space-time regular
lattices, sparse lattices, irregular data, and trajectories; utility
functions for plotting data as map sequences (lattice or animation) or
multiple time series; methods for spatial and temporal selection and
subsetting, as well as for spatial/temporal/spatio-temporal matching or
aggregation, retrieving coordinates, print, summary, etc.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

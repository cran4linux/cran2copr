%global __brp_check_rpaths %{nil}
%global packname  stressr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fetch and plot financial stress index and component data.

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-XML 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 

%description
Forms queries to submit to the Cleveland Federal Reserve Bank web site's
financial stress index data site.  Provides query functions for both the
composite stress index and the components data. By default the download
includes daily time series data starting September 25, 1991.  The
functions return a class of either type easing or cfsi which contain a
list of items related to the query and its graphical presentation.  The
list includes the time series data as an xts object.  The package provides
four lattice time series plots to render the time series data in a manner
similar to the bank's own presentation.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

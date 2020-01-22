%global packname  IDPmisc
%global packver   1.1.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.20
Release:          1%{?dist}
Summary:          'Utilities of Institute of Data Analyses and Process Design(www.zhaw.ch/idp)'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-lattice 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-lattice 

%description
Different high-level graphics functions for displaying large datasets,
displaying circular data in a very flexible way, finding local maxima,
brewing color ramps, drawing nice arrows, zooming 2D-plots, creating
figures with differently colored margin and plot region.  In addition, the
package contains auxiliary functions for data manipulation like omitting
observations with irregular values or selecting data by logical vectors,
which include NAs. Other functions are especially useful in spectroscopy
and analyses of environmental data: robust baseline fitting, finding peaks
in spectra, converting humidity measures.

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
%{rlibdir}/%{packname}/libs

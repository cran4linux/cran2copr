%global packname  vegan
%global packver   2.5-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.6
Release:          2%{?dist}
Summary:          Community Ecology Package

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-permute >= 0.9.0
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-cluster 
BuildRequires:    R-mgcv 
Requires:         R-CRAN-permute >= 0.9.0
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-cluster 
Requires:         R-mgcv 

%description
Ordination methods, diversity analysis and other functions for community
and vegetation ecologists.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/OldChangeLog
%doc %{rlibdir}/%{packname}/ONEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

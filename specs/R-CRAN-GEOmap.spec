%global packname  GEOmap
%global packver   2.4-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.4
Release:          3%{?dist}
Summary:          Topographic and Geologic Mapping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-RPMG 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-MBA 
Requires:         R-CRAN-RPMG 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-MBA 

%description
Set of routines for making Map Projections (forward and inverse),
Topographic Maps, Perspective plots, Geological Maps, geological map
symbols, geological databases, interactive plotting and selection of focus
regions.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

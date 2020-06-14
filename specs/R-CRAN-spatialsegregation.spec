%global packname  spatialsegregation
%global packver   2.45
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.45
Release:          2%{?dist}
Summary:          Segregation Measures for Multitype Spatial Point Patterns

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-spatstat 
Requires:         R-CRAN-spatstat 

%description
Summaries for measuring segregation/mingling in multitype spatial point
patterns with graph based neighbourhood description. Included indices:
Mingling, Shannon, Simpson (also the non-spatial) Included functionals:
Mingling, Shannon, Simpson, ISAR, MCI. Included neighbourhoods: Geometric,
k- nearest neighbours, Gabriel, Delaunay. Dixon's test.

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

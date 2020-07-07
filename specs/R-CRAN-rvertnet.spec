%global packname  rvertnet
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          3%{?dist}
Summary:          Search 'Vertnet', a 'Database' of Vertebrate Specimen Records

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-crul >= 0.5.2
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-maps 
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-crul >= 0.5.2
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-maps 

%description
Retrieve, map and summarize data from the 'VertNet.org' archives
(<http://vertnet.org/>).  Functions allow searching by many parameters,
including 'taxonomic' names, places, and dates. In addition, there is an
interface for conducting spatially delimited searches, and another for
requesting large 'datasets' via email.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX

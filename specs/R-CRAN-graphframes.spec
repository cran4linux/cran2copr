%global packname  graphframes
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Interface for 'GraphFrames'

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sparklyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-forge 
Requires:         R-CRAN-sparklyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-forge 

%description
A 'sparklyr' <https://spark.rstudio.com/> extension that provides an R
interface for 'GraphFrames' <https://graphframes.github.io/>.
'GraphFrames' is a package for 'Apache Spark' that provides a
DataFrame-based API for working with graphs. Functionality includes motif
finding and common graph algorithms, such as PageRank and Breadth-first
search.

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
%{rlibdir}/%{packname}/INDEX

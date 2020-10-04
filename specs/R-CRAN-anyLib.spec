%global packname  anyLib
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Install and Load Any Package from CRAN, Bioconductor or Github

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-BiocManager 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-BiocManager 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 

%description
Made to make your life simpler with packages, by installing and loading a
list of packages, whether they are on CRAN, Bioconductor or github. For
github, if you do not have the full path, with the maintainer name in it
(e.g. "achateigner/topReviGO"), it will be able to load it but not to
install it.

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
%doc %{rlibdir}/%{packname}/dummyPackage_0.1.0.tar.gz
%{rlibdir}/%{packname}/INDEX

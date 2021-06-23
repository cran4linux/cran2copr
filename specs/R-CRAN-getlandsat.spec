%global __brp_check_rpaths %{nil}
%global packname  getlandsat
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Get Landsat 8 Data from Amazon Public Data Sets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-crul >= 0.5.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rappdirs 
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-crul >= 0.5.2
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rappdirs 

%description
Get Landsat 8 Data from Amazon Web Services ('AWS') public data sets
(<https://registry.opendata.aws/landsat-8/>). Includes functions for
listing images and fetching them, and handles caching to prevent
unnecessary additional requests.

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
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX

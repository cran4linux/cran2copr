%global packname  AntWeb
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          3%{?dist}%{?buildtag}
Summary:          programmatic interface to the AntWeb

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-leafletR >= 0.1.1
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-leafletR >= 0.1.1
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-httr 

%description
A complete programmatic interface to the AntWeb database from the
California Academy of Sciences.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AntWeb_guide.Rmd
%{rlibdir}/%{packname}/INDEX

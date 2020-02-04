%global packname  Ecfun
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Functions for Ecdat

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-tis 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-BMA 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-tis 
Requires:         R-CRAN-jpeg 
Requires:         R-MASS 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-stringi 
Requires:         R-methods 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-BMA 
Requires:         R-CRAN-mvtnorm 

%description
Functions to update data sets in Ecdat and to create, manipulate, plot,
and analyze those and similar data sets.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

%global __brp_check_rpaths %{nil}
%global packname  leanpubr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          'Leanpub' API Interface

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 

%description
Provides access to the 'Leanpub' API <https://leanpub.com/help/api> for
gathering information about publications and submissions to the 'Leanpub'
platform.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

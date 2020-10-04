%global packname  boxr
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          3%{?dist}%{?buildtag}
Summary:          Interface for the 'Box.com API'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-fs 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
An R interface for the remote file hosting service 'Box'
(<https://www.box.com/>). In addition to uploading and downloading files,
this package includes functions which mirror base R operations for local
files, (e.g. box_load(), box_save(), box_read(), box_setwd(), etc.), as
well as 'git' style functions for entire directories (e.g. box_fetch(),
box_push()).

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
%doc %{rlibdir}/%{packname}/secret
%{rlibdir}/%{packname}/INDEX

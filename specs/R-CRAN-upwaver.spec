%global packname  upwaver
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Access 'Upwave' API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-XLConnect 
BuildRequires:    R-CRAN-xlsx 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-XLConnect 
Requires:         R-CRAN-xlsx 

%description
'Upwave' <https://www.upwave.io/> is a task management app organising
tasks on boards and cards. 'upwaver' is a wrapper around the 'Upwave' API
<https://upwavehq.github.io/api/> that allows listing and updating those
boards and cards.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

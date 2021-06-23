%global __brp_check_rpaths %{nil}
%global packname  cmmr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          CEU Mass Mediator RESTful API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-RJSONIO >= 1.3.0
BuildRequires:    R-CRAN-progress >= 1.2.0
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-RJSONIO >= 1.3.0
Requires:         R-CRAN-progress >= 1.2.0

%description
CEU (CEU San Pablo University) Mass Mediator is an on-line tool for aiding
researchers in performing metabolite annotation. 'cmmr' (CEU Mass Mediator
RESTful API) allows for programmatic access in R: batch search, batch
advanced search, MS/MS (tandem mass spectrometry) search, etc. For more
information about the API Endpoint please go to
<https://github.com/lzyacht/cmmr>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

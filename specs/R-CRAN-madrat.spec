%global packname  madrat
%global packver   1.64.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.64.5
Release:          1%{?dist}
Summary:          May All Data be Reproducible and Transparent (MADRaT) *

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magclass >= 5.7.0
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-magclass >= 5.7.0
Requires:         R-CRAN-spam 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-digest 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-assertthat 

%description
Provides a framework which should improve reproducibility and transparency
in data processing. It provides functionality such as automatic meta data
creation and management, rudimentary quality management, data caching,
work-flow management and data aggregation. * The title is a wish not a
promise. By no means we expect this package to deliver everything what is
needed to achieve full reproducibility and transparency, but we believe
that it supports efforts in this direction.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

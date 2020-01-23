%global packname  climdex.pcic
%global packver   1.1-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.11
Release:          1%{?dist}
Summary:          PCIC Implementation of Climdex Routines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildRequires:    R-CRAN-PCICt >= 0.5.4
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-methods 
Requires:         R-CRAN-PCICt >= 0.5.4
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-methods 

%description
PCIC's implementation of Climdex routines for computation of extreme
climate indices. Further details on the extreme climate indices can be
found at <http://etccdi.pacificclimate.org/list_27_indices.shtml> and in
the package manual.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

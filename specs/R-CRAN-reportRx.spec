%global packname  reportRx
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Tools for automatically generating reproducible clinical report

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-aod 
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-reshape 
Requires:         R-survival 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-aod 
Requires:         R-CRAN-cmprsk 
Requires:         R-CRAN-geoR 
Requires:         R-CRAN-stringr 

%description
reportRx is a set of tools that integrates with LaTeX and knitr to
automatically generate generate reproducible clinical reports. Fuctions to
automatically produce demoraphic tables, outcome summaries, univariate and
multivariate analysis results and more are included.

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
%{rlibdir}/%{packname}/INDEX

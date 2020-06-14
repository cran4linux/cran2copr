%global packname  poliscidata
%global packver   2.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.3
Release:          2%{?dist}
Summary:          Datasets and Functions Featured in Pollock and Edwards, An RCompanion to Essentials of Political Analysis, Second Edition

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-descr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-ENmisc 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-abind 
Requires:         R-methods 
Requires:         R-CRAN-descr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-ENmisc 
Requires:         R-CRAN-car 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-abind 

%description
Bundles the datasets and functions used in the textbook by Philip Pollock
and Barry Edwards, An R Companion to Essentials of Political Analysis,
Second Edition.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

%global packname  psychotree
%global packver   0.15-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15.3
Release:          3%{?dist}%{?buildtag}
Summary:          Recursive Partitioning Based on Psychometric Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit >= 0.8.4
BuildRequires:    R-CRAN-psychotools >= 0.4.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Formula 
Requires:         R-CRAN-partykit >= 0.8.4
Requires:         R-CRAN-psychotools >= 0.4.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-CRAN-Formula 

%description
Recursive partitioning based on psychometric models, employing the general
MOB algorithm (from package partykit) to obtain Bradley-Terry trees, Rasch
trees, rating scale and partial credit trees, and MPT trees.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

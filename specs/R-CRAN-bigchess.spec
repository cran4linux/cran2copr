%global packname  bigchess
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          2%{?dist}
Summary:          Read, Manipulate, Explore Chess PGN Files and R API to UCI ChessEngines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-CRAN-ffbase 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-processx 
Requires:         R-CRAN-ff 
Requires:         R-CRAN-ffbase 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-processx 

%description
Provides functions for reading *.PGN files with more than one game,
including large files without copying it into RAM (using 'ff' package or
'RSQLite' package). Handle chess data and chess aggregated data, count
figure moves statistics, create player profile, plot winning chances,
browse openings. Set of functions of R API to communicate with
UCI-protocol based chess engines.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

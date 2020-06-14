%global packname  aaSEA
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Amino Acid Substitution Effect Analyser

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.7.1
BuildRequires:    R-CRAN-Hmisc >= 4.1.1
BuildRequires:    R-CRAN-seqinr >= 3.4.5
BuildRequires:    R-CRAN-Bios2cor >= 2.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.0.5
BuildRequires:    R-CRAN-shinydashboard >= 0.7.0
BuildRequires:    R-CRAN-DT >= 0.4
BuildRequires:    R-CRAN-networkD3 >= 0.4
Requires:         R-CRAN-plotly >= 4.7.1
Requires:         R-CRAN-Hmisc >= 4.1.1
Requires:         R-CRAN-seqinr >= 3.4.5
Requires:         R-CRAN-Bios2cor >= 2.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shiny >= 1.0.5
Requires:         R-CRAN-shinydashboard >= 0.7.0
Requires:         R-CRAN-DT >= 0.4
Requires:         R-CRAN-networkD3 >= 0.4

%description
Given a protein multiple sequence alignment, it is daunting task to assess
the effects of substitutions along sequence length. 'aaSEA' package is
intended to help researchers to rapidly analyse property changes caused by
single, multiple and correlated amino acid substitutions in proteins.
Methods for identification of co-evolving positions from multiple sequence
alignment are as described in : Pelé et al., (2017)
<doi:10.4172/2379-1764.1000250>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX

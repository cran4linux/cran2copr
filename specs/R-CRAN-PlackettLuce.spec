%global packname  PlackettLuce
%global packver   0.2-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9
Release:          2%{?dist}
Summary:          Plackett-Luce Models for Rankings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-psychotools 
BuildRequires:    R-CRAN-psychotree 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-qvcalc 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-psychotools 
Requires:         R-CRAN-psychotree 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-qvcalc 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 

%description
Functions to prepare rankings data and fit the Plackett-Luce model jointly
attributed to Plackett (1975) <doi:10.2307/2346567> and Luce (1959,
ISBN:0486441369). The standard Plackett-Luce model is generalized to
accommodate ties of any order in the ranking. Partial rankings, in which
only a subset of items are ranked in each ranking, are also accommodated
in the implementation. Disconnected/weakly connected networks implied by
the rankings may be handled by adding pseudo-rankings with a hypothetical
item. Optionally, a multivariate normal prior may be set on the log-worth
parameters and ranker reliabilities may be incorporated as proposed by
Raman and Joachims (2014) <doi:10.1145/2623330.2623654>. Maximum a
posteriori estimation is used when priors are set. Methods are provided to
estimate standard errors or quasi-standard errors for inference as well as
to fit Plackett-Luce trees. See the package website or vignette for
further details.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/PlackettLuce0
%doc %{rlibdir}/%{packname}/Reference_Implementations
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX

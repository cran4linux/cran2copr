%global packname  datafsm
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}
Summary:          Estimating Finite State Machine Models from Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-Rcpp 

%description
Automatic generation of finite state machine models of dynamic
decision-making that both have strong predictive power and are
interpretable in human terms. We use an efficient model representation and
a genetic algorithm-based estimation process to generate simple
deterministic approximations that explain most of the structure of complex
stochastic processes. We have applied the software to empirical data, and
demonstrated it's ability to recover known data-generating processes by
simulating data with agent-based models and correctly deriving the
underlying decision models for multiple agent models and degrees of
stochasticity.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

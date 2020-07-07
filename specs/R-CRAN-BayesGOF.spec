%global packname  BayesGOF
%global packver   5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.2
Release:          3%{?dist}
Summary:          Bayesian Modeling via Frequentist Goodness-of-Fit

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-Bolstad2 
BuildRequires:    R-CRAN-nleqslv 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-Bolstad2 
Requires:         R-CRAN-nleqslv 

%description
A Bayesian data modeling scheme that performs four interconnected tasks:
(i) characterizes the uncertainty of the elicited parametric prior; (ii)
provides exploratory diagnostic for checking prior-data conflict; (iii)
computes the final statistical prior density estimate; and (iv) executes
macro- and micro-inference. Primary reference is Mukhopadhyay, S. and
Fletcher, D. 2018 paper "Generalized Empirical Bayes via Frequentist
Goodness of Fit" (<https://www.nature.com/articles/s41598-018-28130-5 >).

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
%{rlibdir}/%{packname}/INDEX

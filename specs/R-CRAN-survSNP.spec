%global packname  survSNP
%global packver   0.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.24
Release:          3%{?dist}%{?buildtag}
Summary:          Power Calculations for SNP Studies with Censored Outcomes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel >= 1.14
Requires:         gsl
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-survival >= 2.36.9
BuildRequires:    R-CRAN-xtable >= 1.7.0
BuildRequires:    R-CRAN-foreach >= 1.3.2
BuildRequires:    R-CRAN-Rcpp >= 0.9.10
BuildRequires:    R-lattice >= 0.20.0
Requires:         R-survival >= 2.36.9
Requires:         R-CRAN-xtable >= 1.7.0
Requires:         R-CRAN-foreach >= 1.3.2
Requires:         R-CRAN-Rcpp >= 0.9.10
Requires:         R-lattice >= 0.20.0

%description
Conduct asymptotic and empirical power and sample size calculations for
Single-Nucleotide Polymorphism (SNP) association studies with right
censored time to event outcomes.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

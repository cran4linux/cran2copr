%global packname  FuzzyStatProb
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Fuzzy Stationary Probabilities from a Sequence of Observationsof an Unknown Markov Chain

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MultinomialCI 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-FuzzyNumbers 
BuildRequires:    R-CRAN-DEoptim 
Requires:         R-CRAN-MultinomialCI 
Requires:         R-parallel 
Requires:         R-CRAN-FuzzyNumbers 
Requires:         R-CRAN-DEoptim 

%description
An implementation of a method for computing fuzzy numbers representing
stationary probabilities of an unknown Markov chain, from which a sequence
of observations along time has been obtained. The algorithm is based on
the proposal presented by James Buckley in his book on Fuzzy probabilities
(Springer, 2005), chapter 6. Package 'FuzzyNumbers' is used to represent
the output probabilities.

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

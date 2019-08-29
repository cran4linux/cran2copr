%global packname  kSamples
%global packver   1.2-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.9
Release:          1%{?dist}
Summary:          K-Sample Rank Tests and their Combinations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-SuppDists 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 

%description
Compares k samples using the Anderson-Darling test, Kruskal-Wallis type
tests with different rank score criteria, Steel's multiple comparison
test, and the Jonckheere-Terpstra (JT) test. It computes asymptotic,
simulated or (limited) exact P-values, all valid under randomization, with
or without ties, or conditionally under random sampling from populations,
given the observed tie pattern.  Except for Steel's test and the JT test
it also combines these tests across several blocks of samples.  Also
analyzed are 2 x t contingency tables and their blocked combinations using
the Kruskal-Wallis criterion.  Steel's test is inverted to provide
simultaneous confidence bounds for shift parameters.  A plotting function
compares tail probabilities obtained under asymptotic approximation with
those obtained via simulation or exact calculations.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

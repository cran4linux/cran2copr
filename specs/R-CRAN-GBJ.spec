%global packname  GBJ
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Generalized Berk-Jones Test for Set-Based Inference in GeneticAssociation Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-SKAT 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-SKAT 
Requires:         R-stats 

%description
Offers the Generalized Berk-Jones (GBJ) test for set-based inference in
genetic association studies. The GBJ is designed as an alternative to
tests such as Berk-Jones (BJ), Higher Criticism (HC), Generalized Higher
Criticism (GHC), Minimum p-value (minP), and Sequence Kernel Association
Test (SKAT). All of these other methods (except for SKAT) are also
implemented in this package, and we additionally provide an omnibus test
(OMNI) which integrates information from each of the tests. The GBJ has
been shown to outperform other tests in genetic association studies when
signals are correlated and moderately sparse. Please see the vignette for
a quickstart guide or Sun and Lin (2017) <arXiv:1710.02469> for more
details.

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
%{rlibdir}/%{packname}/libs

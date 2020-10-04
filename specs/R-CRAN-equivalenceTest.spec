%global packname  equivalenceTest
%global packver   0.0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Equivalence Test for the Means of Two Normal Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-graphics 

%description
Two methods for performing equivalence test for the means of two (test and
reference) normal distributions are implemented. The null hypothesis of
the equivalence test is that the absolute difference between the two means
are greater than or equal to the equivalence margin and the alternative is
that the absolute difference is less than the margin. Given that the
margin is often difficult to obtain a priori, it is assumed to be a
constant multiple of the standard deviation of the reference distribution.
The first method assumes a fixed margin which is a constant multiple of
the estimated standard deviation of the reference data and whose
variability is ignored. The second method takes into account the margin
variability. In addition, some tools to summarize and illustrate the data
and test results are included to facilitate the evaluation of the data and
interpretation of the results.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX

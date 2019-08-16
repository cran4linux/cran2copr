%global packname  tmvtnorm
%global packver   1.4-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.10
Release:          1%{?dist}
Summary:          Truncated Multivariate Normal and Student t Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 1.9.0
Requires:         R-core >= 1.9.0
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-gmm 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-stats4 
Requires:         R-CRAN-gmm 
Requires:         R-stats 
Requires:         R-methods 

%description
Random number generation for the truncated multivariate normal and Student
t distribution. Computes probabilities, quantiles and densities, including
one-dimensional and bivariate marginal densities. Computes first and
second moments (i.e. mean and covariance matrix) for the double-truncated
multinormal case.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

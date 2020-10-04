%global packname  disclapmix
%global packver   1.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.3
Release:          3%{?dist}%{?buildtag}
Summary:          Discrete Laplace Mixture Inference using the EM Algorithm

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-disclap >= 1.4
BuildRequires:    R-cluster >= 1.14.4
BuildRequires:    R-CRAN-Rcpp >= 0.11
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-disclap >= 1.4
Requires:         R-cluster >= 1.14.4
Requires:         R-CRAN-Rcpp >= 0.11
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-utils 

%description
Make inference in a mixture of discrete Laplace distributions using the EM
algorithm. This can e.g. be used for modelling the distribution of Y
chromosomal haplotypes as described in [1, 2] (refer to the URL section).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

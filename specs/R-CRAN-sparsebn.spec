%global packname  sparsebn
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          Learning Sparse Bayesian Networks from High-Dimensional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-sparsebnUtils >= 0.0.5
BuildRequires:    R-CRAN-discretecdAlgorithm >= 0.0.5
BuildRequires:    R-CRAN-ccdrAlgorithm >= 0.0.4
Requires:         R-CRAN-sparsebnUtils >= 0.0.5
Requires:         R-CRAN-discretecdAlgorithm >= 0.0.5
Requires:         R-CRAN-ccdrAlgorithm >= 0.0.4

%description
Fast methods for learning sparse Bayesian networks from high-dimensional
data using sparse regularization, as described in Aragam, Gu, and Zhou
(2017) <arXiv:1703.04025>. Designed to handle mixed experimental and
observational data with thousands of variables with either continuous or
discrete observations.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

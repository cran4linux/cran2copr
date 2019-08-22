%global packname  topicmodels
%global packver   0.2-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}
Summary:          Topic Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel >= 1.8
Requires:         gsl
BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-tm >= 0.6
BuildRequires:    R-stats4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-modeltools 
BuildRequires:    R-CRAN-slam 
Requires:         R-CRAN-tm >= 0.6
Requires:         R-stats4 
Requires:         R-methods 
Requires:         R-CRAN-modeltools 
Requires:         R-CRAN-slam 

%description
Provides an interface to the C code for Latent Dirichlet Allocation (LDA)
models and Correlated Topics Models (CTM) by David M. Blei and co-authors
and the C++ code for fitting LDA models using Gibbs sampling by Xuan-Hieu
Phan and co-authors.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

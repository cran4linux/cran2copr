%global packname  abc
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}
Summary:          Tools for Approximate Bayesian Computation (ABC)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-abc.data 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-locfit 
Requires:         R-CRAN-abc.data 
Requires:         R-nnet 
Requires:         R-CRAN-quantreg 
Requires:         R-MASS 
Requires:         R-CRAN-locfit 

%description
Implements several ABC algorithms for performing parameter estimation,
model selection, and goodness-of-fit. Cross-validation tools are also
available for measuring the accuracy of ABC estimates, and to calculate
the misclassification probabilities of different models.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

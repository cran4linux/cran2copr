%global packname  ic.infer
%global packver   1.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          2%{?dist}
Summary:          Inequality Constrained Inference in Linear Normal Situations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-kappalab 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-mvtnorm 
Requires:         R-boot 
Requires:         R-CRAN-kappalab 

%description
Implements inequality constrained inference. This includes parameter
estimation in normal (linear) models under linear equality and inequality
constraints, as well as normal likelihood ratio tests involving
inequality-constrained hypotheses. For inequality-constrained linear
models, averaging over R-squared for different orderings of regressors is
also included.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX

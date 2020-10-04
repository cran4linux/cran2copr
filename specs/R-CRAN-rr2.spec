%global packname  rr2
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          R2s for Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-phylolm 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-nlme 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-phylolm 
Requires:         R-CRAN-ape 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-nlme 

%description
Three methods to calculate R2 for models with correlated errors, including
Phylogenetic GLS, Phylogenetic Logistic Regression, Linear Mixed Models
(LMMs), and Generalized Linear Mixed Models (GLMMs). See details in Ives
2018 <doi:10.1093/sysbio/syy060>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX

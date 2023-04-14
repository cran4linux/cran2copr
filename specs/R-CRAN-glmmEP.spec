%global __brp_check_rpaths %{nil}
%global packname  glmmEP
%global packver   1.0-3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Generalized Linear Mixed Model Analysis via ExpectationPropagation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-matrixcalc 

%description
Approximate frequentist inference for generalized linear mixed model
analysis with expectation propagation used to circumvent the need for
multivariate integration. In this version, the random effects can be any
reasonable dimension. However, only probit mixed models with one level of
nesting are supported. The methodology is described in Hall, Johnstone,
Ormerod, Wand and Yu (2018) <arXiv:1805.08423v1>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

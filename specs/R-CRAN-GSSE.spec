%global __brp_check_rpaths %{nil}
%global packname  GSSE
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Genotype-Specific Survival Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.12
BuildRequires:    R-CRAN-Iso >= 0.0.17
BuildRequires:    R-splines 
BuildRequires:    R-stats 
Requires:         R-CRAN-zoo >= 1.7.12
Requires:         R-CRAN-Iso >= 0.0.17
Requires:         R-splines 
Requires:         R-stats 

%description
We propose a fully efficient sieve maximum likelihood method to estimate
genotype-specific distribution of time-to-event outcomes under a
nonparametric model. We can handle missing genotypes in pedigrees.  We
estimate the time-dependent hazard ratio between two genetic mutation
groups using B-splines, while applying nonparametric maximum likelihood
estimation to the reference baseline hazard function.  The estimators are
calculated via an expectation-maximization algorithm.

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

%global __brp_check_rpaths %{nil}
%global packname  hIRT
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Hierarchical Item Response Theory Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 5.1.1
BuildRequires:    R-Matrix >= 1.2.10
BuildRequires:    R-CRAN-ltm >= 1.1.1
BuildRequires:    R-CRAN-pryr >= 0.1.2
BuildRequires:    R-stats 
Requires:         R-CRAN-rms >= 5.1.1
Requires:         R-Matrix >= 1.2.10
Requires:         R-CRAN-ltm >= 1.1.1
Requires:         R-CRAN-pryr >= 0.1.2
Requires:         R-stats 

%description
Implementation of a class of hierarchical item response theory (IRT)
models where both the mean and the variance of latent preferences (ability
parameters) may depend on observed covariates. The current implementation
includes both the two-parameter latent trait model for binary data and the
graded response model for ordinal data. Both are fitted via the
Expectation-Maximization (EM) algorithm. Asymptotic standard errors are
derived from the observed information matrix.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

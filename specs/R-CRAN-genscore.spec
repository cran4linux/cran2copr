%global __brp_check_rpaths %{nil}
%global packname  genscore
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Generalized Score Matching Estimators

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-stringr 

%description
Implementation of the Generalized Score Matching estimator in Yu et al.
(2019) <http://jmlr.org/papers/v20/18-278.html> for non-negative graphical
models (truncated Gaussian, exponential square-root, gamma, a-b models)
and univariate truncated Gaussian distributions. Also includes the
original estimator for untruncated Gaussian graphical models from Lin et
al. (2016) <doi:10.1214/16-EJS1126>, with the addition of a diagonal
multiplier.

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

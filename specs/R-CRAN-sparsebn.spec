%global __brp_check_rpaths %{nil}
%global packname  sparsebn
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

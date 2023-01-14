%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  poismf
%global packver   0.4.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Factorization of Sparse Counts Matrices Through Poisson Likelihood

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix >= 1.3
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix >= 1.3
Requires:         R-methods 

%description
Creates a non-negative low-rank approximate factorization of a sparse
counts matrix by maximizing Poisson likelihood with L1/L2 regularization
(e.g. for implicit-feedback recommender systems or bag-of-words-based
topic modeling) (Cortes, (2018) <arXiv:1811.01908>), which usually leads
to very sparse user and item factors (over 90%% zero-valued). Similar to
hierarchical Poisson factorization (HPF), but follows an
optimization-based approach with regularization instead of a hierarchical
prior, and is fit through gradient-based methods instead of variational
inference.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

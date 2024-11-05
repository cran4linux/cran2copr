%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rnnmf
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized Non-Negative Matrix Factorization

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-Matrix 

%description
A proof of concept implementation of regularized non-negative matrix
factorization optimization. A non-negative matrix factorization factors
non-negative matrix Y approximately as L R, for non-negative matrices L
and R of reduced rank. This package supports such factorizations with
weighted objective and regularization penalties. Allowable regularization
penalties include L1 and L2 penalties on L and R, as well as
non-orthogonality penalties. This package provides multiplicative update
algorithms, which are a modification of the algorithm of Lee and Seung
(2001)
<http://papers.nips.cc/paper/1861-algorithms-for-non-negative-matrix-factorization.pdf>,
as well as an additive update derived from that multiplicative update.
See also Pav (2004) <doi:10.48550/arXiv.2410.22698>.

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

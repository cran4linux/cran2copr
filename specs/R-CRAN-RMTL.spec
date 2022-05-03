%global __brp_check_rpaths %{nil}
%global packname  RMTL
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized Multi-Task Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.50
BuildRequires:    R-CRAN-psych >= 1.8.4
BuildRequires:    R-CRAN-corpcor >= 1.6.9
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-doParallel >= 1.0.14
Requires:         R-CRAN-MASS >= 7.3.50
Requires:         R-CRAN-psych >= 1.8.4
Requires:         R-CRAN-corpcor >= 1.6.9
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-doParallel >= 1.0.14

%description
Efficient solvers for 10 regularized multi-task learning algorithms
applicable for regression, classification, joint feature selection, task
clustering, low-rank learning, sparse learning and network incorporation.
Based on the accelerated gradient descent method, the algorithms feature a
state-of-art computational complexity O(1/k^2). Sparse model structure is
induced by the solving the proximal operator. The detail of the package is
described in the paper of Han Cao and Emanuel Schwarz (2018)
<doi:10.1093/bioinformatics/bty831>.

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

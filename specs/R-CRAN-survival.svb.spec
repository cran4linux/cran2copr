%global __brp_check_rpaths %{nil}
%global packname  survival.svb
%global packver   0.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fit High-Dimensional Proportional Hazards Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-survival 

%description
Implementation of methodology designed to perform: (i) variable selection,
(ii) effect estimation, and (iii) uncertainty quantification, for
high-dimensional survival data. Our method uses a spike-and-slab prior
with Laplace slab and Dirac spike and approximates the corresponding
posterior using variational inference, a popular method in machine
learning for scalable conditional inference. Although approximate, the
variational posterior provides excellent point estimates and good control
of the false discovery rate. For more information see Komodromos et al.
(2021) <arXiv:2112.10270>.

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

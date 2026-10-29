%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evgmrf
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Markov Random Field Models for Extreme Values

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix >= 1.6.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-sparseinv 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix >= 1.6.0
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-methods 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-sparseinv 

%description
Fitting extreme value distributions with parameters that vary according to
Gaussian Markov random fields (GMRFs). For details of distributions see
Coles, S.G. (2001) <doi:10.1007/978-1-4471-3675-0>, GMRFs see Rue, H., &
Held, L. (2005) <doi:10.1201/9780203492024>, and the fitting approach see
Wood, S.N., Pya, N. & Safken, B. (2016)
<doi:10.1080/01621459.2016.1180986>.

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

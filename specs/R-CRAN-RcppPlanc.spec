%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcppPlanc
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Low-Rank Approximation with Nonnegativity Constraints

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-hdf5r.Extra 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-hdf5r.Extra 

%description
'Rcpp' bindings for 'PLANC', a highly parallel and extensible NMF/NTF
(Non-negative Matrix/Tensor Factorization) library. Wraps algorithms
described in Kannan et. al (2018) <doi:10.1109/TKDE.2017.2767592> and
Eswar et. al (2021) <doi:10.1145/3432185>. Implements algorithms described
in Welch et al. (2019) <doi:10.1016/j.cell.2019.05.006>, Gao et al. (2021)
<doi:10.1038/s41587-021-00867-x>, and Kriebel & Welch (2022)
<doi:10.1038/s41467-022-28431-4>.

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

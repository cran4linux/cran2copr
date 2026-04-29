%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  apca
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Principal Component Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Provides nine computational algorithms for dimensionality reduction via
Principal Component Analysis (PCA), built using an object-oriented (S3)
architecture. The package includes classical and modern methods: Singular
Value Decomposition (SVD) based on Eckart and Young (1936)
<doi:10.1007/BF02288367>, Power Iteration based on Hotelling (1933)
<doi:10.1037/h0071325>, QR Algorithm based on Francis (1961)
<doi:10.1093/comjnl/4.3.265>, Jacobi Algorithm based on Jacobi (1846)
<doi:10.1515/crll.1846.30.51>, Arnoldi Iteration based on Arnoldi (1951)
<doi:10.1090/qam/42792>, 'NIPALS' based on Wold (1975)
<doi:10.1017/S0021900200047604>, Alternating Least Squares (ALS) based on
Kolda and Bader (2009) <doi:10.1137/07070111X>, Probabilistic PCA (PPCA)
with EM Algorithm based on Tipping and Bishop (1999)
<doi:10.1111/1467-9868.00196>, and Generalized Hebbian Algorithm (GHA)
based on Sanger (1989) <doi:10.1016/0893-6080(89)90044-0>.

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

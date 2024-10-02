%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UniIsoRegression
%global packver   0.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unimodal and Isotonic L1, L2 and Linf Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-Rcpp >= 0.12.11

%description
Perform L1 or L2 isotonic and unimodal regression on 1D weighted or
unweighted input vector and isotonic regression on 2D weighted or
unweighted input vector. It also performs L infinity isotonic and unimodal
regression on 1D unweighted input vector. Reference: Quentin F. Stout
(2008) <doi:10.1016/j.csda.2008.08.005>. Spouge, J., Wan, H. & Wilbur,
W.(2003) <doi:10.1023/A:1023901806339>. Q.F. Stout (2013)
<doi:10.1007/s00453-012-9628-4>.

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

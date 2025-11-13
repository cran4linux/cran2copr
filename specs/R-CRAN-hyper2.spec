%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hyper2
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          1%{?dist}%{?buildtag}
Summary:          The Hyperdirichlet Distribution, Mark 2

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-disordR >= 0.0.9
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-calibrator 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-disordR >= 0.0.9
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-calibrator 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-cubature 
Requires:         R-methods 

%description
A suite of routines for the hyperdirichlet distribution and reified
Bradley-Terry; supersedes the 'hyperdirichlet' package; uses 'disordR'
discipline <doi:10.48550/ARXIV.2210.03856>.  To cite in publications
please use Hankin 2017 <doi:10.32614/rj-2017-061>, and for Generalized
Plackett-Luce likelihoods use Hankin 2024 <doi:10.18637/jss.v109.i08>.

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

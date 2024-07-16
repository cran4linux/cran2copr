%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EloRating
%global packver   0.46.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.46.18
Release:          1%{?dist}%{?buildtag}
Summary:          Animal Dominance Hierarchies by Elo Rating

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-network 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 

%description
Provides functions to quantify animal dominance hierarchies. The major
focus is on Elo rating and its ability to deal with temporal dynamics in
dominance interaction sequences. For static data, David's score and de
Vries' I&SI are also implemented. In addition, the package provides
functions to assess transitivity, linearity and stability of dominance
networks. See Neumann et al (2011) <doi:10.1016/j.anbehav.2011.07.016> for
an introduction.

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

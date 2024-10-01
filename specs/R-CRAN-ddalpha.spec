%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ddalpha
%global packver   1.3.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.16
Release:          1%{?dist}%{?buildtag}
Summary:          Depth-Based Classification and Calculation of Data Depth

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-class 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-geometry 

%description
Contains procedures for depth-based supervised learning, which are
entirely non-parametric, in particular the DDalpha-procedure (Lange,
Mosler and Mozharovskyi, 2014 <doi:10.1007/s00362-012-0488-4>). The
training data sample is transformed by a statistical depth function to a
compact low-dimensional space, where the final classification is done. It
also offers an extension to functional data and routines for calculating
certain notions of statistical depth functions. 50 multivariate and 5
functional classification problems are included. (Pokotylo, Mozharovskyi
and Dyckerhoff, 2019 <doi:10.18637/jss.v091.i05>).

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

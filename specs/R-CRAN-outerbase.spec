%global __brp_check_rpaths %{nil}
%global packname  outerbase
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Outer Product Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-stats 

%description
High-dimensional regression using outer product models.  Research on the
methods is currently under investigation and published resources will be
posted as they are available.  As the method is new, the website is the
best resource for understanding the principals. Some of the core ideas are
based on Plumlee and coauthors' work on analysis of grid-structured
experiments described in Plumlee (2014) <doi:10.1080/01621459.2014.900250>
and Plumlee, Erickson, Ankenman, Lawrence (2021)
<doi:10.1093/biomet/asaa084>.  Some additional textbooks for additional
information on Gaussian processes are Rasmussen and Williams (2005)
<doi:10.7551/mitpress/3206.001.0001> and Gramacy (2022)
<doi:10.1201/9780367815493>.

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

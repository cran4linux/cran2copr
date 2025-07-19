%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rim
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'Maxima', Enabling Symbolic Computation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       maxima
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-GlobalOptions 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-GlobalOptions 

%description
An interface to the powerful and fairly complete computer algebra system
'Maxima'. It can be used to start and control 'Maxima' from within R by
entering 'Maxima' commands. Results from 'Maxima' can be parsed and
evaluated in R. It facilitates outputting results from 'Maxima' in 'LaTeX'
and 'MathML'. 2D and 3D plots can be displayed directly. This package also
registers a 'knitr'-engine enabling 'Maxima' code chunks to be written in
'RMarkdown' documents.

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

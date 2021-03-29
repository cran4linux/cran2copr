%global packname  EDOIF
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Distribution Ordering Inference Framework (EDOIF)

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-distr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-simpleboot 
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-boot 
Requires:         R-CRAN-distr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-simpleboot 

%description
A non-parametric framework based on estimation statistics principle. Its
main purpose is to infer orders of empirical distributions from different
categories based on a probability of finding a value in one distribution
that is greater than an expectation of another distribution. Given a set
of ordered-pair of real-category values the framework is capable of 1)
inferring orders of domination of categories and representing orders in
the form of a graph; 2) estimating magnitude of difference between a pair
of categories in forms of mean-difference confidence intervals; and 3)
visualizing domination orders and magnitudes of difference of categories.
The publication of this package is at Chainarong Amornbunchornvej,
Navaporn Surasvadi, Anon Plangprasopchok, and Suttipong Thajchayapong
(2020) <doi:10.1016/j.heliyon.2020.e05435>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

%global packname  MRReg
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          MDL Multiresolution Linear Regression Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-igraph 

%description
We provide the framework to analyze multiresolution partitions (e.g.
country, provinces, subdistrict) where each individual data point belongs
to only one partition in each layer (e.g. i belongs to subdistrict A,
province P, and country Q).  We assume that a partition in a higher layer
subsumes lower-layer partitions (e.g. a nation is at the 1st layer
subsumes all provinces at the 2nd layer). Given N individuals that have a
pair of real values (x,y) that generated from independent variable X and
dependent variable Y. Each individual i belongs to one partition per
layer. Our goal is to find which partitions at which highest level that
all individuals in the these partitions share the same linear model Y=f(X)
where f is a linear function. The framework deploys the Minimum
Description Length principle (MDL) to infer solutions. The publication of
this package is at Chainarong Amornbunchornvej, Navaporn Surasvadi, Anon
Plangprasopchok, and Suttipong Thajchayapong (2021) <doi:10.1145/3424670>.

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

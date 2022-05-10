%global __brp_check_rpaths %{nil}
%global packname  BDgraph
%global packver   2.67
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.67
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Structure Learning in Graphical Models using Birth-Death MCMC

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-igraph 

%description
Statistical tools for Bayesian structure learning in undirected graphical
models for continuous, discrete, and mixed data. The package is
implemented the recent improvements in the Bayesian graphical models'
literature, including Mohammadi and Wit (2015) <doi:10.1214/14-BA889>,
Mohammadi et al. (2021) <doi:10.1080/01621459.2021.1996377>, and Mohammadi
and Wit (2019) <doi:10.18637/jss.v089.i03>.

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

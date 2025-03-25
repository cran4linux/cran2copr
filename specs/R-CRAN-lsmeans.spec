%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lsmeans
%global packver   2.30-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.30.2
Release:          1%{?dist}%{?buildtag}
Summary:          Least-Squares Means

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-emmeans >= 1.3
BuildRequires:    R-methods 
Requires:         R-CRAN-emmeans >= 1.3
Requires:         R-methods 

%description
Obtain least-squares means for linear, generalized linear, and mixed
models. Compute contrasts or linear functions of least-squares means, and
comparisons of slopes. Plots and compact letter displays. Least-squares
means were proposed in Harvey, W (1960) "Least-squares analysis of data
with unequal subclass numbers", Tech Report ARS-20-8, USDA National
Agricultural Library, and discussed further in Searle, Speed, and Milliken
(1980) "Population marginal means in the linear model: An alternative to
least squares means", The American Statistician 34(4), 216-221
<doi:10.1080/00031305.1980.10483031>. NOTE: lsmeans now relies primarily
on code in the 'emmeans' package. 'lsmeans' will be archived in the near
future.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ShiVa
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Detection of Evolutionary Shifts in Both Optimal Value and Variance

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phylolm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phylolm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-igraph 

%description
Implements statistical methods for detecting evolutionary shifts in both
the optimal trait value (mean) and evolutionary diffusion variance. The
method uses an L1-penalized optimization framework to identify branches
where shifts occur, and the shift magnitudes. It also supports the
inclusion of measurement error. For more details, see Zhang, Ho, and
Kenney (2023) <doi:10.48550/arXiv.2312.17480>.

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

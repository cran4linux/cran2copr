%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arf
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Adversarial Random Forests

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-matrixStats 

%description
Adversarial random forests (ARFs) recursively partition data into fully
factorized leaves, where features are jointly independent. The procedure
is iterative, with alternating rounds of generation and discrimination.
Data becomes increasingly realistic at each round, until original and
synthetic samples can no longer be reliably distinguished. This is useful
for several unsupervised learning tasks, such as density estimation and
data synthesis. Methods for both are implemented in this package. ARFs
naturally handle unstructured data with mixed continuous and categorical
covariates. They inherit many of the benefits of random forests, including
speed, flexibility, and solid performance with default parameters. For
details, see Watson et al. (2022) <arXiv:2205.09435>.

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

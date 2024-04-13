%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  basksim
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Calculation of Basket Trial Operating Characteristics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-CRAN-bhmbasket 
BuildRequires:    R-CRAN-bmabasket 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-arrangements 
Requires:         R-CRAN-bhmbasket 
Requires:         R-CRAN-bmabasket 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-progressr 

%description
Provides a unified syntax for the simulation-based comparison of different
single-stage basket trial designs with a binary endpoint and equal sample
sizes in all baskets. Methods include the designs by Baumann et al. (2024)
<doi:10.48550/arXiv.2309.06988>, Fujikawa et al. (2020)
<doi:10.1002/bimj.201800404>, Berry et al. (2020)
<doi:10.1177/1740774513497539>, Neuenschwander et al. (2016)
<doi:10.1002/pst.1730> and Psioda et al. (2021)
<doi:10.1093/biostatistics/kxz014>. For the latter three designs, the
functions are mostly wrappers for functions provided by the packages
'bhmbasket' and 'bmabasket'.

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

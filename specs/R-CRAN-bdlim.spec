%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bdlim
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Distributed Lag Interaction Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-BayesLogit 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-BayesLogit 

%description
Estimation and interpretation of Bayesian distributed lag interaction
models (BDLIMs). A BDLIM regresses a scalar outcome on repeated measures
of exposure and allows for modification by a categorical variable under
four specific patterns of modification. The main function is bdlim().
There are also summary and plotting files. Details on methodology are
described in Wilson et al. (2017) <doi:10.1093/biostatistics/kxx002>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drcarlate
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Improving Estimation Efficiency in CAR with Imperfect Compliance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-splus2R 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-splus2R 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-CRAN-purrr 

%description
We provide a list of functions for replicating the results of the Monte
Carlo simulations and empirical application of Jiang et al. (2022). In
particular, we provide corresponding functions for generating the three
types of random data described in this paper, as well as all the
estimation strategies. Detailed information about the data generation
process and estimation strategy can be found in Jiang et al. (2022)
<doi:10.48550/arXiv.2201.13004>.

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

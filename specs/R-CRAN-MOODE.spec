%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MOODE
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Objective Optimal Design of Experiments

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-far 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-far 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 

%description
Provides functionality to generate compound optimal designs for targeting
the multiple experimental objectives directly, ensuring that the full set
of research questions is answered as economically as possible. Designs can
be found using point or coordinate exchange algorithms combining
estimation, inference and lack-of-fit criteria that account for model
inadequacy. Details and examples are given by Koutra et al. (2024)
<doi:10.48550/arXiv.2412.17158>.

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

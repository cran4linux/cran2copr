%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GEC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Exponentiated Composite Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mistr 
Requires:         R-stats 
Requires:         R-CRAN-mistr 

%description
Contains the framework of the estimation, sampling, and hypotheses testing
for two special distributions (Exponentiated Exponential-Pareto and
Exponentiated Inverse Gamma-Pareto) within the family of Generalized
Exponentiated Composite distributions. The detailed explanation and the
applications of these two distributions were introduced in Bowen Liu,
Malwane M.A. Ananda (2022) <doi:10.1080/03610926.2022.2050399>, Bowen Liu,
Malwane M.A. Ananda (2022) <doi:10.3390/math10111895>, and Bowen Liu,
Malwane M.A. Ananda (2022) <doi:10.3390/app13010645>.

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

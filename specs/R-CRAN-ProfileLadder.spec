%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ProfileLadder
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functional-Based Chain Ladder for Claims Reserving

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon >= 1.5.0
BuildRequires:    R-CRAN-ChainLadder >= 0.2.12
BuildRequires:    R-CRAN-raw >= 0.1.8
Requires:         R-CRAN-crayon >= 1.5.0
Requires:         R-CRAN-ChainLadder >= 0.2.12
Requires:         R-CRAN-raw >= 0.1.8

%description
Functional claims reserving methods based on aggregated chain-ladder data,
also known as a run-off triangle, implemented in three nonparametric
algorithms (PARALLAX, REACT, and MACRAME) proposed in Maciak, Mizera, and
Pešta (2022) <doi:10.1017/asb.2022.4>. Additional methods including
permutation bootstrap for completed run-off triangles are also provided.

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

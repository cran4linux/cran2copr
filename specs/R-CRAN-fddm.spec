%global packname  fddm
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Implementation of the Diffusion Decision Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
Provides the probability density function (PDF) of the diffusion decision
model (DDM; e.g., Ratcliff & McKoon, 2008,
<doi:10.1162/neco.2008.12-06-420>) with across-trial variability in the
drift rate. Because the PDF of the DDM contains an infinite sum, it needs
to be approximated. 'fddm' implements all published approximations
(Navarro & Fuss, 2009, <doi:10.1016/j.jmp.2009.02.003>; Gondan, Blurton, &
Kesselmeier, 2014, <doi:10.1016/j.jmp.2014.05.002>) plus new
approximations. All approximations are implemented purely in 'C++'
providing faster speed than existing packages.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

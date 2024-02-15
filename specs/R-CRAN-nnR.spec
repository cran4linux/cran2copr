%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nnR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Neural Networks Made Algebraic

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch

%description
Do algebraic operations on neural networks. We seek here to implement in
R, operations on neural networks and their resulting approximations. Our
operations derive their descriptions mainly from Rafi S., Padgett, J.L.,
and Nakarmi, U. (2024), "Towards an Algebraic Framework For Approximating
Functions Using Neural Network Polynomials",
<doi:10.48550/arXiv.2402.01058>, Grohs P., Hornung, F., Jentzen, A. et al.
(2023), "Space-time error estimates for deep neural network approximations
for differential equations", <doi:10.1007/s10444-022-09970-2>, Jentzen A.,
Kuckuck B., von Wurstemberger, P. (2023), "Mathematical Introduction to
Deep Learning Methods, Implementations, and Theory"
<doi:10.48550/arXiv.2310.20360>. Our implementation is meant mainly as a
pedagogical tool, and proof of concept. Faster implementations with deeper
vectorizations may be made in future versions.

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

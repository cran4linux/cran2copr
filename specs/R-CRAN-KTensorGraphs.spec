%global packname  KTensorGraphs
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Co-Tucker3 Analysis of Two Sequences of Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides a function called COTUCKER3() (Co-Inertia Analysis + Tucker3
method) which performs a Co-Tucker3 analysis of two sequences of matrices,
as well as other functions called PCA() (Principal Component Analysis) and
BGA() (Between-Groups Analysis), which perform analysis of one matrix,
COIA() (Co-Inertia Analysis), which performs analysis of two matrices,
PTA() (Partial Triadic Analysis), STATIS(), STATISDUAL() and TUCKER3(),
which perform analysis of a sequence of matrices, and BGCOIA()
(Between-Groups Co-Inertia Analysis), STATICO() (STATIS method +
Co-Inertia Analysis), COSTATIS() (Co-Inertia Analysis + STATIS method),
which also perform analysis of two sequences of matrices.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

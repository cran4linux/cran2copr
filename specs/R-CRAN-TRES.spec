%global __brp_check_rpaths %{nil}
%global packname  TRES
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Tensor Regression with Envelope Structure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma >= 2.2.5
BuildRequires:    R-CRAN-rTensor >= 1.4
BuildRequires:    R-CRAN-ManifoldOptim >= 1.0.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-pracma >= 2.2.5
Requires:         R-CRAN-rTensor >= 1.4
Requires:         R-CRAN-ManifoldOptim >= 1.0.0
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-stats 

%description
Provides three estimators for tensor response regression (TRR) and tensor
predictor regression (TPR) models with tensor envelope structure. The
three types of estimation approaches are generic and can be applied to any
envelope estimation problems. The full Grassmannian (FG) optimization is
often associated with likelihood-based estimation but requires heavy
computation and good initialization; the one-directional optimization
approaches (1D and ECD algorithms) are faster, stable and does not require
carefully chosen initial values; the SIMPLS-type is motivated by the
partial least squares regression and is computationally the least
expensive. For details of TRR, see Li L, Zhang X (2017)
<doi:10.1080/01621459.2016.1193022>. For details of TPR, see Zhang X, Li L
(2017) <doi:10.1080/00401706.2016.1272495>. For details of 1D algorithm,
see Cook RD, Zhang X (2016) <doi:10.1080/10618600.2015.1029577>. For
details of ECD algorithm, see Cook RD, Zhang X (2018)
<doi:10.5705/ss.202016.0037>.

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

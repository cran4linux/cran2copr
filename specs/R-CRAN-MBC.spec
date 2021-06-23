%global __brp_check_rpaths %{nil}
%global packname  MBC
%global packver   0.10-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Bias Correction of Climate Model Outputs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-FNN 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-FNN 

%description
Calibrate and apply multivariate bias correction algorithms for climate
model simulations of multiple climate variables. Three methods described
by Cannon (2016) <doi:10.1175/JCLI-D-15-0679.1> and Cannon (2018)
<doi:10.1007/s00382-017-3580-6> are implemented — (i) MBC Pearson
correlation (MBCp), (ii) MBC rank correlation (MBCr), and (iii) MBC
N-dimensional PDF transform (MBCn) — as is the Rank Resampling for
Distributions and Dependences (R2D2) method.

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

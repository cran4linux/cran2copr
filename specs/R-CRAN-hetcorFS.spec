%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hetcorFS
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unsupervised Feature Selection using the Heterogeneous Correlation Matrix

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-polycor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-cluster 
Requires:         R-graphics 
Requires:         R-CRAN-psych 

%description
Unsupervised multivariate filter feature selection using the UFS-rHCM or
UFS-cHCM algorithms based on the heterogeneous correlation matrix (HCM).
The HCM consists of Pearson's correlations between numerical features,
polyserial correlations between numerical and ordinal features, and
polychoric correlations between ordinal features. Tortora C., Madhvani S.,
Punzo A. (2025). "Designing unsupervised mixed-type feature selection
techniques using the heterogeneous correlation matrix." International
Statistical Review <doi:10.1111/insr.70016>. This work was supported by
the National Science foundation NSF Grant N 2209974 (Tortora) and by the
Italian Ministry of University and Research (MUR) under the PRIN 2022
grant number 2022XRHT8R (CUP: E53D23005950006), as part of ‘The SMILE
Project: Statistical Modelling and Inference to Live the Environment’,
funded by the European Union – Next Generation EU (Punzo).

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

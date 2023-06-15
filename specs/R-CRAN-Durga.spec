%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Durga
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Effect Size Estimation and Visualisation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-vipor 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-methods 
Requires:         R-CRAN-vipor 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-methods 

%description
An easy-to-use yet powerful system for plotting grouped data effect sizes.
Various types of effect size can be estimated, then plotted together with
a representation of the original data. Select from many possible data
representations (box plots, violin plots, raw data points etc.), and
combine as desired. 'Durga' plots are implemented in base R, so are
compatible with base R methods for combining plots, such as 'layout()'.
See Khan & McLean (2023) <doi:10.1101/2023.02.06.526960>.

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

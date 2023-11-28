%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crqa
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Unidimensional and Multidimensional Methods for Recurrence Quantification Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-tseriesChaos 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-rdist 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-tseriesChaos 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-rdist 

%description
Auto, Cross and Multi-dimensional recurrence quantification analysis.
Different methods for computing recurrence, cross vs. multidimensional or
profile iti.e., only looking at the diagonal recurrent points, as well as
functions for optimization and plotting are proposed. in-depth measures of
the whole cross-recurrence plot, Please refer to Coco and others (2021)
<doi:10.32614/RJ-2021-062>, Coco and Dale (2014)
<doi:10.3389/fpsyg.2014.00510> and Wallot (2018) <doi:
10.1080/00273171.2018.1512846> for further details about the method.

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

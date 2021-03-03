%global packname  fdaoutlier
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Outlier Detection Tools for Functional Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
A collection of functions for outlier detection in functional data
analysis. Methods implemented include directional outlyingness by Dai and
Genton (2019) <doi:10.1016/j.csda.2018.03.017>, MS-plot by Dai and Genton
(2018) <doi:10.1080/10618600.2018.1473781>, total variation depth and
modified shape similarity index by Huang and Sun (2019)
<doi:10.1080/00401706.2019.1574241>, and sequential transformations by Dai
et al. (2020) <doi:10.1016/j.csda.2020.106960 among others. Additional
outlier detection tools and depths for functional data like functional
boxplot, (modified) band depth etc., are also available.

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

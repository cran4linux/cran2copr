%global packname  MatchItEXT
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Supplementary Function Set to 'MatchIt'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sure 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sure 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-stats 

%description
This function set is supplementary to 'MatchIt'. Its functions conduct
several computations that 'MatchIt' does not provide. It takes the
'MatchIt' result object and/or the original data to compute standardized
mean differences (SMD) between groups before and after matching. It also
calculates ratio of variances and ratio of residual variances. In
addition, it draws SMD comparison plots and QQ plots of distance measure
score to help diagnose the matching result.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  foodwebWrapper
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Enhanced Wrapper to Show Which Functions Call What

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvbutils 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-R2HTML 
BuildRequires:    R-CRAN-textshaping 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-mvbutils 
Requires:         R-utils 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-R2HTML 
Requires:         R-CRAN-textshaping 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-stringr 

%description
Enhances the functionality of the mvbutils::foodweb() program. The
matrix-format output of the original program contains identical row names
and column names, each name representing a retrieved function. This format
is enhanced by using the find_funs() program [see Sebastian (2017)
<https://sebastiansauer.github.io/finds_funs/>] to concatenate the package
name to the function name. Each package is assigned a unique color, that
is used to color code the text naming the packages and the functions. This
color coding is extended to the entries of value "1" within the matrix,
indicating the pattern of ancestor and descendent functions.

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

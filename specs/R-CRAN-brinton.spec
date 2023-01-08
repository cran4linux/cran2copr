%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  brinton
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          A Graphical EDA Tool

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-scales 

%description
An automated graphical exploratory data analysis (EDA) tool that
introduces: a.) wideplot graphics for exploring the structure of a dataset
through a grid of variables and graphic types. b.) longplot graphics,
which present the entire catalog of available graphics for representing a
particular variable using a grid of graphic types and variations on these
types. c.) plotup function, which presents a particular graphic for a
specific variable of a dataset. The plotup() function also makes it
possible to obtain the code used to generate the graphic, meaning that the
user can adjust its properties as needed. d.) matrixplot graphics that is
a grid of a particular graphic showing bivariate relationships between all
pairs of variables of a certain(s) type(s) in a multivariate data set.

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

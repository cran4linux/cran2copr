%global __brp_check_rpaths %{nil}
%global packname  miceRanger
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Imputation by Chained Equations with Random Forests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-foreach 

%description
Multiple Imputation has been shown to be a flexible method to impute
missing values by Van Buuren (2007) <doi:10.1177/0962280206074463>.
Expanding on this, random forests have been shown to be an accurate model
by Stekhoven and Buhlmann <arXiv:1105.0828> to impute missing values in
datasets. They have the added benefits of returning out of bag error and
variable importance estimates, as well as being simple to run in parallel.

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

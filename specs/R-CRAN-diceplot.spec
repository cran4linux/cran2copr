%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diceplot
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Categorical Data Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.14.8
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-data.table >= 1.14.8
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-sf 

%description
Easy visualization for datasets with more than two categorical variables
and additional continuous variables. 'diceplot' is particularly useful for
exploring complex categorical data in the context of pathway analysis
across multiple conditions. For a detailed documentation please visit
<https://dice-and-domino-plot.readthedocs.io/en/latest/>.

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

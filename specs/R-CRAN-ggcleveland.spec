%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggcleveland
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Implementation of Plots from Cleveland's Visualizing Data Book

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-egg 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-graphics 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-egg 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 

%description
William S. Cleveland's book 'Visualizing Data' is a classic piece of
literature on Exploratory Data Analysis. Although it was written several
decades ago, its content is still relevant as it proposes several tools
which are useful to discover patterns and relationships among the data
under study, and also to assess the goodness of fit o a model.  This
package provides functions to produce the 'ggplot2' versions of the
visualization tools described in this book and is thought to be used in
the context of courses on Exploratory Data Analysis.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  overviewR
%global packver   0.0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.13
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Extracting Information About Your Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-ggrepel >= 0.8.2
BuildRequires:    R-CRAN-ggvenn >= 0.1.8
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-ggrepel >= 0.8.2
Requires:         R-CRAN-ggvenn >= 0.1.8
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
Makes it easy to display descriptive information on a data set.  Getting
an easy overview of a data set by displaying and visualizing sample
information in different tables (e.g., time and scope conditions).  The
package also provides publishable 'LaTeX' code to present the sample
information.

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

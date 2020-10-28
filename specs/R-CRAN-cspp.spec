%global packname  cspp
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool for the Correlates of State Policy Project Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-purrr 

%description
A tool that imports, subsets, visualizes, and exports the Correlates of
State Policy Project dataset assembled by Marty P. Jordan and Matt
Grossmann (2020)
<http://ippsr.msu.edu/public-policy/correlates-state-policy>. The
Correlates data contains over 2000 variables across more than 100 years
that pertain to state politics and policy in the United States. Users with
only a basic understanding of R can subset this data across multiple
dimensions, export their search results, create map visualizations, export
the citations associated with their searches, and more.

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

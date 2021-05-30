%global packname  autocogs
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Cognostic Summaries

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-diptest 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-progress 

%description
Automatically calculates cognostic groups for plot objects and list column
plot objects.  Results are returned in a nested data frame.

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

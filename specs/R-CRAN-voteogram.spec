%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  voteogram
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          United States House and Senate Voting Cartogram Generators

License:          AGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
'ProPublica' <https://projects.propublica.org/represent/> makes United
States Congress member votes available and has developed their own unique
cartogram to visually represent this data. Tools are provided to retrieve
voting data, prepare voting data for plotting with 'ggplot2', create vote
cartograms and theme them.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BioTIMEr
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Use and Explore the 'BioTIME' Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dggridR >= 3.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-dggridR >= 3.1.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-checkmate 

%description
The 'BioTIME' database was first published in 2018 and inspired ideas,
questions, project and research article. To make it even more accessible,
an R package was created. The 'BioTIMEr' package provides tools designed
to interact with the 'BioTIME' database. The functions provided include
the 'BioTIME' recommended methods for preparing (gridding and rarefaction)
time series data, a selection of standard biodiversity metrics (including
species richness, numerical abundance and exponential Shannon) alongside
examples on how to display change over time. It also includes a sample
subset of both the query and meta data, the full versions of which are
freely available on the 'BioTIME' website
<https://biotime.st-andrews.ac.uk/home.php>.

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

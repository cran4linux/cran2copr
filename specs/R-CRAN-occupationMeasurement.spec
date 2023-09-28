%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  occupationMeasurement
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interactively Measure Occupations in Interviews and Beyond

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-stringdist >= 0.9.8
BuildRequires:    R-CRAN-tm >= 0.7.8
BuildRequires:    R-CRAN-text2vec >= 0.6.1
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-stringdist >= 0.9.8
Requires:         R-CRAN-tm >= 0.7.8
Requires:         R-CRAN-text2vec >= 0.6.1
Requires:         R-CRAN-digest 

%description
Perform interactive occupation coding during interviews as described in
Peycheva, D., Sakshaug, J., Calderwood, L. (2021)
<doi:10.2478/jos-2021-0042> and Schierholz, M., Gensicke, M., Tschersich,
N., Kreuter, F. (2018) <doi:10.1111/rssa.12297>. Generate suggestions for
occupational categories based on free text input, with pre-trained machine
learning models in German and a ready-to-use shiny application provided
for quick and easy data collection.

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

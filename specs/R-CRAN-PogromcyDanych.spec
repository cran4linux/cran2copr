%global __brp_check_rpaths %{nil}
%global packname  PogromcyDanych
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          DataCrunchers (PogromcyDanych) is the Massive Online Open Course that Brings R and Statistics to the People

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-SmarterPoland 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-SmarterPoland 

%description
The data sets used in the online course ,,PogromcyDanych''. You can
process data in many ways. The course Data Crunchers will introduce you to
this variety. For this reason we will work on datasets of different size
(from several to several hundred thousand rows), with various level of
complexity (from two to two thousand columns) and prepared in different
formats (text data, quantitative data and qualitative data). All of these
data sets were gathered in a single big package called PogromcyDanych to
facilitate access to them. It contains all sorts of data sets such as data
about offer prices of cars, results of opinion polls, information about
changes in stock market indices, data about names given to newborn babies,
ski jumping results or information about outcomes of breast cancer
patients treatment.

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

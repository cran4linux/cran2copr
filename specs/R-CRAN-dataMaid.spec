%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dataMaid
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Suite of Checks for Identification of Potential Errors in a Data Frame as Part of the Data Screening Process

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 1.10
BuildRequires:    R-CRAN-robustbase >= 0.93.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-whoami 
Requires:         R-CRAN-rmarkdown >= 1.10
Requires:         R-CRAN-robustbase >= 0.93.2
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-whoami 

%description
Data screening is an important first step of any statistical analysis.
dataMaid auto generates a customizable data report with a thorough summary
of the checks and the results that a human can use to identify possible
errors. It provides an extendable suite of test for common potential
errors in a dataset.

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

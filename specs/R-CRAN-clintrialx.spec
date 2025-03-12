%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clintrialx
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Connect and Work with Clinical Trials Data Sources

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-rmarkdown 

%description
Are you spending too much time fetching and managing clinical trial data?
Struggling with complex queries and bulk data extraction? What if you
could simplify this process with just a few lines of code? Introducing
'clintrialx' - Fetch clinical trial data from sources like
'ClinicalTrials.gov' <https://clinicaltrials.gov/> and the 'Clinical
Trials Transformation Initiative - Access to Aggregate Content of
ClinicalTrials.gov' database <https://aact.ctti-clinicaltrials.org/>,
supporting pagination and bulk downloads. Also, you can generate HTML
reports based on the data obtained from the sources!

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

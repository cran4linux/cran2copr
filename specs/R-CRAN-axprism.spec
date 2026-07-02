%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  axprism
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Client for the 'AxPrism' Institutional XBRL and Shariah Compliance API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 

%description
Provides an R client for the 'AxPrism' Application Programming Interface
(API) (<https://axprism.com>), which serves institutional financial data
in the eXtensible Business Reporting Language (XBRL) format together with
Shariah compliance screening. Supported compliance rulesets include those
of the Accounting and Auditing Organization for Islamic Financial
Institutions (AAOIFI), the Morgan Stanley Capital International (MSCI)
Islamic methodology, the Dow Jones Islamic Market (DJIM), the Financial
Times Stock Exchange (FTSE) and the Saudi Capital Market Authority (CMA).
Convenience functions wrap company fundamentals, compliance verdicts and
portfolio screening, company profiles, equity screeners, regulatory
disclosures and filing text search, and the Tadawul (Saudi Exchange),
Bursa Malaysia and Indonesia Stock Exchange (IDX) markets, as well as
webhooks and bulk data export. Requests use 'X-API-Key' header
authentication, automatic retries with exponential backoff, and a generic
request helper that covers all endpoints.

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

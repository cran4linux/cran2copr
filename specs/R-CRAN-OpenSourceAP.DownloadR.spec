%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OpenSourceAP.DownloadR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Open Source Asset Pricing (OpenAP) Data Directly

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-nanoparquet 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-getPass 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-nanoparquet 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-getPass 

%description
Convenient download functions enabling access Open Source Asset Pricing
(OpenAP) data. This package enables users to download predictor portfolio
returns (over 200 cross-sectional predictors with multiple portfolio
construction methods) and firm characteristics (over 200 characteristics
replicated from the academic asset pricing literature). Center for
Research in Security Prices (CRSP)-based variables such as Price, Size,
and Short-term Reversal can be downloaded with a Wharton Research Data
Services (WRDS, <https://wrds-www.wharton.upenn.edu/>) subscription. For a
full list of what is available, see <https://www.openassetpricing.com/>.
Data are read from the OpenAP Hugging Face dataset
<https://huggingface.co/datasets/OpenSourceAP/CrossSection>, which holds
data releases from 2020 onward.

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

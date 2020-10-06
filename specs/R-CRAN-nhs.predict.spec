%global packname  nhs.predict
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Breast Cancer Survival and Therapy Benefits

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Calculate Overall Survival or Recurrence-Free Survival for breast cancer
patients, using 'NHS Predict'. The time interval for the estimation can be
set up to 15 years, with default at 10. Incremental therapy benefits are
estimated for hormone therapy, chemotherapy, trastuzumab, and
bisphosphonates. An additional function, suited for SCAN audits, features
a more user-friendly version of the code, with fewer inputs, but
necessitates the correct standardised inputs. This work is not affiliated
with the development of 'NHS Predict' and its underlying statistical
model. Details on 'NHS Predict' can be found at: <doi:10.1186/bcr2464>.
The web version of 'NHS Predict': <https://breast.predict.nhs.uk/>. A
small dataset of 50 fictional patient observations is provided for the
purpose of running examples with the main two functions, and an additional
dataset is provided for running example with the dedicated SCAN function.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  carbonpredict
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Predict Carbon Emissions for UK SMEs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 

%description
Predict Scope 1, 2 and 3 carbon emissions for UK Small and Medium-sized
Enterprises (SMEs), using Standard Industrial Classification (SIC) codes
and annual turnover data, as well as Scope 1 carbon emissions for UK
farms. The 'carbonpredict' package provides single and batch prediction,
plotting, and workflow tools for carbon accounting and reporting. The
package utilises pre-trained models, leveraging rich classified
transaction data to accurately predict Scope 1, 2 and 3 carbon emissions
for UK SMEs as well as identifying emissions hotspots. It also provides
Scope 1 carbon emissions predictions for UK farms of types: Cereals ex.
rice, Dairy, Mixed farming, Sheep and goats, Cattle & buffaloes, Poultry,
Animal production and Support for crop production. The methodology used to
produce the estimates in this package is fully detailed in the following
peer-reviewed publications: Phillpotts, A., Owen. A., Norman, J., Trendl,
A., Gathergood, J., Jobst, Norbert., Leake, D. (2025)
<doi:10.1111/jiec.70106> "Bridging the SME Reporting Gap: A New Model for
Predicting Scope 1 and 2 Emissions" and Wells, J., Trendl, A., Owen, A.,
Barrett, J., Gridley, J., Jobst, N., Leake, D. (2025)
<doi:10.1088/1748-9326/ae20ab> "A Scalable Tool for Farm-Level Carbon
Accounting: Evidence from UK Agriculture".

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

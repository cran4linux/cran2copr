%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CompareMultipleModels
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Finding the Best Model Using Eight Metrics Values

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CEEMDANML 
Requires:         R-CRAN-CEEMDANML 

%description
In statistical modeling, multiple models need to be compared based on
certain criteria. The method described here uses eight metrics from
'AllMetrics' package. ‘input_df’ is the data frame (at least two columns
for comparison) containing metrics values in different rows of a column
(which denotes a particular model’s performance). First five metrics are
expected to be minimum and last three metrics are expected to be maximum
for a model to be considered good. Firstly, every metric value (among
first five) is searched in every columns and minimum values are denoted as
‘MIN’ and other values are denoted as ‘NA’. Secondly, every metric (among
last three) is searched in every columns and maximum values are denoted as
‘MAX’ and other values are denoted as ‘NA’. ‘output_df’ contains the
similar number of rows (which is 8) and columns (which is number of models
to be compared) as of ‘input_df’. Values in ‘output_df’ are corresponding
‘NA’, ‘MIN’ or ‘MAX’. Finally, the column containing minimum number of
‘NA’ values is denoted as the best column. ‘min_NA_col’ gives the name of
the best column (model). ‘min_NA_values’ are the corresponding metrics
values. ‘BestColumn_metrics’ is the data frame (dimension: 1*8) containing
different metrics of the best column (model). ‘best_column_results’ is the
final result (a list) containing all of these output elements. In special
case, if two columns having equal 'NA', it will be checked among these two
column which one is having least 'NA' in first five rows and will be
inferred as the best. More details about 'AllMetrics' can be found in
Garai (2023) <doi:10.13140/RG.2.2.18688.30723>.

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

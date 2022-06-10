%global __brp_check_rpaths %{nil}
%global packname  uscoauditlog
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          United States Copyright Office Product Management Division SR Audit Data Dataset Cleaning Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-readxl 

%description
Intended to be used by the United States Copyright Office Product
Management Division Business Analysts. Include algorithms for the United
States Copyright Office Product Management Division SR Audit Data dataset.
The algorithm takes in the SR Audit Data excel file and reformat the
spreadsheet such that the values and variables fit the format of the
online database. Support functions in this package include clean_str(),
which cleans instances of variable AUDIT_LOG; clean_data_to_excel(), which
cleans and output the reorganized SR Audit Data dataset in excel format;
clean_data_to_dataframe(), which cleans and stores the reorganized SR
Audit Data data set to a data frame; format_from_excel(), which reads in
the outputted excel file from the clean_data_to_excel() function and
formats and returns the data as a dictionary that uses FIELD types as keys
and NON-FIELD types as the values of those keys. format_from_dataframe(),
which reads in the outputted data frame from the clean_data_to_dataframe()
function and formats and returns the data as a dictionary that uses FIELD
types as keys and NON-FIELD types as the values of those keys;
support_function(), which takes in the dictionary outputted either from
the format_from_dataframe() or format_from_excel() function and returns
the data as a formatted data frame according to the original U.S.
Copyright Office SR Audit Data online database. The main function of this
package is clean_format_all(), which takes in an excel file and returns
the formatted data into a new excel and text file according to the format
from the U.S. Copyright Office SR Audit Data online database.

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

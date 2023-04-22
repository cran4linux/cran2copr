%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MissingHandle
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Handles Missing Dates and Data and Converts into Weekly from Daily

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-imputeTS 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-imputeTS 
Requires:         R-CRAN-dplyr 

%description
Many times, you will not find data for all dates. After first January,
2011 you may have next data on 20th January, 2011 and so on. Also
available dates may have zero values. Try to gather all such kinds of data
in different excel sheets of a single excel file. Every sheet will contain
two columns (1st one is dates and second one is the data). After loading
all the sheets into different elements of a list, using this you can fill
the gaps for all the sheets and mark all the corresponding values as
zeros. Here I am talking about daily data. Finally, it will combine all
the filled results into one data frame (first column is date and other
columns will be corresponding values of your sheets) and give one csv
file. Number of columns in the data frame will be number of sheets plus
one. Then imputation will be done. Daily to weekly conversion is also
possible.  More details can be found in Garai and others (2023)
<doi:10.13140/RG.2.2.11977.42087>.

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

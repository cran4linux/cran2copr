%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  binomialtrend
%global packver   0.0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates the Statistical Significance of a Trend in a Set of Measurements

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-pheatmap 
Requires:         R-CRAN-pheatmap 

%description
Detection of a statistically significant trend in the data provided by the
user. This is based on the a signed test based on the binomial
distribution. The package returns a trend test value, T, and also a
p-value. A T value close to 1 indicates a rising trend, whereas a T value
close to -1 indicates a decreasing trend. A T value close to 0 indicates
no trend. There is also a command to visualize the trend. A test data set
called gtsa_data is also available, which has global mean temperatures for
January, April, July, and October for the years 1851 to 2022. Reference:
Walpole, Myers, Myers, Ye. (2007, ISBN: 0-13-187711-9).

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

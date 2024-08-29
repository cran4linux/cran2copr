%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DataSum
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Data Summarization for Statistical Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-stats 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nortest 
Requires:         R-stats 

%description
Summarizing data frames by calculating various statistical measures,
including measures of central tendency, dispersion, skewness(),
kurtosis(), and normality tests. The package leverages the 'moments'
package for calculating statistical moments and related measures, the
'dplyr' package for data manipulation, and the 'nortest' package for
normality testing. 'DataSum' includes functions such as getmode() for
finding the mode(s) of a data vector, shapiro_normality_test() for
performing the Shapiro-Wilk test (Shapiro & Wilk 1965
<doi:10.1093/biomet/52.3-4.591>) (or the Anderson-Darling test when the
data length is outside the valid range for the Shapiro-Wilk test)
(Stephens 1974 <doi:10.1080/01621459.1974.10480196>), Datum() for
generating a comprehensive summary of a data vector with various
statistics (including data type, sample size, mean, mode, median,
variance, standard deviation, maximum, minimum, range, skewness(),
kurtosis(), and normality test result) (Joanes & Gill 1998
<doi:10.1111/1467-9884.00122>), and DataSumm() for applying the Datum()
function to each column of a data frame. Emphasizing the importance of
normality testing, the package provides robust tools to validate whether
data follows a normal distribution, a fundamental assumption in many
statistical analyses and models.

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

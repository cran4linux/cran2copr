%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  codecountR
%global packver   0.0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Counting Codes in a Text and Preparing Data for Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Data analysis frequently requires coding, in particular when data are
collected by interviews, by observations or even by questionnaires.
Therefore, code counting and data preparation are necessary phases to
carry out the analysis. Thus, the analysts will wish to count the codes
inserted in a text (tokenization and counting of a list of pre-established
codes) and to carry out the preparation of the data (feature scaling
min-max normalization, Zscore, Box and Cox transformation, Yeo and Johnson
transformation, median absolute deviation). For Box and Cox (1964)
<https://www.jstor.org/stable/2984418> transformation, optimal Lambda is
calculated by correlation coefficient test inspired of Lye (1993)
<doi:10.1139/l93-101>. The same method is used for the calculation of the
optimal lambda for Yeo and Johnson (2000) <doi:10.1093/biomet/87.4.954>
transformation. Median absolute deviation is calculated on the basis of
Leys et al (1993) <doi:10.1016/j.jesp.2013.03.013>. Package for
educational purposes.

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

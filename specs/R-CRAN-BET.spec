%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BET
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Binary Expansion Testing

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-Rcpp >= 0.12.3

%description
Nonparametric detection of nonuniformity and dependence with Binary
Expansion Testing (BET). See Kai Zhang (2019) BET on Independence, Journal
of the American Statistical Association, 114:528, 1620-1637,
<DOI:10.1080/01621459.2018.1537921>, Kai Zhang, Wan Zhang, Zhigen Zhao,
Wen Zhou. (2023). BEAUTY Powered BEAST, <doi:10.48550/arXiv.2103.00674>
and Wan Zhang, Zhigen Zhao, Michael Baiocchi, Yao Li, Kai Zhang. (2023)
SorBET: A Fast and Powerful Algorithm to Test Dependence of Variables,
Techinical report.

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

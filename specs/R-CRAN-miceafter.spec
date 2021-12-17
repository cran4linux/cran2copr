%global __brp_check_rpaths %{nil}
%global packname  miceafter
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data and Statistical Analyses after Multiple Imputation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 6.1.0
BuildRequires:    R-CRAN-mice >= 3.12.0
BuildRequires:    R-CRAN-survival >= 3.1.12
BuildRequires:    R-CRAN-tibble >= 3.0.4
BuildRequires:    R-CRAN-car >= 3.0.10
BuildRequires:    R-CRAN-mitools >= 2.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-pROC >= 1.16.2
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-mitml >= 0.3.7
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-rms >= 6.1.0
Requires:         R-CRAN-mice >= 3.12.0
Requires:         R-CRAN-survival >= 3.1.12
Requires:         R-CRAN-tibble >= 3.0.4
Requires:         R-CRAN-car >= 3.0.10
Requires:         R-CRAN-mitools >= 2.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-pROC >= 1.16.2
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-mitml >= 0.3.7
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 

%description
Statistical Analyses and Pooling after Multiple Imputation. A large
variety of repeated statistical analysis can be performed and finally
pooled. Statistical analysis that are available are, among others,
Levene's test, Odds and Risk Ratios, One sample proportions, difference
between proportions and linear and logistic regression models. Functions
can also be used in combination with the Pipe operator. More and more
statistical analyses and pooling functions will be added over time.
Heymans (2007) <doi:10.1186/1471-2288-7-33>. Eekhout (2017)
<doi:10.1186/s12874-017-0404-7>. Wiel (2009)
<doi:10.1093/biostatistics/kxp011>. Marshall (2009)
<doi:10.1186/1471-2288-9-57>. Sidi (2021)
<doi:10.1080/00031305.2021.1898468>. Lott (2018)
<doi:10.1080/00031305.2018.1473796>. Grund (2021)
<doi:10.31234/osf.io/d459g>.

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

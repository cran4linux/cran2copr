%global __brp_check_rpaths %{nil}
%global packname  ELISAtools
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          ELISA Data Analysis with Batch Correction

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R2HTML >= 2.3.2
BuildRequires:    R-CRAN-minpack.lm >= 1.2.1
BuildRequires:    R-CRAN-stringi >= 1.1.7
BuildRequires:    R-methods 
Requires:         R-CRAN-R2HTML >= 2.3.2
Requires:         R-CRAN-minpack.lm >= 1.2.1
Requires:         R-CRAN-stringi >= 1.1.7
Requires:         R-methods 

%description
To run data analysis for enzyme-link immunosorbent assays (ELISAs). Either
the five- or four-parameter logistic model will be fitted for data of
single ELISA. Moreover, the batch effect correction/normalization will be
carried out, when there are more than one batches of ELISAs. Feng (2018)
<doi:10.1101/483800>.

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

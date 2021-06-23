%global __brp_check_rpaths %{nil}
%global packname  coefficientalpha
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          2%{?dist}%{?buildtag}
Summary:          Robust Coefficient Alpha and Omega with Missing and Non-NormalData

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rsem 
BuildRequires:    R-CRAN-lavaan 
Requires:         R-CRAN-rsem 
Requires:         R-CRAN-lavaan 

%description
Cronbach's alpha and McDonald's omega are widely used reliability or
internal consistency measures in social, behavioral and education
sciences. Alpha is reported in nearly every study that involves measuring
a construct through multiple test items. The package 'coefficientalpha'
calculates coefficient alpha and coefficient omega with missing data and
non-normal data. Robust standard errors and confidence intervals are also
provided. A test is also available to test the tau-equivalent and
homogeneous assumptions. Since Version 0.5, the bootstrap confidence
intervals were added.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

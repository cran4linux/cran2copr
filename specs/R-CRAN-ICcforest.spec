%global __brp_check_rpaths %{nil}
%global packname  ICcforest
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Ensemble Method for Interval-Censored Survival Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-icenReg 
BuildRequires:    R-CRAN-ipred 
Requires:         R-CRAN-partykit 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-survival 
Requires:         R-CRAN-icenReg 
Requires:         R-CRAN-ipred 

%description
Implements the conditional inference forest approach to modeling
interval-censored survival data. It also provides functions to tune the
parameters and evaluate the model fit. See Yao et al. (2019)
<arXiv:1901.04599>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

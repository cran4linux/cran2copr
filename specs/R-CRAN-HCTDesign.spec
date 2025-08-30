%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HCTDesign
%global packver   0.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Group Sequential Design for Historical Control Trial with Survival Outcome

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-diversitree 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-diversitree 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-flexsurv 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-crayon 

%description
It provides functions to design historical controlled trials with survival
outcome by group sequential method. The options for interim look
boundaries are efficacy only, efficacy & futility or futility only. It
also provides the function to monitor the trial for any unplanned look.
The package is based on Jianrong Wu, Xiaoping Xiong (2016)
<doi:10.1002/pst.1756> and Jianrong Wu, Yimei Li (2020)
<doi:10.1080/10543406.2019.1684305>.

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

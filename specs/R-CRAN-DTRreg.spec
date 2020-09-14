%global packname  DTRreg
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          DTR Estimation and Inference via G-Estimation, Dynamic WOLS, Q-Learning, and Dynamic Weighted Survival Modeling (DWSurv)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-MASS 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-MASS 

%description
Dynamic treatment regime estimation and inference via G-estimation,
dynamic weighted ordinary least squares (dWOLS) and Q-learning. Inference
via bootstrap and (for G-estimation) recursive sandwich estimation.
Estimation and inference for survival outcomes via Dynamic Weighted
Survival Modeling (DWSurv). Extension to continuous treatment variables
(gdwols). Wallace et al. (2017) <DOI:10.18637/jss.v080.i02>; Simoneau et
al. (2020) <DOI:10.1080/00949655.2020.1793341>.

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

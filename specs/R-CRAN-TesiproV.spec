%global __brp_check_rpaths %{nil}
%global packname  TesiproV
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Calculation of Reliability and Failure Probability in Civil Engineering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-edfun 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-nloptr 
Requires:         R-methods 
Requires:         R-CRAN-edfun 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Calculate the failure probability of civil engineering problems with Level
I up to Level III Methods. Have fun and enjoy. References: Spaethe (1991,
ISBN:3-211-82348-4) "Die Sicherheit tragender Baukonstruktionen", AU,BECK
(2001) "Estimation of small failure probabilities in high dimensions by
subset simulation." <doi:10.1016/S0266-8920(01)00019-4>, Breitung (1989)
"Asymptotic approximations for probability integrals."
<doi:10.1016/0266-8920(89)90024-6>.

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

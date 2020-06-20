%global packname  distdichoR
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Distributional Method for the Dichotomisation of ContinuousOutcomes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-stats 
BuildRequires:    R-nlme 
Requires:         R-boot 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-emmeans 
Requires:         R-stats 
Requires:         R-nlme 

%description
Contains a range of functions covering the present development of the
distributional method for the dichotomisation of continuous outcomes. The
method provides estimates with standard error of a comparison of
proportions (difference, odds ratio and risk ratio) derived, with similar
precision, from a comparison of means. See the URL below or
<arXiv:1809.03279> for more information.

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

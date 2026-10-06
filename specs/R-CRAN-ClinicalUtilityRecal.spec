%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ClinicalUtilityRecal
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Recalibration Methods for Improved Clinical Utility of Risk Scores

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-nloptr 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-nloptr 

%description
Recalibrate risk scores (predicting binary outcomes) to improve clinical
utility of risk score using weighted logistic or constrained logistic
recalibration methods. Additionally, produces plots to assess the
potential for recalibration to improve the clinical utility of a risk
model. Methods are described in detail in Mishra, A. (2019) "Methods for
Risk Markers that Incorporate Clinical Utility"
<http://hdl.handle.net/1773/44068>.

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

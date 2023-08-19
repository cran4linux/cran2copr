%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MetabolicSyndrome
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnosis of Metabolic Syndrome

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-dplyr 

%description
The modified Adult Treatment Panel -III guidelines (ATP-III) proposed by
American Heart Association (AHA) and National Heart, Lung and Blood
Institute (NHLBI) are used widely for the clinical diagnosis of Metabolic
Syndrome. The AHA-NHLBI criteria advise using parameters such as waist
circumference (WC), systolic blood pressure (SBP), diastolic blood
pressure (DBP), fasting plasma glucose (FPG), triglycerides (TG) and
high-density lipoprotein cholesterol (HDLC) for diagnosis of metabolic
syndrome. Each parameter has to be interpreted based on the proposed
cut-offs, making the diagnosis slightly complex and error-prone. This
package is developed by incorporating the modified ATP-III guidelines, and
it will aid in the easy and quick diagnosis of metabolic syndrome in busy
healthcare settings and also for research purposes. The modified
ATP-III-AHA-NHLBI criteria for the diagnosis is described by Grundy et al
., (2005) <doi:10.1161/CIRCULATIONAHA.105.169404>.

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

%global packname  BHTSpack
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Multi-Plate High-Throughput Screening of Compounds

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-R2HTML >= 2.3.2
BuildRequires:    R-CRAN-xtable >= 1.8.2
Requires:         R-CRAN-R2HTML >= 2.3.2
Requires:         R-CRAN-xtable >= 1.8.2

%description
Can be used for joint identification of candidate compound hits from
multiple assays, in drug discovery. This package implements the framework
of I. D. Shterev, D. B. Dunson, C. Chan and G. D. Sempowski. "Bayesian
Multi-Plate High-Throughput Screening of Compounds", Scientific Reports
8(1):9551, 2018. This project was funded by the Division of Allergy,
Immunology, and Transplantation, National Institute of Allergy and
Infectious Diseases, National Institutes of Health, Department of Health
and Human Services, under contract No. HHSN272201400054C entitled
"Adjuvant Discovery For Vaccines Against West Nile Virus and Influenza",
awarded to Duke University and lead by Drs. Herman Staats and Soman
Abraham.

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

%global __brp_check_rpaths %{nil}
%global packname  highSCREEN
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          High-Throughput Screening for Plate Based Essays

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots >= 3.0.1
Requires:         R-CRAN-gplots >= 3.0.1

%description
Can be used to carry out extraction, normalization, quality control (QC),
candidate hits identification and visualization for plate based assays, in
drug discovery. The package methods were applied in H. W. Choi et al.
"Identification of Novel Mast Cell Activators Using Cell-Based
High-Throughput Screening", SLAS Discovery 24(6), 2019. This project was
funded by the Division of Allergy, Immunology, and Transplantation,
National Institute of Allergy and Infectious Diseases, National Institutes
of Health, Department of Health and Human Services, under contract No.
HHSN272201400054C entitled "Adjuvant Discovery For Vaccines Against West
Nile Virus and Influenza", awarded to Duke University and lead by Drs.
Herman Staats and Soman Abraham.

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

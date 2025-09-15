%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MAFLD
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnosis of Metabolic Dysfunction Associated Fatty Liver Disease

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-dplyr 

%description
The latest guidelines proposed by International Expert Consensus are used
for the clinical diagnosis of Metabolic Associated Fatty Liver Disease
(MAFLD). The new definition takes hepatic steatosis (determined by
elastography or histology or biomarker-based fatty liver index) as a major
criterion. In addition, race, gender, body mass index (BMI), waist
circumference (WC), fasting plasma glucose (FPG), systolic blood pressure
(SBP), diastolic blood pressure (DBP), triglycerides (TG), high-density
lipoprotein cholesterol (HDLC), homeostatic model assessment of insulin
resistance (HOMAIR), high sensitive c-reactive protein (HsCRP) for the
diagnosis of MAFLD. Each parameter has to be interpreted based on the
proposed cut-offs, making the diagnosis slightly complex and error-prone.
This package is developed by incorporating the latest international expert
consensus guidelines, and it will aid in the easy and quick diagnosis of
MAFLD based on FibroScan in busy healthcare settings and also for research
purposes. The new definition for MAFLD as per the International Consensus
Statement is described by Eslam M et al (2020).
<doi:10.1016/j.jhep.2020.03.039>.

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

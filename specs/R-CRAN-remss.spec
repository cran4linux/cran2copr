%global packname  remss
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Refining Evaluation Methodology on Stage System

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-survival 

%description
T (extent of the primary tumor), N (absence or presence and extent of
regional lymph node metastasis) and M (absence or presence of distant
metastasis) are three components to describe the anatomical tumor extent.
TNM stage is important in treatment decision-making and outcome
predicting. The existing oropharyngeal Cancer (OPC) TNM stages have not
made distinction of the two sub sites of Human papillomavirus positive
(HPV+) and Human papillomavirus negative (HPV-) diseases. We developed
novel criteria to assess performance of the TNM stage grouping schemes
based on parametric modeling adjusting on important clinical factors.
These criteria evaluate the TNM stage grouping scheme in five different
measures: hazard consistency, hazard discrimination, explained variation,
likelihood difference, and balance. The methods are described in Xu, W.,
et al. (2015)
<https://www.austinpublishinggroup.com/biometrics/fulltext/biometrics-v2-id1014.php>.

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

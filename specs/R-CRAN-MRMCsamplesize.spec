%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MRMCsamplesize
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size Estimations for Planning Multi-Reader Multi-Case (MRMC) Studies Without Pilot Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fpow 
Requires:         R-stats 
Requires:         R-CRAN-fpow 

%description
Sample size estimations for MRMC studies based on the Obuchowski-Rockette
(OR) methodology is implemented. The function can calculate sample sizes
where the endpoint of interest in the study is either ROC AUC
(Area-Under-the-Receiver-Operating-Characteristics-Curve) or sensitivity.
The package can also return sample sizes for studies expected to have
clustering effect (e.g.- multiple pulmonary nodules per patient). All
calculations assume that the study design is fully crossed (paired-reader,
paired-case) where each reader reads/interprets each case and that there
are two interventions/imaging-modalities/techniques in the study. In
addition to MRMC, it can also be used to estimate sample sizes for
standalone studies where sensitivity or AUC are the primary endpoints. The
methods implemented are based on the methods described in Zhou et.al.
(2011) <doi:10.1002/9780470906514> and Obuchowski (2000)
<doi:10.1097/EDE.0b013e3181a663cc>.

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

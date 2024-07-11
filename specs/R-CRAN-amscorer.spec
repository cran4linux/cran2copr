%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  amscorer
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clinical Scores Calculator for Healthcare

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Provides functions to compute various clinical scores used in healthcare.
These include the Charlson Comorbidity Index (CCI), predicting 10-year
survival in patients with multiple comorbidities; the EPICES score, an
individual indicator of precariousness considering its multidimensional
nature; the MELD score for chronic liver disease severity; the Alternative
Fistula Risk Score (a-FRS) for postoperative pancreatic fistula risk; and
the Distal Pancreatectomy Fistula Risk Score (D-FRS) for risk following
distal pancreatectomy. For detailed methodology, refer to Charlson et al.
(1987) <doi:10.1016/0021-9681(87)90171-8> , Sass et al. (2006)
<doi:10.1007/s10332-006-0131-5>, Kamath et al. (2001)
<doi:10.1053/jhep.2001.22172>, Kim et al. (2008)
<doi:10.1056/NEJMoa0801209> Kim et al. (2021)
<doi:10.1053/j.gastro.2021.08.050>, Mungroop et al. (2019)
<doi:10.1097/SLA.0000000000002620>, and de Pastena et al. (2023)
<doi:10.1097/SLA.0000000000005497>..

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

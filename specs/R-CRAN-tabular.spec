%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tabular
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Render Tables, Listings, and Figures for Clinical Submissions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-xml2 

%description
Render clinical submission tables, listings, and figures to 'RTF',
'LaTeX', 'Typst', 'HTML', 'PDF', and 'DOCX' from pre-summarised data
frames, with no external 'Java' or 'SAS' dependency. Features include
decimal alignment via font metrics, multi-level column headers with
passthrough leaves, predicate-targeted cell styling, footnotes,
group-aware pagination, and figures that wrap a plot or image in the same
page chrome as a table. Built for Clinical Data Interchange Standards
Consortium (CDISC) Analysis Data Model (ADaM) workflows and regulatory
submissions to agencies such as the Food and Drug Administration (FDA),
European Medicines Agency (EMA), and Pharmaceuticals and Medical Devices
Agency (PMDA).

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

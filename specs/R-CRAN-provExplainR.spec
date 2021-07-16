%global __brp_check_rpaths %{nil}
%global packname  provExplainR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Compare Provenance Collections to Explain Changed Script Outputs

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-provParseR >= 0.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-diffobj 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-provParseR >= 0.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-diffobj 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-stringr 

%description
Inspects provenance collected by the 'rdt' or 'rdtLite' packages, or other
tools providing compatible PROV JSON output created by the execution of a
script, and find differences between two provenance collections. Factors
under examination included the hardware and software used to execute the
script, versions of attached libraries, use of global variables, modified
inputs and outputs, and changes in main and sourced scripts. Based on
detected changes, 'provExplainR' can be used to study how these factors
affect the behavior of the script and generate a promising diagnosis of
the causes of different script results. More information about 'rdtLite'
and associated tools is available at
<https://github.com/End-to-end-provenance/> and Barbara Lerner, Emery
Boose, and Luis Perez (2018), Using Introspection to Collect Provenance in
R, Informatics, <doi:10.3390/informatics5010012>.

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

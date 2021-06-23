%global __brp_check_rpaths %{nil}
%global packname  provSummarizeR
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Summarizes Provenance Related to Inputs and Outputs of a Scriptor Console Commands

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-provParseR >= 0.3
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-provParseR >= 0.3
Requires:         R-CRAN-dplyr 

%description
Reads the provenance collected by the 'rdt' or 'rdtLite' packages, or
other tools providing compatible PROV JSON output created by the execution
of a script, and provides a human-readable summary identifying the input
and output files, the script used (if any), errors and warnings produced,
and the environment in which it was executed.  It can also optionally
package all the files into a zip file.  The exact format of the JSON
created by 'rdt' and 'rdtLite' is described in
<https://github.com/End-to-end-provenance/ExtendedProvJson>. More
information about 'rdtLite' and associated tools is available at
<https://github.com/End-to-end-provenance/> and Barbara Lerner, Emery
Boose, and Luis Perez (2018), Using Introspection to Collect Provenance in
R, Informatics, <doi: 10.3390/informatics5010012>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

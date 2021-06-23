%global __brp_check_rpaths %{nil}
%global packname  TRAMPR
%global packver   1.0-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          3%{?dist}%{?buildtag}
Summary:          'TRFLP' Analysis and Matching Package for R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4
Requires:         R-core >= 2.4
BuildArch:        noarch

%description
Matching terminal restriction fragment length polymorphism ('TRFLP')
profiles between unknown samples and a database of known samples.
'TRAMPR' facilitates analysis of many unknown profiles at once, and
provides tools for working directly with electrophoresis output through to
generating summaries suitable for community analyses with R's rich set of
statistical functions.  'TRAMPR' also resolves the issues of multiple
'TRFLP' profiles within a species, and shared 'TRFLP' profiles across
species.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/demo_samples_abi_info_full.csv
%doc %{rlibdir}/%{packname}/demo_samples_abi_soilcore.csv
%doc %{rlibdir}/%{packname}/demo_samples_abi_template_full.csv
%doc %{rlibdir}/%{packname}/demo_samples_abi.txt
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global packname  esmprep
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Data Preparation During and After the Use of the ExperienceSampling Methodology (ESM)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-lubridate >= 1.6.0

%description
Support in preparing a raw ESM dataset for statistical analysis.
Preparation includes the handling of errors (mostly due to technological
reasons) and the generating of new variables that are necessary and/or
helpful in meeting the conditions when statistically analyzing ESM data.
The functions in 'esmprep' are meant to hierarchically lead from bottom,
i.e. the raw (separated) ESM dataset(s), to top, i.e. a single ESM dataset
ready for statistical analysis. This hierarchy evolved out of my personal
experience in working with ESM data.

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
%{rlibdir}/%{packname}/INDEX

%global packname  CrossVA
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          2%{?dist}
Summary:          Verbal Autopsy Data Transformation for InSilicoVA and InterVA5Algorithms

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-stringi 

%description
Enables transformation of Verbal Autopsy data collected with the WHO 2016
questionnaire (versions 1.4.1 & 1.5.1) or the WHO 2014 questionnaire for
automated coding of Cause of Death using the InSilicoVA (data.type =
"WHO2016") and InterVA5 algorithms. Previous versions of this package
supported user-supplied mappings (via the map_records function), but this
functionality has been removed.  This package is made available by WHO and
the Bloomberg Data for Health Initiative.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/sample
%{rlibdir}/%{packname}/INDEX

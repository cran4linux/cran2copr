%global packname  SoyNAM
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Soybean Nested Association Mapping Dataset

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-NAM 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-NAM 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-reshape2 

%description
Genomic and multi-environmental soybean data. Soybean Nested Association
Mapping (SoyNAM) project dataset funded by the United Soybean Board (USB).
See <doi.org/10.1534/g3.118.200332> and <doi.org/10.1534/g3.117.300300>.
BLUP function formats data for genome-wide prediction and association
analysis.

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

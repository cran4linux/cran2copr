%global packname  daff
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Diff, Patch and Merge for Data.frames

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-V8 >= 0.6
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
Requires:         R-CRAN-V8 >= 0.6
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 

%description
Diff, patch and merge for data frames. Document changes in data sets and
use them to apply patches. Changes to data can be made visible by using
render_diff. The V8 package is used to wrap the 'daff.js' JavaScript
library which is included in the package.

%prep
%setup -q -c -n %{packname}


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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/html_templates
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/useR2017
%{rlibdir}/%{packname}/INDEX

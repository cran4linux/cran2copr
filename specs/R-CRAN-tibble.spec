%global packname  tibble
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          3%{?dist}
Summary:          Simple Data Frames

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-pillar >= 1.4.3
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-rlang >= 0.4.3
BuildRequires:    R-CRAN-fansi >= 0.4.0
BuildRequires:    R-CRAN-vctrs >= 0.2.4
BuildRequires:    R-CRAN-ellipsis >= 0.2.0
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pkgconfig 
BuildRequires:    R-utils 
Requires:         R-CRAN-pillar >= 1.4.3
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-rlang >= 0.4.3
Requires:         R-CRAN-fansi >= 0.4.0
Requires:         R-CRAN-vctrs >= 0.2.4
Requires:         R-CRAN-ellipsis >= 0.2.0
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-pkgconfig 
Requires:         R-utils 

%description
Provides a 'tbl_df' class (the 'tibble') that provides stricter checking
and better formatting than the traditional data frame.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

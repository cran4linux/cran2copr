%global packname  rsample
%global packver   0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          3%{?dist}
Summary:          General Resampling Infrastructure

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-methods 
Requires:         R-CRAN-generics 
Requires:         R-utils 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-tidyr 

%description
Classes and functions to create and summarize different types of
resampling objects (e.g. bootstrap, cross-validation).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

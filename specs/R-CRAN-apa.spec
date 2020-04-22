%global packname  apa
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Format Outputs of Statistical Tests According to APA Guidelines

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.4
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr >= 0.4
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MBESS 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 

%description
Formatter functions in the 'apa' package take the return value of a
statistical test function, e.g. a call to chisq.test() and return a string
formatted according to the guidelines of the APA (American Psychological
Association).

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

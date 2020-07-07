%global packname  siteymlgen
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Automatically Generate _site.yml File for 'R Markdown'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ymlthis 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ymlthis 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-purrr 

%description
The goal of 'siteymlgen' is to make it easy to organise the building of
your 'R Markdown' website. The init() function placed within the first
code chunk of the index.Rmd file of an 'R' project directory will initiate
the generation of an automatically written _site.yml file. 'siteymlgen'
recommends a specific naming convention for your 'R Markdown' files. This
naming will ensure that your navbar layout is ordered according to a
hierarchy.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

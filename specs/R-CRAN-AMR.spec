%global packname  AMR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Antimicrobial Resistance Analysis

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.0
BuildRequires:    R-CRAN-crayon >= 1.3.0
BuildRequires:    R-CRAN-knitr >= 1.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-cleaner 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-pillar 
Requires:         R-CRAN-data.table >= 1.9.0
Requires:         R-CRAN-crayon >= 1.3.0
Requires:         R-CRAN-knitr >= 1.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-backports 
Requires:         R-CRAN-cleaner 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-pillar 

%description
Functions to simplify the analysis and prediction of Antimicrobial
Resistance (AMR) and to work with microbial and antimicrobial properties
by using evidence-based methods, like those defined by Leclercq et al.
(2013) <doi:10.1111/j.1469-0691.2011.03703.x> and the Clinical and
Laboratory Standards Institute (2014) <isbn: 1-56238-899-1>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX

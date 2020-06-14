%global packname  crsra
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          Tidying and Analyzing 'Coursera' Research Export Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rcorpora 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rcorpora 
Requires:         R-CRAN-knitr 

%description
Tidies and performs preliminary analysis of 'Coursera' research export
data. These export data can be downloaded by anyone who has classes on
Coursera and wants to analyze the data. Coursera is one of the leading
providers of MOOCs and was launched in January 2012. With over 25 million
learners, Coursera is the most popular provider in the world being
followed by EdX, the MOOC provider that was a result of a collaboration
between Harvard University and MIT, with over 10 million users. Coursera
has over 150 university partners from 29 countries and offers a total of
2000+ courses from computer science to philosophy. Besides, Coursera
offers 180+ specialization, Coursera's credential system, and four fully
online Masters degrees. For more information about Coursera check
Coursera's About page on <https://blog.coursera.org/about/>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
